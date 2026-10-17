import pymupdf4llm as pdf

md_case_B = pdf.to_markdown("Docs/caseB_header_first_page_only.pdf")
# print(md)

with open("Outputs/Case_B_test_output.md", "w", encoding="utf-8") as file:
    file.write(md_case_B)
    
    print("Markdown file saved successfully as 'Case_B_test_output.md' !")