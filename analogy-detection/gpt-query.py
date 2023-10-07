import os
import spacy
import openai
import config
import csv

TEXTS_FOLDER = "../pdf-recognition/test-outputs/pos/" # Location of text files to be read
RESPONSE_FILE = "responses.csv" # File where GPT responses will be saved in full

# Read texts from each file into dictionary
def read_files_in_folder(folder_path):
    file_texts = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_texts[filename] = file.read()
    return file_texts

# Split each text into chunks
def split_text_into_chunks(text, max_tokens=500):

    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 2000000  # Adjust the value as per your needs
    doc = nlp(text)
   
    chunks = []
    current_chunk = ""
    current_tokens = 0
   
    for sentence in doc.sents:
        num_tokens = len(sentence)
       
        # If adding this sentence doesn't exceed the maximum token limit, add it to the current chunk
        if current_tokens + num_tokens <= max_tokens:
            current_chunk += ' ' + str(sentence)
            current_tokens += num_tokens
        else:
            # Otherwise, add the current chunk to the list of chunks and start a new one
            chunks.append(current_chunk)
            current_chunk = str(sentence)
            current_tokens = num_tokens
   
    # Add any remaining chunk to the list of chunks
    if current_chunk:
        chunks.append(current_chunk)
   
    return chunks


# Call GPT on each chunk and save results
def gpt3(stext):
    openai.api_key = config.GPT_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=stext,
        temperature=0.1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
    

def try_gpt(querySpell, n):
    try:
        response = gpt3(querySpell)
        return response
    except Exception as e:
        print("An error occurred:", type(e).__name__, ":", str(e))
        if n < 4:
            return try_gpt(querySpell, n+1)
        else:
            return "EXCEPTION"
        

# Get relevance from texts
def get_analogies(articles_dict):
    results = articles_dict.copy()
    for key in results:
        results[key] = []
    print("creating chunks...")
    for key in articles_dict.keys():
        text = articles_dict[key]
        chunks =  split_text_into_chunks(text)

    # Call GPT
        for chunk in chunks:
            print("calling GPT...")
            querytxt = chunk
            # querySpell = f"In the 1980s and 1990s, the electric power industry underwent deregulation and trading changes. During this time many companies were referencing other industries which underwent similar changes in order to justify or guide their actions. For example, one executive said 'SCANA has evaluated the process of deregulation and its impact on other industries, including the natural gas business, and several points are clear. Competition may benefit customers, but does not automatically benefit investors or employees. Significant alteration in the traditional ways of doing business is required. The winners in a more competitive environment are those companies which are more agile and innovative.' I want you to look at an excerpt from a power industry annual report and decide whether the author(s) have made any such comparisons to other industries. Your respone should be either 'No' or 'Yes: [Quote from article containing comparison]'. That is, if the text contains a comparison or reference of this sort, report it specifically as a quote from the text. Excerpt: {querytxt}"
            # querySpell = "In the 1980s and 1990s, the electric power industry underwent deregulation and trading changes. During this time many companies were referencing other industries which underwent similar changes in order to justify or guide their actions. For example, one executive said 'SCANA has evaluated the process of deregulation and its impact on other industries, including the natural gas business, and several points are clear. Competition may benefit customers, but does not automatically benefit investors or employees. Significant alteration in the traditional ways of doing business is required. The winners in a more competitive environment are those companies which are more agile and innovative.' I want you to look at an excerpt from a power industry annual report and decide whether the author(s) have made any such comparisons to other industries. Your respone should be either 'No' or 'Yes: [Quote from article containing comparison]'. That is, if the text contains a comparison or reference of this sort, report it specifically as a quote from the text. Excerpt: {The regulatory changes we’re experiencing on the electric side of our business are similar to those we’ve experienced in the natural gas industry over the past decade. }"
            querySpell = (
                # f"In the 1980s and 1990s, the electric power industry underwent deregulation and trading changes. "
                # ""
                # "During this time many companies were referencing other industries which underwent similar "
                # "changes in order to justify or guide their actions. "
                # ""
                # "For example, one executive said: "
                # "'SCANA has evaluated the process of deregulation and its impact on other industries, "
                # "including the natural gas business, and several points are clear. Competition may benefit "
                # "customers, but does not automatically benefit investors or employees. Significant alteration "
                # "in the traditional ways of doing business is required. The winners in a more competitive "
                # "environment are those companies which are more agile and innovative.' "
                # ""
                # "I want you to look at an excerpt from a power industry annual report and decide whether "
                # "the author(s) have made any such comparisons to other industries. "
                # ""
                # "Your respone should be either 'No' or 'Yes: [Quote from excerpt containing comparison]'. "
                # ""
                # "That is, if the text contains a comparison or reference of this sort, report it "
                # "specifically as a quote from the text. "
                # ""
                # "Excerpt: "
                # "{querytxt}"


                f"I want you to look at an excerpt from a power industry annual report and decide whether "
                "the author(s) are making decisions based on knowledge of events that occured in "
                "other industries. "
                ""
                "Your respone should be either 'No' or 'Yes: [Quote from excerpt containing comparison]'. "
                ""
                "That is, if the text contains a comparison or reference of this sort, report it "
                "specifically as a quote from the text. "
                ""
                "Excerpt: "
                "{querytxt}"
            )
            response = try_gpt(querySpell, 1)
            print(str(key) + ": " + response)
            results[key].append(response)

    return results

def save_responses_to_csv(dictionary, file_path=RESPONSE_FILE):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write each key-value pair as a row in the CSV file
        for key, values in dictionary.items():
            values_str = '$$$ '.join(values)  # Convert list to $$$ -separated string
            writer.writerow([key, values_str.lstrip('\n')])




def main():

    print("reading files...")
    texts = read_files_in_folder(TEXTS_FOLDER)
    
    results = get_analogies(texts)
    save_responses_to_csv(results)

    
main()