import pymupdf

pdf_path = "Docs/caseB_header_first_page_only.pdf"

with pymupdf.open(pdf_path) as doc:
    print("Total pages:", len(doc))

    page = doc[1]  # Second page
    tables = page.find_tables()

    print("Tables detected on page 2:", len(tables.tables))

    for i, table in enumerate(tables.tables, start=1):
        extracted = table.extract()

        print(f"\nTable {i}")
        print("Rows detected:", len(extracted))
        print("First row:", extracted[0] if extracted else None)
        print("Last row:", extracted[-1] if extracted else None)