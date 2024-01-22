import os
import openpyxl

# Function to get a list of file names in a folder
def get_file_names(folder_path):
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return file_names

# Function to write file names to an Excel file
def write_to_excel(file_names, excel_file_path):
    wb = openpyxl.Workbook()
    ws = wb.active

    # Writing file names to the first column of the Excel sheet
    for i, file_name in enumerate(file_names, start=1):
        ws.cell(row=i, column=1, value=file_name)

    # Save the Excel file
    wb.save(excel_file_path)
    print(f"File names written to {excel_file_path} successfully.")

# Specify the folder path and Excel file path
folder_path = "split-texts"
excel_file_path = "news-articles-data.xlsx"

# Get file names from the specified folder
file_names = get_file_names(folder_path)

# Write file names to the Excel file
write_to_excel(file_names, excel_file_path)
