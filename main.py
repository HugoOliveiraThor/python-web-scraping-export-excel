import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url = 'http://127.0.0.1:3000/'
response = requests.get(url)
raw_html = response.content
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

# Function to clean up text
def clean_text(text):
    return re.sub(r'\s{1,}', ' ', text).strip()

# Empty list to store paragraphs
paragraphs = []


top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    # print(article)    
    if article is not None:
        for p in article.select('p'):
           # print(p) # All p selector
           # print(p.text) # Text of the p selector
            paragraphs.append(clean_text(p.text))
            print(clean_text(p.text)) # Remove spaces if was equal two removes spaces from start and end

# Create a DataFrame with the paragraphs
df = pd.DataFrame(paragraphs, columns=['Paragraph'])

# Save DataFrame to Excel with sheet_name
# df.to_excel('output_paragrapher.xlsx', index=False, sheet_name='paragrapher')

# df.to_excel('output_header_false.xlsx', index=False, sheet_name='paragrapher', header=False)

# df.to_excel('output_number_row_start.xlsx', index=False, sheet_name='paragrapher', startrow=2)

# df.to_excel('output_start_column_writing_data.xlsx', index=False, sheet_name='paragrapher', startcol=1)

# df.to_excel('output_float_numbers.xlsx', index=False, sheet_name='paragrapher', float_format='%.2f')

# df.to_excel('output_represent_Nan_values.xlsx', index=False, sheet_name='paragrapher', na_rep='NaN')

# df.to_excel('output_merge_cell_writings_columns.xlsx', index=False, sheet_name='paragrapher', merge_cells=False)


# Create an ExcelWriter object
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Save DataFrame to Excel with sheet_name
df.to_excel(writer, index=False, sheet_name='set-tab-name')
df.to_excel(writer, index=False, sheet_name='header-false', header=False)
df.to_excel(writer, index=False, sheet_name='start-row-2', startrow=2)
df.to_excel(writer, index=False, sheet_name='start-col-1', startcol=1)
df.to_excel(writer, index=False, sheet_name='float-format', float_format='%.2f')
df.to_excel(writer, index=False, sheet_name='not-a-number', na_rep='NaN')
df.to_excel(writer, index=False, sheet_name='merge-cells', merge_cells=False)
writer.close()