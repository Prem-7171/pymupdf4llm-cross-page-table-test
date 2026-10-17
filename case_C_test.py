import pymupdf4llm as pdf

md_case_C = pdf.to_markdown("caseC_Plain_Doc.pdf")
# print(md)

with open("Case_C_test_output.md", "w", encoding="utf-8") as file:
    file.write(md_case_C)
    
    print("Markdown file saved successfully as 'Case_C_test_output.md' !")