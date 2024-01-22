import pandas as pd

# Load the Excel file into a DataFrame
file_path = 'user-responses.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Filter rows where the 'USER-RESPONSE' column has the value 'Yes'
filtered_df = df[df['USER-RESPONSE'] == 'Yes']

# Create a new Excel file with a new sheet named 'Sheet2'
output_file_path = 'filtered-user-responses-positive.xlsx'  # Replace with the desired output file path
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    filtered_df.to_excel(writer, sheet_name='Sheet1', index=False)

print(f"Filtered data has been saved to '{output_file_path}' with 'Sheet1' as the sheet name.")
