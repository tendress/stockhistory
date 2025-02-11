### Description: This script is used to get the updated fact sheets from the website and store them in the local directory. ###

import requests
import pandas as pd

#Open a csv file with a list of tickers and urls
df = pd.read_excel('factsheets/tickers.xlsx')
print(df)

tickers = {}

#make a dictionary item for each row in the dataframe
for index, row in df.iterrows():
    ticker = row['Ticker']
    url = row['FactSheetURL']
    tickers[ticker] = url

#loop through the dictionary and download the fact sheets
for ticker, url in tickers.items():
    response = requests.get(url)
    with open(f'factsheets/FS-{ticker}.pdf', 'wb') as file:
        file.write(response.content)
        print(f'{ticker} fact sheet downloaded successfully')