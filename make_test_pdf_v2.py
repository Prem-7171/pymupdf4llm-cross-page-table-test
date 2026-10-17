import csv
from fpdf import FPDF
from fpdf.enums import TableHeadingsDisplay

HEADER = ["ID", "Name", "Dept", "Score"]
DEPTS = ["Eng", "Ops", "Sales", "HR", "Legal"]
rows = [[f"R{i:03d}", f"Person {chr(65 + i % 26)}{i}", DEPTS[i % 5], str(100 + i * 7)]
        for i in range(1, 61)]  # 60 rows, all values unique/traceable

with open("ground_truth.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(HEADER); w.writerows(rows)

class Doc(FPDF):
    def header(self):
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 6, "Staff Score Report - Internal", new_x="LMARGIN", new_y="NEXT")
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 10)
            self.cell(0, 7, "Table 1 (continued)", new_x="LMARGIN", new_y="NEXT")
    def footer(self):
        self.set_y(-12); self.set_font("Helvetica", size=9)
        self.cell(0, 6, f"Page {self.page_no()} of {{nb}}", align="C")

def build(path, repeat):
    pdf = Doc(); pdf.alias_nb_pages(); pdf.set_auto_page_break(True, 15)
    pdf.add_page(); pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 8, "Table 1: Staff scores", new_x="LMARGIN", new_y="NEXT")
    with pdf.table(first_row_as_headings=True, repeat_headings=repeat,
                   col_widths=(20, 50, 30, 20)) as t:
        r = t.row()
        for h in HEADER: r.cell(h)
        for row in rows:
            r = t.row()
            for c in row: r.cell(c)
    pdf.output(path)

build("caseA_header_repeated.pdf", TableHeadingsDisplay.ON_TOP_OF_EVERY_PAGE)
build("caseB_header_first_page_only.pdf", TableHeadingsDisplay.NONE)