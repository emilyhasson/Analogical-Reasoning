import tkinter as tk
from tkinter import messagebox
import csv
import os
import pandas as pd

POSITIVE_RESPONSES = "positive-responses.csv"
SAVE_LOC = 'user-responses.xlsx'
PROGRESS = 0

def check_progress():
    file_path = "progress.txt"

    # Check if the file "progress.txt" exists
    if os.path.exists(file_path):
        # If the file exists, try to read its contents and check if it's an integer
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                if content.strip().isdigit():
                    # If the content is an integer, return it
                    progress = int(content)
                    return progress
                else:
                    print("File 'progress.txt' exists, but its contents are not an integer.")
        except IOError as e:
            print("Error reading file:", str(e))
    else:
        # If the file does not exist, create it and write 0 to it
        try:
            with open(file_path, 'w') as file:
                file.write("0")
                print("File 'progress.txt' created with initial value 0.")
                return 0
        except IOError as e:
            print("Error creating file:", str(e))

def update_progress(index):
    file_path = "progress.txt"
    
    # Ensure the provided index is an integer
    if not isinstance(index, int):
        print("Error: Provided index is not an integer.")
        return

    try:
        with open(file_path, 'w') as file:
            file.write(str(index))
            print(f"Progress updated to {index} in 'progress.txt'.")
    except IOError as e:
        print("Error updating progress:", str(e))
        

def load_responses():
    data = []

    with open(POSITIVE_RESPONSES, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header row if it exists
        next(csv_reader, None)
        
        for row in csv_reader:
            if len(row) == 2:
                article, response = row
                data.append((article, response))

    return data



def record_response_xlsx(user_response, current_tuple):
    file_path = SAVE_LOC

    # Create or load the Excel file
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame()

    # Append data to the DataFrame
    new_data = {'FILE': current_tuple[0], 'CONTENT': current_tuple[1], 'USER-RESPONSE': user_response}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    # Save the DataFrame back to the Excel file
    df.to_excel(file_path, index=False)
    update_progress(current_index)

def next_string():
    global current_index, current_tuple

    if current_index < len(tuples):
        current_tuple = tuples[current_index]

        label1.config(text=current_tuple[0])

        text_widget1.config(state=tk.NORMAL)
        text_widget1.delete(1.0, tk.END)
        text_widget1.insert(tk.END, current_tuple[1])
        text_widget1.config(state=tk.DISABLED)

        progress_label.config(text=str(current_index + 1) + progress_label_text)

        current_index += 1
        
    else:
        messagebox.showinfo("Survey Completed", "All responses have been recorded in " + SAVE_LOC)
        root.quit()

def yes_button_clicked():
    record_response_xlsx("Yes", current_tuple)
    next_string()

def no_button_clicked():
    record_response_xlsx("No", current_tuple)
    next_string()

def flag_button_clicked():
    record_response_xlsx("Flag", current_tuple)
    next_string()

PROGRESS = check_progress()


tuples = load_responses()

current_index = PROGRESS
current_tuple = tuples[current_index]

root = tk.Tk()
root.title("Analogy Validator")
root.geometry("600x600")


label1 = tk.Label(root, text="", wraplength=400)  # Add label for the first Text widget
label1.grid(row=0, column=0, padx=10, pady=0)

text_widget1 = tk.Text(root, wrap=tk.WORD, height=10, width=30, state=tk.DISABLED)
text_widget1.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

scrollbar = tk.Scrollbar(root, command=text_widget1.yview)
scrollbar.grid(row=1, column=1, sticky='ns')

text_widget1.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, pady=10)

yes_button = tk.Button(button_frame, text="Yes", command=yes_button_clicked, width=10, height=2)
no_button = tk.Button(button_frame, text="No", command=no_button_clicked, width=10, height=2)
flag_button = tk.Button(button_frame, text="Flag", command=flag_button_clicked, width=10, height=2, fg="#8B0000")

yes_button.grid(row=0, column=0, padx=10)
no_button.grid(row=0, column=1, padx=10)
# Place the Flag button in the middle column with columnspan to center it
flag_button.grid(row=1, column=0, columnspan=2, padx=10)

progress_label_text = "/"+str(len(tuples))
progress_label = tk.Label(root, text="hi", wraplength=400)  # Add label for the second Text widget
progress_label.grid(row=4, column=0, padx=10, pady=0)

next_string()

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()



next_string()

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()