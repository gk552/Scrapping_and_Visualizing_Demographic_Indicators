import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Demographics_of_Germany'
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
data_table = soup.find_all('table', attrs={'class': 'wikitable sortable'})
required_table = data_table[0]
# print(required_table)

headers = [header.text.strip()
           for header in required_table.find_all('th', limit=9)]
# print(headers)
rows = []

# Find all `tr` tags
data_rows = required_table.find_all('tr')

for row in data_rows:
    value = row.find_all('td', limit=9)
    beautified_value = [ele.text.strip() for ele in value]
    # Remove data arrays that are empty
    if len(beautified_value) == 0:
        continue
    rows.append(beautified_value)
    # print(rows)

# Create a pandas DataFrame from the table data
df = pd.DataFrame(rows, columns=headers)
print(df)

# Write the DataFrame to an Excel sheet
writer = pd.ExcelWriter('Germany_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer._save()
