import pymupdf4llm as pdf

md_case_A = pdf.to_markdown("Docs/caseA_header_repeated.pdf")
# print(md)

with open("Outputs/Case_A_test_output.md", "w", encoding="utf-8") as file:
    file.write(md_case_A)
    
    print("Markdown file saved successfully as 'Case_A_test_output.md' !")