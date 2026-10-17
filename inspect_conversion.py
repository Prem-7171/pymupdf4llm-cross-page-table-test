import inspect
import pymupdf4llm
import pymupdf

pdf_path = "Docs/caseB_header_first_page_only.pdf"

print("PyMuPDF4LLM version:", pymupdf4llm.__version__)
print("\nConversion function signature:")
print(inspect.signature(pymupdf4llm.to_markdown))

with pymupdf.open(pdf_path) as doc:
    table = doc[1].find_tables().tables[0]
    rows = table.extract()

    print("\nRaw table extraction:")
    print("Row count:", len(rows))
    print("First row:", rows[0])
    print("Second row:", rows[1])

markdown = pymupdf4llm.to_markdown(pdf_path)

print("\nMarkdown output around the page-2 table:")
lines = markdown.splitlines()

for i, line in enumerate(lines):
    if "R033" in line:
        print("\n".join(lines[max(0, i - 3):i + 5]))
        break