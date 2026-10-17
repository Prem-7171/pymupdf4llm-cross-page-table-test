# PyMuPDF4LLM: a table that continues across a page break

**AI Product Research assignment for AI Demos / FutureSmart AI**
Author: Prem Palkar | [LinkedIn](https://www.linkedin.com/in/prem-palkar-7a6b23297) | [GitHub](https://github.com/Prem-7171)

> These are my own controlled test cases, **not an official AI Demos benchmark run**, as agreed in the confirmation email.

## What this tests

- **Benchmark:** [Converting a complex PDF into clean Markdown with an open-source library](https://aidemos.com/benchmarks/pdf-to-markdown-open-source)
- **Scenario:** [A table that continues across a page break](https://aidemos.com/benchmarks/pdf-to-markdown-open-source/scenarios/a-table-that-continues-across-a-page-break)
- **Tool:** PyMuPDF4LLM 1.28.2 (PyMuPDF 1.28.2), default settings, run locally
- **Question:** When a table continues onto page 2, does the Markdown keep every row correct, in order, and attributable to the right columns?

## Test data

Two PDFs generated from the same 60 unique records (`ID, Name, Dept, Score`), with the break between **R032** (page 1) and **R033** (page 2). Both include a running header, a "Table 1 (continued)" label and a "Page N of 2" footer as noise.

| Case | Variable |
|---|---|
| **A** | Column header repeated at the top of page 2 |
| **B** | Column header on page 1 only |

`ground_truth.csv` is the answer key.

## Results (one machine, one library version, synthetic table)

| Case | Result |
|---|---|
| **A** | Passes: 60 of 60 rows in data position (32 + 28), correct headers and order |
| **B** | **R033 becomes the second table's header**; 59 of 60 rows in data position. No value lost, order correct |
| Repeatability | 5 runs per case, identical output each time (Case B failed 5 of 5) |

A diagnostic with PyMuPDF's table object shows `header.names` = `['R033', 'Person H33', 'HR', '331']` for Case B page 2, consistent with the Markdown. **The root cause inside the layout converter was not verified.**

## Files

| File | Purpose |
|---|---|
| `make_test_pdf_v2.py` | Generates the two PDFs and `ground_truth.csv` |
| `caseA_header_repeated.pdf`, `caseB_header_first_page_only.pdf` | Inputs |
| `ground_truth.csv` | Answer key (60 rows) |
| `case_A_test.py`, `case_B_test.py` | Convert each PDF with default settings |
| `Case_A_test_output.md`, `Case_B_test_output.md` | Raw, unedited Markdown outputs |
| `compare.py` | Compares an output `.md` against the ground truth |
| `repeat_runs.py` | Runs each conversion 5 times and compares hashes |
| `caseA_run1.md` ... `caseB_run5.md` | The 10 repeat-run outputs |
| `inspect_tables.py`, `inspect_header.py`, `inspect_conversion.py` | Investigation scripts |
| `commands.txt` | Every command used, in order |
| `requirements.txt` | Library versions |
| `[Report PDF name]` | Full written report |
| `[screenshots folder, if any]` | Screenshots used in the report |

## Reproduce

Tested on Windows with Python 3.13.

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python make_test_pdf_v2.py
python case_A_test.py
python case_B_test.py
python compare.py Case_A_test_output.md
python compare.py Case_B_test_output.md
python repeat_runs.py
```

Full command list: `commands.txt`.

## Limits

- One machine, one library version (1.28.2), one synthetic table made with fpdf2.
- Not tested: other PDF generators (Word, LaTeX, scans), other versions, other settings (`table_output`, `header`/`footer`, `edge_threshold`), tables over 2 pages.
- The first version of `compare.py` had a bug (a false order error on Case B), which I found, fixed and re-ran. All results use the fixed version.

## AI assistance

I used AI assistants (Claude and ChatGPT) for scripting help, explaining tool behavior and reviewing my draft. I designed the test cases, ran every experiment, checked the outputs myself, and I am responsible for the conclusions.

## Links

- Written report: [`[Report PDF name]`](./[Report%20PDF%20name].pdf)
