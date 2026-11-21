"""Load the reviewed wave slot sequences; no publication or reservations."""
import json
import re
from collections import Counter

BASELINE = 495
BASELINE_COMMIT = "c087eb9816db395317dafd9e104f0657726e59ab"
BASELINE_CAPS = {
    "ACC": 40, "FIN": 50, "MKT": 40, "OPS": 40, "PPL": 40, "STR": 40,
    "ENT": 40, "IS": 40, "GVR": 40, "SUS": 40, "ECO": 45, "HSP": 40,
}

SECOND_BASELINE = 516
SECOND_BASELINE_COMMIT = "9beed46db5e049854a3535e18db4ccc4dfa3e7dd"
THIRD_BASELINE = 537
THIRD_BASELINE_COMMIT = "d503315e1850824538d8e9841434346cb9c127c4"
MIXED_ORDER = ("ACC","MKT","OPS","PPL","STR","ENT","IS","GVR","SUS","HSP")

def load_wave(root, wave=1, initial_caps=None):
    """Read a strictly bounded plan, then derive area ceilings."""
    if wave == 1:
        baseline, commit, caps, eco = BASELINE, BASELINE_COMMIT, BASELINE_CAPS, "ECO-46"
    elif wave == 2:
        baseline, commit, eco = SECOND_BASELINE, SECOND_BASELINE_COMMIT, "ECO-47"
        if initial_caps is None:
            _, initial_caps = load_wave(root)
        caps = initial_caps
    elif wave == 3:
        baseline, commit, eco = THIRD_BASELINE, THIRD_BASELINE_COMMIT, "ECO-48"
        if initial_caps is None:
            _, initial_caps = load_wave(root, 2)
        caps = initial_caps
    else:
        raise ValueError("Unsupported wave")
    label = {1:"first-wave",2:"second-wave",3:"third-wave"}[wave]
    path = root / "planning" / f"wave-{wave}-slots.json"
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as e:
        raise ValueError(f"Cannot read the {label} slot plan") from e
    fixed = {"schema_version": 1, "wave": wave, "status": "private-technical-sequence",
             "baseline_commit": commit, "baseline_count": baseline}
    if (not isinstance(d, dict) or set(d) != fixed.keys() | {"slots", "target_count"}
        or any(type(d[k]) is not type(v) or d[k] != v for k,v in fixed.items())):
        raise ValueError(f"Invalid {label} slot plan header")
    slots = d["slots"]
    if (not isinstance(slots, list) or len(slots) != 21
        or type(d["target_count"]) is not int or d["target_count"] != baseline + len(slots)):
        raise ValueError(f"Expected exactly 21 bounded {label} slots")
    ceilings = dict(caps)
    counts = Counter()
    order = {}
    for n, slot in enumerate(slots, baseline + 1):
        if (not isinstance(slot, dict) or set(slot) != {"legacy_id", "code"}
            or type(slot["legacy_id"]) is not int or slot["legacy_id"] != n
            or not isinstance(slot["code"], str)
            or not re.fullmatch(r"[A-Z]{2,3}-[0-9]{2}", slot["code"])):
            raise ValueError(f"Invalid {label} slot {n}")
        code = slot["code"]
        area, seq = code.split("-")
        if area not in ceilings or area == "FIN" or int(seq) != ceilings[area] + 1:
            raise ValueError(f"Unexpected {label} area sequence: {code}")
        order[n] = code
        ceilings[area] += 1
        counts[area] += 1
    if order[baseline + 1] != eco or any(counts[k] != (0 if k == "FIN" else 1 if k == "ECO" else 2) for k in ceilings):
        raise ValueError(f"{label} must start with {eco} and preserve its approved area balance")
    if wave in (2, 3) and tuple(code.split("-")[0] for code in tuple(order.values())[1:]) != MIXED_ORDER * 2:
        raise ValueError(f"Unexpected {label} slot order")
    return order, ceilings

def load_release(root, number):
    """Validate all plans; use historical caps until the proposed slot crosses a boundary."""
    first, first_caps = load_wave(root)
    second, second_caps = load_wave(root, 2, first_caps)
    third, third_caps = load_wave(root, 3, second_caps)
    if number <= BASELINE:
        return {}, BASELINE_CAPS, BASELINE, max(third)
    if number <= SECOND_BASELINE:
        return first, first_caps, max(first), max(third)
    if number <= THIRD_BASELINE:
        return second, second_caps, max(second), max(third)
    return third, third_caps, max(third), max(third)

def historical_slot(number):
    """Keep the pre-wave approved mappings for existing builder fixtures."""
    if 491 <= number <= BASELINE:
        return "FIN-" + str(number - 445)
    if 481 <= number <= 490:
        return ("FIN" if number % 2 else "ECO") + "-" + str(41 + (number-481)//2)
    return None
