# Basic example of Web Scraping and Excel Export

This Python script performs web scraping on a specified URL and extracts paragraphs from the HTML content. It then cleans up the text and stores it in a pandas DataFrame. Finally, it exports the DataFrame to an Excel file with various options for customization using the `xlsxwriter` engine.

## Libraries Used

- **requests**: Used to send HTTP requests to the specified URL and retrieve the HTML content.
- **BeautifulSoup (bs4)**: Used to parse the raw HTML content and extract specific elements, such as paragraphs (`<p>` tags).
- **re**: Used for text cleaning by removing extra whitespace and special characters.
- **pandas**: Used to store the extracted paragraphs in a DataFrame for easy manipulation.
- **xlsxwriter**: Used as the engine for writing the DataFrame to an Excel file with custom options.

## How It Works

1. The script sends an HTTP GET request to the specified URL and retrieves the raw HTML content.
2. The HTML content is parsed using BeautifulSoup to extract paragraphs under a specific heading (`<h2>` tag).
3. Text cleaning is performed on each paragraph to remove extra whitespace and special characters.
4. The cleaned paragraphs are stored in a pandas DataFrame.
5. The DataFrame is exported to an Excel file (`output.xlsx`) with various options for sheet naming and formatting.

## Installation

```bash
pip install -r requirements.txt
```

## Run server locally for UI project  
```bash
python -m http.server -d ui/ 3000
```

## Running the code 
- Run the script main.py to perform web scraping and export the data to an Excel file.


## Customization Options

- **Sheet Names**: You can specify different sheet names for each export operation using the `sheet_name` parameter in the `to_excel` method.
- **Header Visibility**: You can control whether the DataFrame column names are included as the first row in the Excel file using the `header` parameter.
- **Starting Row and Column**: You can specify the starting row and column in the Excel file where the data should be written using the `startrow` and `startcol` parameters.
- **Floating Point Format**: You can specify a format string for floating-point numbers using the `float_format` parameter.
- **NaN Representation**: You can specify a string representation for NaN (Not a Number) values using the `na_rep` parameter.
- **Merge Cells**: You can control whether cells should be merged when writing MultiIndex columns using the `merge_cells` parameter.

