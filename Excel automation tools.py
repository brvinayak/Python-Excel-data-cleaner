import pandas as pd
import os

file_name=input("Enter excel file name(with extension):")

if not os.path.exists(file_name):
    print("File not found.")
    exit()

df = pd.read_excel(file_name)
print(df.head())
print("Original rows: ",df.shape[0])
print("No of columns",df.shape[1])
original_rows=df.shape[0]

permission=input("Proceed with cleaning? (yes/no)")
if permission.lower() != "yes":
    print("Cleaning cancelled.")
    exit()

df=df.dropna()
df=df.drop_duplicates()

output_file=input("Enter output file name: ")

if not output_file.endswith(".xlsx"):
    output_file += ".xlsx"

df.to_excel(output_file,index = False)
columns=df.columns

for column in columns:
    print(column)

print("No of rows after cleaning: ",df.shape[0])
print("No of columns",df.shape[1])
print("Removed rows: ",original_rows-df.shape[0])

print(f"Cleaned file saved successfully as: {output_file}")