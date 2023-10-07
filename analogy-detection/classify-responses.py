import csv
import os

RESPONSE_FILE = "responses.csv"
CLASS_FILE = "classed-responses.csv"

def read_csv_to_dict(file_path=RESPONSE_FILE):
    data_dict = {}

    # Open the CSV file in read mode
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            key = row[0]
            values = [value.strip() for value in row[1].split('$$$')]

            data_dict[key] = values
        
    return data_dict


def classify(data_dict):
    classifications = data_dict.copy()
    for key in classifications.keys():
        classifications[key] = 'N'
    for key in data_dict.keys():
        
        for response in data_dict[key]:
            if "Yes" in response:
                classifications[key] = 'Y'

            
            # # Split the string into sentences
            # sentences = response.split('. ')
            # # Get the last sentence
            # final_sentence = sentences[-1]
            
            # account for error
            # what about "while the article mentions EPI, the primary topic is ____"
            # if "No" not in final_sentence and "not" not in final_sentence and "no" not in final_sentence:
            #     print(key, ": ", final_sentence)
            #     classifications[key] = 'Y'
            # for sentence in sentences:
            #     if "Yes" in sentence:
            #         classifications[key] = 'N'
    return classifications

def save_classes_to_csv(dictionary, file_path=CLASS_FILE):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row if the file is newly created
        if not file_exists:
            writer.writerow(['Key', 'Value'])

        # Write each key-value pair as a row in the CSV file
        for key, value in dictionary.items():
            writer.writerow([key, value])

def main():
    print("classifying results...")
    responses = read_csv_to_dict()
    classifications = classify(responses)
    save_classes_to_csv(classifications)

    
main()