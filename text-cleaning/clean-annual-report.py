import os
import spacy
import openai
import config
import csv

TEXTS_FOLDER = "../pdf-recognition/test-outputs/pos/" # Location of text files to be read
OUTPUT_FOLDER = "output/" # Folder for cleaned documents



# def main():

#     print("reading files...")
#     texts = read_files_in_folder(TEXTS_FOLDER)
    
#     results = clean_texts(texts)
#     save_responses_to_txt(results)

    
# main()