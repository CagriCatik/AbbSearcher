# AbbSearcher

`AbbSearcher` is a simple Python application built using the Tkinter library for creating a graphical user interface (GUI) to search and visualize information from an Excel file containing abbreviations and their descriptions.

## Features

* **Search Abbreviations** : Enter an abbreviation in the search box to retrieve its corresponding descriptions.
* **Detailed Description** : View a detailed description of an abbreviation in a separate window.
* **Statistics & Plot** : Generate and display statistics on the distribution of abbreviations across different starting letters along with a corresponding plot.

## Installation

1. Clone the repository to your local machine:

```sh
  git clone https://github.com/CagriCatik/AbbSearcher/tree/main
```

2. Navigate to the project directory:

```sh
  cd AbbSearcher
```

3. Install the required dependencies:

```sh
  pip install openpyxl matplotlib
```

## Usage

Run the application by executing the following command in your terminal:

```sh
  python main.py
```

The GUI will open, allowing you to search for abbreviations, view detailed descriptions, and generate statistics.

## Instructions

1. **Search Tab** :

* Enter an abbreviation in the search box.
* Press "Search" to retrieve corresponding descriptions.
* The detailed description will automatically appear in a new window.

1. **Statistics & Plot Tab** :

* Click on "Show Statistics & Plot" to view a statistical analysis and plot of the abbreviations.

1. **Autocomplete** :

* The search box supports autocomplete for easier abbreviation input.

1. **Warning** :

* If no data is available for the plot, a warning message will be displayed.

## Excel File Format

The application assumes that the Excel file (`AbbList.xlsx`) contains sheets for each alphabet letter, with three columns: `Abbreviation`, `Description`, and `Detailed Description`.
