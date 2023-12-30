import csv
import re
import pandas as pd

GPT_RESPONSES = "../analogy-detection/query-response-data.xlsx"
POSITIVE_RESPONSES = "positive-responses.csv"



def excel_to_dict(file_path=GPT_RESPONSES, sheet_name="Data", identifier_column_index=1, data_column_index=2):
    """
    Read Excel data into a dictionary.

    Parameters:
    - file_path (str): Path to the Excel file.
    - sheet_name (str): Name of the Excel sheet.
    - identifier_column_index (int): Index of the column containing string identifiers.
    - data_column_index (int): Index of the column containing text data.

    Returns:
    - data_dict (dict): Dictionary where keys are identifiers and values are lists of text data.
    """
    try:
        # Read Excel file into a DataFrame without header
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        
        # Create a dictionary to store the data
        data_dict = {}

        # Iterate over rows and populate the dictionary
        for index, row in df.iterrows():
            identifier = row[identifier_column_index]
            data = row[data_column_index]

            # If the identifier is not already a key in the dictionary, add it
            if identifier not in data_dict:
                data_dict[identifier] = []

            # Append the text data to the list for the corresponding identifier
            data_dict[identifier].append(data)
        
        return data_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        # Print the full exception traceback for more details
        import traceback
        traceback.print_exc()
        return None
    


def get_positive_responses(data_dict):
    positive_responses = []
    for key in data_dict.keys():
        for response in data_dict[key]:
            if "Yes" in response:
                positive_responses.append((key, response[response.find("Yes") + 4:]))
    return positive_responses

def save_positive_responses(positive_responses):

    with open(POSITIVE_RESPONSES, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["article", "response"])  # Write the header row
        for key, response in positive_responses:
            writer.writerow([key, response])
    print("Responses saved to " + POSITIVE_RESPONSES)



def main():
    data_dict = excel_to_dict()
    positive_responses = get_positive_responses(data_dict)
    save_positive_responses(positive_responses)




main()
