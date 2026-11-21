"""Load the reviewed first-wave slot sequence; no publication or reservations."""
import json
import re
from collections import Counter

BASELINE = 495
BASELINE_COMMIT = "c087eb9816db395317dafd9e104f0657726e59ab"
BASELINE_CAPS = {
    "ACC": 40, "FIN": 50, "MKT": 40, "OPS": 40, "PPL": 40, "STR": 40,
    "ENT": 40, "IS": 40, "GVR": 40, "SUS": 40, "ECO": 45, "HSP": 40,
}

def load_wave(root):
    """Read and validate a strictly bounded plan, then derive area ceilings."""
    path = root / "planning" / "wave-1-slots.json"
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as e:
        raise ValueError("Cannot read the first-wave slot plan") from e
    fixed = {"schema_version": 1, "wave": 1, "status": "private-technical-sequence",
             "baseline_commit": BASELINE_COMMIT, "baseline_count": BASELINE}
    if not isinstance(d, dict) or set(d) != fixed.keys() | {"slots", "target_count"} or any(d[k] != v for k,v in fixed.items()):
        raise ValueError("Invalid first-wave slot plan header")
    slots = d["slots"]
    if not isinstance(slots, list) or len(slots) != 21 or d["target_count"] != BASELINE + len(slots):
        raise ValueError("Expected exactly 21 bounded first-wave slots")
    ceilings = dict(BASELINE_CAPS)
    counts = Counter()
    order = {}
    for n, slot in enumerate(slots, BASELINE + 1):
        if (not isinstance(slot, dict) or set(slot) != {"legacy_id", "code"}
            or type(slot["legacy_id"]) is not int or slot["legacy_id"] != n
            or not isinstance(slot["code"], str)
            or not re.fullmatch(r"[A-Z]{2,3}-[0-9]{2}", slot["code"])):
            raise ValueError(f"Invalid first-wave slot {n}")
        code = slot["code"]
        area, seq = code.split("-")
        if area not in ceilings or area == "FIN" or int(seq) != ceilings[area] + 1:
            raise ValueError(f"Unexpected first-wave area sequence: {code}")
        order[n] = code
        ceilings[area] += 1
        counts[area] += 1
    if order[BASELINE + 1] != "ECO-46" or any(counts[k] != (0 if k == "FIN" else 1 if k == "ECO" else 2) for k in ceilings):
        raise ValueError("First wave must start with ECO-46 and preserve its approved area balance")
    return order, ceilings

def historical_slot(number):
    """Keep the pre-wave approved mappings for existing builder fixtures."""
    if 491 <= number <= BASELINE:
        return "FIN-" + str(number - 445)
    if 481 <= number <= 490:
        return ("FIN" if number % 2 else "ECO") + "-" + str(41 + (number-481)//2)
    return None
