import os 
FOLDER_PATH = "raw-data/"
SAVE_PATH = "split-texts/"

# Read combined texts into dictionary
def read_files_in_folder(folder_path):
    file_texts = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                file_texts[filename] = file.read()
    return file_texts

def get_first_line(text):
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if line:
            invalid_chars = r'\/:*?"<>|'
            for char in invalid_chars:
                line = line.replace(char, '-')
            line = line.replace('.', '')
            return line
    return None  # If the string is empty or contains only empty lines

# Split combined text files into individual articles and store in text files
def split_articles(files_dict):
    articles_dict = {}
    i = 1
    for key in files_dict.keys():
        text = files_dict[key]
        articles = text.split("End of Document")
        articles.pop()
        for article in articles:
            articles_dict[i] = article

            # Delete end portion
            split_string = article.split("Classification\n")
            # split_string = article.split("Classification\nLanguage: ENGLISH")
            article = split_string[0]
            
            filename = get_first_line(article)

            # write to text file i.txt
            with open(SAVE_PATH + str(i) + '-' + filename +".txt", "w") as file:
                file.write(article)
            i += 1
    return articles_dict



def main():
    # Call the function to read files and store text in a dictionary
    print("reading files...")
    files_dict = read_files_in_folder(FOLDER_PATH)

    # Split each text file into individual articles, save as text files and store in dictionary (only works for LexisNexis articles)
    articles_dict = split_articles(files_dict)
    



    print(str(len(articles_dict))+" FILES SAVED")
    

main()