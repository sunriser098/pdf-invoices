import pandas as pd
import glob
import os

# use glob to read all .xlsx files
# path = os.getcwd()
# path = path + "\\invoices"
# excel_files = glob.glob(os.path.join(path, "*.xlsx"))

excel_files = glob.glob("invoices/*.xlsx")
print(excel_files)

# loop over .xlsx files for data
for file in excel_files:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    print(df)

