import pandas as pd

# Read file Excel and some options
excel_file = 'Trim video\Sơn (1).xlsx'
df = pd.read_excel(excel_file, usecols=[0], skiprows=4, header= None)
# usecols=lambda column: column != n mmeans ignoring the nth column
# header = none means don't ignore the first row
# skiprows = [n] means skipping nth row
# write values to the file txt

txt_file = 'Trim video\\alphabet.txt'
with open(txt_file, 'w') as file:
    for row in df.itertuples(index=False):
        for value in row:
            file.write(str(value) + '\n')

print("Recorded value from Excel file to text file")
