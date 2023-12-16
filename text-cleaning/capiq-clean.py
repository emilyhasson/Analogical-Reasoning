import os
import re

def clean_text_files(input_folder, output_folder):
    # Ensure the folder paths end with a slash
    input_folder = input_folder.rstrip("/") + "/"
    output_folder = output_folder.rstrip("/") + "/"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # Assuming text files have a .txt extension
            input_file_path = input_folder + filename
            output_file_path = output_folder + filename

            # Read the content of the input file
            with open(input_file_path, 'r') as input_file:
                content = input_file.read()

            # Use regular expression to find the position of "Presentation"
            presentation_match = re.search(r'Presentation  ', content)
            all_rights_match = re.search(r'All rights reserved.', content)

            if presentation_match and all_rights_match:
                start_index = presentation_match.end()
                end_index = all_rights_match.start()

                # Extract the cleaned content and remove leading/trailing whitespace
                cleaned_content = content[start_index:end_index].strip()

                # Write the cleaned content to the output file
                with open(output_file_path, 'w') as output_file:
                    output_file.write(cleaned_content)

if __name__ == "__main__":
    raw_data_folder = "raw-data"
    split_texts_folder = "split-texts"
    clean_text_files(raw_data_folder, split_texts_folder)
