#!/usr/bin/env python3
"""Build one reviewed expansion case. Default is a read-only dry run.
Usage: python scripts/build_case.py reviewed-case.json [--repo PATH] [--write]
Requires lxml. Does not create art, commit, push or certify visual/source review.
"""
import argparse, copy, html, importlib.util, json, re, sys
from pathlib import Path
from lxml import html as LH

# A dry run must not create imported helper bytecode in the repository.
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]

def require(ok, message):
    if not ok: raise ValueError(message)

def module(path, name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj

def markdown(fragment):
    """Preserve prose, lists and real tables rather than flattening cell text."""
    root=LH.fragment_fromstring(fragment,create_parent="div")
    def inner(n):
        return (n.text or "")+"".join(render(c)+(c.tail or "") for c in n)
    def render(n):
        tag=n.tag.lower() if isinstance(n.tag,str) else ""
        text=inner(n)
        if tag=="table":
            rows=[]
            for row in n.xpath(".//tr"):
                rows.append([inner(cell).strip().replace("|","\\|").replace("\n"," ") for cell in row if cell.tag in ("td","th")])
            if not rows:return ""
            width=max(map(len,rows)); rows=[row+[""]*(width-len(row)) for row in rows]
            lines=["| "+" | ".join(row)+" |" for row in rows]
            lines.insert(1,"| "+" | ".join(["---"]*width)+" |")
            return "\n\n"+"\n".join(lines)+"\n\n"
        if tag in ("strong","b"):return "**"+text+"**"
        if tag in ("em","i"):return "*"+text+"*"
        if tag=="br":return "\n"
        if tag=="li":return "- "+text+"\n"
        if tag in ("p","div","ul","ol","section"):return text+"\n\n"
        return text
    return re.sub(r"\n{3,}","\n\n",inner(root)).strip()

def duration_minutes(value):
    """Use the displayed duration's upper bound for the available-time filter."""
    match = re.fullmatch(r"\s*(\d+)(?:\s*[-–—]\s*(\d+))?\s+minutes?\s*", value, re.I) if isinstance(value, str) else None
    require(match is not None, "Duration must be a positive minute count or range, e.g. 15–20 minutes")
    lower = int(match[1]); upper = int(match[2] or match[1])
    require(0 < lower <= upper, "Duration must have positive, ascending minute bounds")
    return upper

def validate_payload(x):
    """Reject malformed metadata and active/external main-body content early."""
    required={"number","code","slug","title","discipline","topics","teaser","alt","news_heading","news","opening","q1","q2","round2","exhibit","exhibit_md","sections","notes","sources","slides"}
    require(isinstance(x,dict), "Input must be a JSON object")
    require(required <= x.keys(), "Missing required JSON fields: "+str(required-x.keys()))
    for key in required-{"number","topics","sections","sources","slides"}:
        require(isinstance(x[key],str) and x[key].strip(), "Expected nonempty string: "+key)
    for key in ("title","discipline","teaser","alt","news_heading","notes","location","duration"):
        if key in x:
            require(isinstance(x[key],str) and x[key].strip() and not re.search(r"[<>]|https?://",x[key],re.I), "Expected plain text: "+key)
    duration_minutes(x.get("duration", "10–15 minutes"))
    require(type(x["number"]) is int, "Number must be an integer")
    require(isinstance(x["topics"],list) and x["topics"] and all(isinstance(t,str) and t.strip() and not re.search(r"[<>|]|https?://",t,re.I) for t in x["topics"]), "Topics must be nonempty plain-text strings")
    require(len(set(x["topics"]))==len(x["topics"]), "Duplicate topics")
    for key,width in (("sections",2),("slides",2),("sources",3)):
        require(isinstance(x[key],list) and x[key] and all(isinstance(row,list) and len(row)==width and all(isinstance(v,str) and v.strip() for v in row) for row in x[key]), "Malformed "+key)
    require(sum(heading == "Instructor note" for heading, _ in x["sections"]) == 1, "Exactly one dedicated Instructor note section required")
    for heading,_ in x["sections"]+x["slides"]:
        require(not re.search(r"[<>]|https?://",heading,re.I), "Headings must be plain text")
    allowed={"p","strong","b","em","i","br","ul","ol","li","table","thead","tbody","tfoot","tr","th","td","caption"}
    fragments=[x[k] for k in ("news","opening","exhibit","round2")]+[b for _,b in x["sections"]+x["slides"]]
    for fragment in fragments:
        require(not re.search(r"https?://",fragment,re.I), "Body URLs prohibited")
        tree=LH.fragment_fromstring(fragment,create_parent="div")
        for node in tree.iterdescendants():
            require(isinstance(node.tag,str) and node.tag.lower() in allowed, "Unsupported body HTML tag")
            require(not node.attrib, "Body HTML attributes prohibited; builder owns presentation")
    require(not re.search(r"https?://|<|\]\s*\(",x["exhibit_md"],re.I), "Markdown exhibit must be self-contained, with no links or HTML")


def write_outputs(outputs, originals, baseline, verify):
    """Optimistic concurrency check and best-effort rollback on caught failures.

    Not a crash-safe transaction or lock: use a single writer per checkout.
    """
    for p,original in {**baseline,**originals}.items():
        require((p.read_bytes() if p.exists() else None)==original, "Concurrent modification: "+str(p))
    written=[]
    try:
        for p,text in outputs.items():
            written.append(p)
            p.write_text(text,encoding="utf-8")
        verify()
    except BaseException:
        for p in reversed(written):
            if originals[p] is None:p.unlink(missing_ok=True)
            else:p.write_bytes(originals[p])
        raise


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path",type=Path)
    parser.add_argument("--repo",type=Path,default=ROOT)
    parser.add_argument("--write",action="store_true")
    parser.add_argument("--dry-run",action="store_true",help="Explicit read-only mode (the default)")
    args=parser.parse_args(argv)
    require(not(args.write and args.dry_run),"Choose --write OR --dry-run")
    r=args.repo.resolve();x=json.loads(args.json_path.read_text(encoding="utf-8"));esc=html.escape
    validate_payload(x)
    baseline={p:p.read_bytes() for p in r.rglob("*") if p.is_file() and p.suffix in (".html", ".md", ".json", ".py") and ".git" not in p.parts}
    reg=json.loads(baseline[r/"case-registry.json"]); oldreg=copy.deepcopy(reg)
    registry_checks=module(r/"tests/check_registry.py","builder_registry")
    try:registry_checks.validate_registry(reg)
    except (AssertionError,KeyError) as error:raise ValueError("Invalid existing registry: "+str(error)) from error
    slug=x["slug"]; number=x["number"]; code=x["code"]
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",slug),"Unsafe slug")
    release=module(r/"scripts/release_slots.py","builder_release_slots")
    wave, caps, stage_limit, limit=release.load_release(r,number)
    require(isinstance(number,int) and 121<=number<=limit,f"Expansion builder supports IDs 121–{limit}")
    require(number==max(c["legacy_id"] for c in reg["cases"])+1,"ID must follow existing registry")
    require(not any(c["slug"]==slug or c["legacy_id"]==number or c["code"]==code for c in reg["cases"]),"Existing slug, ID or code: refusing overwrite")
    for p in [r/(slug+".html"),r/"authoring"/(slug+".md")]:require(not p.exists(),"Existing output: "+str(p))
    area=next((a for a in reg["areas"] if a["name"]==x["discipline"]),None)
    require(area is not None,"Unknown primary discipline")
    peers=[c for c in reg["cases"] if c["area"]==x["discipline"]]
    require(code==area["code"]+"-"+str(len(peers)+1).zfill(2) and len(peers)<caps[area["code"]],"Wrong next area code")
    expected=wave.get(number) or release.historical_slot(number)
    if expected is not None:
        require(code==expected,"Wrong approved expansion slot")
    require(len(x["sources"])>=5 and len({s[0] for s in x["sources"]})==len(x["sources"]),"Need >=5 distinct source URLs")
    require(all(len(s)==3 and s[0].startswith("https://") for s in x["sources"]),"Malformed source")
    require(all(isinstance(t,str) and t for t in x["topics"]),"Empty topic")
    fragments=[x[k] for k in ("news","opening","exhibit","round2")]+[b for h,b in x["sections"]]+[b for h,b in x["slides"]]
    require(not any(re.search(r"<script|on[a-z]+\s*=|https?://",b,re.I) for b in fragments),"Scripts, inline handlers or body URLs prohibited")
    for q in (x["q1"],x["q2"]):
        require(q and "<" not in q and "http" not in q,"Questions must be plain self-contained text")
        require(sum(b.count("<p>"+q+"</p>") for h,b in x["slides"])==1,"Each decision must appear exactly once as a standalone slide paragraph")
    require(x["q1"] != x["q2"],"Opening and second decisions must differ")
    positions=[next(i for i,(_,b) in enumerate(x["slides"]) if "<p>"+q+"</p>" in b) for q in (x["q1"],x["q2"])]
    require(positions[0] < positions[1],"Opening decision must precede second decision")
    if args.write:require((r/(slug+"-scene.jpg")).is_file(),"Reviewed illustration must exist before writing")
    template=next(c for c in reg["cases"] if c["slug"]=="tarts")
    oldcode=template["code"];base=(r/"tarts.html").read_text(encoding="utf-8")
    require(base.count("<main>")==1 and base.count("<dialog")==1,"Unexpected template structure")
    prefix=base.split("<main>",1)[0]
    prefix,n=re.subn(r"<title>.*?</title>","<title>"+esc(code+" · "+x["title"])+" · Micro Cases</title>",prefix)
    require(n==1,"Template title missing")
    prefix,n=re.subn(r"(<strong>MICRO CASE · )"+re.escape(oldcode)+r"(</strong>)",lambda m:m[1]+code+m[2],prefix)
    require(n==1,"Template header code missing")
    location=x.get("location","Hong Kong");duration=x.get("duration","10–15 minutes");minutes=duration_minutes(duration)
    meta=code+" · "+location+" · "+duration+" · "+" · ".join(x["topics"])
    img='<img class="scene" src="'+slug+'-scene.jpg" alt="'+esc(x["alt"],quote=True)+'">'
    def prompt(q):return '<div class="student-prompt"><strong>Your decision</strong><p>'+esc(q)+'</p></div>'
    refs='<div class="references"><p class="source-note">All information needed for classroom decisions is provided above. Sources are optional reading for attribution and background.</p><p>'+esc(x["notes"])+'</p><ol>'+''.join('<li><a href="'+esc(u,quote=True)+'">'+esc(t)+'</a>. '+esc(s)+'</li>' for u,t,s in x["sources"])+'</ol></div>'
    body='<main><div class="meta" data-case-id="'+str(number)+'" data-case-code="'+code+'"><span class="case-code">'+code+'</span>'+esc(meta[len(code):])+'</div><h1>'+esc(x["title"])+'</h1>'+img
    body+='<section class="news-context"><h2>'+esc(x["news_heading"])+'</h2>'+x["news"]+'</section><h2>Your classroom decision</h2>'+x["opening"]+x["exhibit"]+prompt(x["q1"])
    body+='<details><summary>Round 2 · More information</summary>'+x["round2"]+prompt(x["q2"])+'</details>'
    for heading,fragment in x["sections"]:body+='<details><summary>'+esc(heading)+'</summary>'+fragment+'</details>'
    body+='<footer><details><summary>Sources and case assumptions · optional reference</summary>'+refs+'</details></footer><section class="printonly"><div class="space"></div><h2>Round two</h2>'+x["round2"]+prompt(x["q2"])+'<div class="space"></div></section><div class="printonly" id="printed-sources"></div></main>'
    suffix="<dialog"+base.split("<dialog",1)[1]
    slides=copy.deepcopy(x["slides"]); require(len(slides)>=3,"Too few slides")
    slides[1][1]=img+slides[1][1]
    for slide in slides:
        for q in (x["q1"],x["q2"]):slide[1]=slide[1].replace("<p>"+q+"</p>",prompt(q))
    serialized=json.dumps(slides,ensure_ascii=False).replace("</","<\\/")
    suffix,n=re.subn(r"const rounds=.*?;let step=0;",lambda m:"const rounds="+serialized+";let step=0;",suffix,flags=re.S)
    require(n==1,"Presentation data marker missing")
    suffix,n=re.subn(r'aria-label="'+re.escape(oldcode)+r' classroom presentation"', 'aria-label="'+code+' classroom presentation"',suffix); require(n==1,"Presentation aria marker missing")
    suffix,n=re.subn(r"('#counter'\)\.textContent=')"+re.escape(oldcode),lambda m:m[1]+code,suffix)
    # Counter pattern may include document.querySelector prefix, but must replace exactly once.
    require(n==1,"Presentation counter marker missing")
    page=prefix+body+'<nav class="case-navigation" aria-label="More cases in this teaching area"></nav>'+suffix
    md="# "+x["title"]+"\n\n<!-- legacy-case-id: "+str(number)+" -->\n\n"+meta+"\n\n!["+x["alt"]+"](../"+slug+"-scene.jpg)\n\n"
    for heading,fragment in [(x["news_heading"],x["news"]),("Opening decision",x["opening"])]:md+="## "+heading+"\n\n"+markdown(fragment)+"\n\n"
    md+="## Evidence\n\n"+x["exhibit_md"]+"\n\n**Student question:** "+x["q1"]+"\n\n## Round two\n\n"+markdown(x["round2"])+"\n\n**Student question:** "+x["q2"]+"\n\n"
    for h,b in x["sections"]:md+="## "+h+"\n\n"+markdown(b)+"\n\n"
    md+="## Sources and case assumptions · optional reference\n\nAll information needed for classroom decisions is provided above. Sources are optional reading.\n\n"+x["notes"]+"\n\n"
    md+="".join("- ["+t+"]("+u+"). "+s+"\n" for u,t,s in x["sources"])
    reg["cases"].append(dict(legacy_id=number,code=code,slug=slug,area=x["discipline"],title=x["title"]))
    try:registry_checks.validate_registry(reg)
    except (AssertionError,KeyError) as error:raise ValueError("Invalid proposed registry: "+str(error)) from error
    outputs={r/(slug+".html"):page,r/"authoring"/(slug+".md"):md,r/"case-registry.json":json.dumps(reg,ensure_ascii=False,indent=2)+"\n"}
    s=(r/"index.html").read_text(encoding="utf-8");cards=re.findall(r'<a class="card".*?</a>',s,re.S)
    require(len(cards)==len(oldreg["cases"]),"Existing card count differs from registry")
    lookup={re.search(r'href="([^"]+)"',c)[1]:c for c in cards}
    require(len(lookup)==len(cards) and set(lookup)=={c["slug"]+".html" for c in oldreg["cases"]},"Card identities mismatch")
    lookup[slug+".html"]='<a class="card" href="'+slug+'.html" data-case-id="'+str(number)+'" data-case-code="'+code+'" data-discipline="'+esc(x["discipline"],quote=True)+'" data-concepts="'+esc("|".join(x["topics"]),quote=True)+'" data-minutes="'+str(minutes)+'"><img width="760" height="389" loading="lazy" alt="" src="'+slug+'-scene.jpg"><div><span class="tag"><span class="case-code">'+code+'</span><span class="duration">'+esc(duration)+'</span></span><h3>'+esc(x["title"])+'</h3><p>'+esc(x["teaser"])+'</p><span class="discipline">'+esc(x["discipline"])+'</span><small>'+esc(" · ".join(x["topics"]))+'</small></div></a>'
    order={a["name"]:i for i,a in enumerate(reg["areas"])}
    start=s.index(cards[0]);end=s.index(cards[-1])+len(cards[-1])
    require(not re.sub(r'<a class="card".*?</a>',"",s[start:end],flags=re.S).strip(),"Unexpected content among cards")
    s=s[:start]+''.join(lookup[c["slug"]+".html"] for c in sorted(reg["cases"],key=lambda c:(order[c["area"]],int(c["code"].split("-")[1]))))+s[end:]
    start=s.index('<select id="concept">');end=s.index("</select>",start)
    for topic in x["topics"]:
        if "<option>"+esc(topic)+"</option>" not in s[start:end]:
            s=s[:end]+"<option>"+esc(topic)+"</option>"+s[end:];end=s.index("</select>",start)
    counts=module(r/"scripts/sync_collection.py","exp_counts")
    nav=module(r/"scripts/sync_case_navigation.py","exp_nav")
    outputs[r/"index.html"]=counts.render(s,reg)
    outputs[r/"README.md"]=(r/"README.md").read_text(encoding="utf-8")+"\n## "+code+"\n\n"+str(number)+". ["+x["title"]+"]("+slug+".html)\n"
    outputs[r/"docs/case-numbering.md"]=(r/"docs/case-numbering.md").read_text(encoding="utf-8").rstrip()+"\n| "+str(number)+" | "+code+" | ["+slug+".html](../"+slug+".html) | "+x["title"]+" |\n"
    if number>release.BASELINE:
        readme=r/"README.md"
        numbering=r/"docs/case-numbering.md"
        snapshot=(f"The collection contains {number} cases. The third balanced wave started at 537 cases: 50 in Finance, 47 in Economics and 44 in each of the other ten areas."
                  if number>release.THIRD_BASELINE else
                  f"The collection contains {number} cases. The second balanced wave started at 516 cases: 50 in Finance, 46 in Economics and 42 in each of the other ten areas."
                  if number>release.SECOND_BASELINE else
                  f"The collection contains {number} cases. The balanced wave started at 495 cases: 50 in Finance, 45 in Economics and 40 in each of the other ten areas.")
        outputs[readme], n=re.subn(r"The collection contains \d+ cases[.:][^\n]*?ten areas\.",snapshot,outputs[readme],count=1)
        require(n==1,"README collection snapshot marker missing")
        outputs[readme], n=re.subn(r"Identity fixtures protect [^\n]+",
                                  f"Identity fixtures protect all 537 baseline permanent IDs, area codes and URLs. Earlier snapshots remain unchanged. The builder supports the first three balanced waves, through ID {limit}.",outputs[readme],count=1)
        require(n==1,"README identity note marker missing")
        outputs[numbering], n=re.subn(r"Five further Finance cases (?:bring|brought) the collection to 495, with 50 in FIN, 45 in ECO and 40 in every other area\.",
                                     "Five further Finance cases brought the pre-wave collection to 495, with 50 in FIN, 45 in ECO and 40 in every other area.",outputs[numbering],count=1)
        require(n==1 or "brought the pre-wave collection to 495" in outputs[numbering],"Numbering baseline marker missing")
    ledger=(r/"planning/collection-roadmap.md").read_text(encoding="utf-8")
    ledger,n=re.subn(r"^\d+ cases are published:.*$",str(len(reg["cases"]))+" cases are published: the original 120 plus "+str(len(reg["cases"])-120)+" approved expansion cases. The 2024 award acknowledgement remains limited to Cases 1–8.",ledger,count=1,flags=re.M);require(n==1,"Coverage total marker missing")
    for a in reg["areas"]:
        members=sorted(c["legacy_id"] for c in reg["cases"] if c["area"]==a["name"])
        pat=r"^\| "+re.escape(a["name"])+r" \|[^\n]*"
        def row(m):
            cells=m[0].split("|");require(len(cells)==7,"Unexpected coverage table row")
            cells[2]=" "+", ".join(map(str,members))+" ";cells[4]=" "+str(caps[a["code"]]-len(members))+" "
            if number>release.BASELINE:
                planned=[c for n,c in wave.items() if c.split("-")[0]==a["code"] and (number<=release.SECOND_BASELINE or n>number)]
                cells[3]=" "+(", ".join(planned) if planned else "None remaining in this wave")+" "
            return "|".join(cells)
        ledger,n=re.subn(pat,row,ledger,count=1,flags=re.M);require(n==1,"Missing coverage area "+a["name"])
    total=len(reg["cases"]);remaining=stage_limit-total
    ledger,n=re.subn(r"^\| \*\*Total\*\* \|.*$",f"| **Total** | **{total} published** | **{remaining} approved editorial slots** | **{remaining}** | |",ledger,count=1,flags=re.M);require(n==1,"Coverage total row missing")
    if number>release.BASELINE:
        ordinal="third" if number>release.THIRD_BASELINE else "second" if number>release.SECOND_BASELINE else "first"
        ledger,n=re.subn(r"(?m)^# Micro Cases in Business · Coverage and (?:targeted expansion|(?:first|second|third) balanced wave) to \d+$",
                         f"# Micro Cases in Business · Coverage and {ordinal} balanced wave to {stage_limit}",ledger,count=1)
        require(n==1,"Coverage heading marker missing")
    outputs[r/"planning/collection-roadmap.md"]=ledger
    # Only navigation may change in existing case pages. No teaching-content re-render.
    for case in reg["cases"]:
        path=r/(case["slug"]+".html");source=outputs.get(path,path.read_text(encoding="utf-8") if path.exists() else "")
        revised=nav.render(source,reg,case)
        if case["slug"]!=slug:
            require(nav.PATTERN.sub("",source)==nav.PATTERN.sub("",revised),"Existing content changed")
        if revised!=source or path in outputs:outputs[path]=revised
    originals={p:baseline.get(p) for p in outputs}
    print("Validated",code,";",len(outputs),"planned files; existing cases navigation only.")
    for path in outputs:print(path.relative_to(r))
    if not args.write:
        print("DRY RUN: no files changed. Artwork existence required for --write.")
        return
    def verify():
        counts.check(r)
        nav.sync(r,check=True)
    write_outputs(outputs, originals, baseline, verify)
    print("Written locally; review diff, run tests and visual/print QA before publication.")
if __name__=="__main__":main()

