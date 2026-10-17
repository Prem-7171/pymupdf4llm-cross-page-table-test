import hashlib, pymupdf4llm

N = 5
for pdf in ["caseA_header_repeated.pdf", "caseB_header_first_page_only.pdf"]:
    hashes, promoted = [], []
    for run in range(1, N + 1):
        md = pymupdf4llm.to_markdown(pdf)
        open(f"{pdf[:5]}_run{run}.md", "w", encoding="utf-8").write(md)
        hashes.append(hashlib.sha256(md.encode()).hexdigest()[:10])
        lines = md.splitlines()
        idx = next(i for i, l in enumerate(lines) if "continued" in l)
        first_pipe = next(l for l in lines[idx:] if l.startswith("|"))
        promoted.append("R033" in first_pipe)
    print(pdf)
    print("  output hashes:", hashes, "-> identical across runs:", len(set(hashes)) == 1)
    print("  R033 in header position:", promoted, f"({sum(promoted)}/{N})")