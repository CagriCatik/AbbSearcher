
# AbbSearcher

This is a simple tool (`AbbSearcher`) built with Python using the Tkinter library for creating a graphical user interface (GUI). The purpose of this tool is to search for and display descriptions associated with abbreviations stored in a local CSV or XLSX file.

## Usage

1. **Run the Application:**

   - Execute the code in a Python environment to launch the `AbbSearcher` application.
2. **Enter Abbreviation:**

   - Type an abbreviation into the entry field labeled "Enter an abbreviation."
3. **Search:**

   - Press the "Search" button or press Enter to initiate the search.
4. **View Results:**

   - The tool will display the corresponding descriptions for the entered abbreviation in the text area below.

## Features

- **Autocomplete:**

  - The abbreviation entry field supports autocomplete functionality, suggesting existing abbreviations as you type.
- **Multiple Descriptions:**

  - If an abbreviation has multiple associated descriptions, they will be displayed sequentially in the results.
- **Error Handling:**

  - The tool attempts to read the provided XLSX file first and falls back to CSV if unsuccessful. Any errors encountered during the file reading process are displayed in the console.

## File Format

- The tool supports both XLSX and CSV file formats.

## Dependencies

- The following Python libraries are required:
  - `tkinter` for GUI
  - `openpyxl` for XLSX file handling

## File Path

- The default file path for the local CSV or XLSX file is set to "AbbList.xlsx". Modify the `dateipfad` variable to point to your desired file.

