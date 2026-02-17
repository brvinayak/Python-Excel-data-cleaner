# Python Excel Data Cleaner

A Python automation tool that cleans Excel files automatically by removing empty rows and duplicate entries, then saves a new cleaned file.

---

## Features
- Loads Excel files dynamically
- Shows preview of data
- Displays row and column counts
- Removes empty rows
- Removes duplicate rows
- Confirmation prompt before cleaning
- Saves cleaned file with custom name
- Generates cleaning report summary

---

## How It Works
The script reads an Excel file, analyzes its contents, cleans the data, and exports a new cleaned file without modifying the original.

---

## Example Workflow

Input file:
messy_data.xlsx

Output file:
cleaned_data.xlsx

Report:
Original rows: 200
Rows after cleaning: 178
Removed rows: 22

---

## Installation

Install dependencies:

pip install pandas openpyxl

---

## Usage

Run script:

python excel_cleaner.py

Enter:
- file name
- confirmation
- output file name

---

## Technologies Used
- Python
- Pandas
- OpenPyXL

---

## Use Cases
- Cleaning datasets before analysis
- Preparing ML training data
- Removing duplicate records
- Fixing messy spreadsheets

---

## Author
Vinayak R B
