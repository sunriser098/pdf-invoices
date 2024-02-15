import pandas as pd
import glob
import os
from fpdf import FPDF
from pathlib import Path

# use glob to read all .xlsx files
# path = os.getcwd()
# path = path + "\\invoices"
# excel_files = glob.glob(os.path.join(path, "*.xlsx"))

excel_files = glob.glob("invoices/*.xlsx")
print(excel_files)

# loop over .xlsx files for data
for file in excel_files:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(file).stem
    invoice_nbr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nbr}")
    pdf.output(f"output_pdfs/{filename}.pdf")

