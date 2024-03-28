import tkinter as tk
from tkinter import ttk
import csv
from openpyxl import load_workbook

# File path to local CSV or XLSX file
file_path = "AbbList.xlsx"

# Function to read the file and create a dictionary
def load_file_into_dictionary(file_path):
    abbreviations_descriptions = {}
    
    try:
        # Try to open the file as XLSX
        workbook = load_workbook(filename=file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header row
            if len(row) >= 2:
                abbreviation = row[0].lower()
                description = row[1]
                if abbreviation in abbreviations_descriptions:
                    abbreviations_descriptions[abbreviation].append(description)
                else:
                    abbreviations_descriptions[abbreviation] = [description]
    
    except Exception as e:
        # If unable to open as XLSX, try as CSV
        print(f"Error reading XLSX file: {e}")
        try:
            with open(file_path, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    if len(row) >= 2:
                        abbreviation = row[0].lower()
                        description = row[1]
                        if abbreviation in abbreviations_descriptions:
                            abbreviations_descriptions[abbreviation].append(description)
                        else:
                            abbreviations_descriptions[abbreviation] = [description]
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    return abbreviations_descriptions

# Function for search
def search_description(event=None):
    abbreviation = input_abbreviation_var.get().lower()
    descriptions_text.config(state=tk.NORMAL)
    descriptions_text.delete(1.0, tk.END)

    if abbreviation in abbreviations_descriptions:
        descriptions = abbreviations_descriptions[abbreviation]
        for idx, description in enumerate(descriptions, start=1):
            descriptions_text.insert(tk.END, f"{idx}. {description}\n")
    else:
        descriptions_text.insert(tk.END, "Abbreviation not found")

    descriptions_text.config(state=tk.DISABLED)

# Autocomplete function for the input field
def autocomplete(entry, list):
    current_text = entry.get().lower()
    filtered_list = [item for item in list if current_text in item.lower()]
    entry['values'] = filtered_list

# Function to load the file into the dictionary at start
def load_dictionary():
    return load_file_into_dictionary(file_path)

# Create GUI
root = tk.Tk()
root.title("AbbSearcher")

input_label = tk.Label(root, text="Enter an abbreviation:")
input_label.pack()

input_abbreviation_var = tk.StringVar()
input_abbreviation = ttk.Combobox(root, textvariable=input_abbreviation_var)
input_abbreviation.pack()

# Load file into dictionary (only once)
abbreviations_descriptions = load_dictionary()

input_abbreviation['values'] = list(abbreviations_descriptions.keys())
input_abbreviation.bind('<KeyRelease>', lambda event: autocomplete(input_abbreviation, list(abbreviations_descriptions.keys())))
input_abbreviation.bind("<Return>", search_description)

search_button = tk.Button(root, text="Search", command=search_description)
search_button.pack()

descriptions_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
descriptions_text.pack()
descriptions_text.config(state=tk.DISABLED)

root.mainloop()
