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

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # get filename and extract invoice number and date
    filename = Path(file).stem
    invoice_nbr, date = filename.split("-")

    # set text format
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nbr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    # read the data from excel file into a data frame
    df = pd.read_excel(file, sheet_name="Sheet 1")

    # add a header
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=68, h=8, txt=columns[1], border=1)
    pdf.cell(w=32, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=68, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=32, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=68, h=8, txt="", border=1)
    pdf.cell(w=32, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum text
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"The total price is {total_sum}", ln=1)

    # flush output
    pdf.output(f"output_pdfs/{filename}.pdf")

