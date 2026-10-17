import csv, sys

def cells(line):
    return [c.strip().replace("**", "") for c in line.strip().strip("|").split("|")]

def parse_tables(md):
    blocks, cur = [], []
    for line in md.splitlines():
        if line.strip().startswith("|"):
            cur.append(line)
        else:
            if cur: blocks.append(cur); cur = []
    if cur: blocks.append(cur)
    out = []
    for b in blocks:
        header = cells(b[0])
        sep_ok = len(b) > 1 and set(b[1].replace("|", "").strip()) <= set("-: ")
        data = [cells(l) for l in b[2:]] if sep_ok else [cells(l) for l in b[1:]]
        out.append({"header": header, "data": data})
    return out

def main(md_path, csv_path="Docs/ground_truth.csv"):
    truth = list(csv.reader(open(csv_path, encoding="utf-8")))
    truth_header, truth_rows = truth[0], truth[1:]
    md = open(md_path, encoding="utf-8").read()
    tables = parse_tables(md)
    print(f"== {md_path} ==")
    print("Table blocks found:", len(tables))
    all_data, promoted = [], []
    for i, t in enumerate(tables, 1):
        ok = t["header"] == truth_header
        print(f" Block {i}: header={t['header']} | proper column header: {ok} | data rows: {len(t['data'])}")
        all_data += t["data"]
        if not ok: promoted.append(t["header"])
    print("Data rows in DATA position:", len(all_data), "of", len(truth_rows), "expected")
    print("Rows sitting in HEADER position:", promoted)
    everything = []
    for t in tables:
        if t["header"] != truth_header: everything.append(t["header"])
        everything += t["data"]
    ids = [r[0] for r in everything]
    print("Missing IDs:", [r[0] for r in truth_rows if r not in everything])
    print("Duplicate IDs:", sorted({x for x in ids if ids.count(x) > 1}))
    print("Order correct:", ids == [r[0] for r in truth_rows])
    for rid in ["R001", "R032", "R033", "R060"]:
        exp = next(r for r in truth_rows if r[0] == rid)
        print(f" {rid} exact match anywhere: {exp in everything} | in data position: {exp in all_data}")
    print("Repeated header leaked as data row:", any(r[0] == "ID" for r in all_data))
    print("Non-table lines:", [l for l in md.splitlines() if l.strip() and not l.strip().startswith("|")])

main(*sys.argv[1:])