import pymupdf

for pdf in ["caseA_header_repeated.pdf", "caseB_header_first_page_only.pdf"]:
    with pymupdf.open(pdf) as doc:
        for pno in (0, 1):
            t = doc[pno].find_tables().tables[0]
            print(f"{pdf} page {pno+1}: rows={len(t.extract())}")
            print("   header.names   :", t.header.names)
            print("   header.external:", t.header.external)
            print("   markdown first 2 lines:", t.to_markdown().splitlines()[:2])