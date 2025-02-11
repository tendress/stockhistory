import yfinance as yf
import pandas as pd
import json

tickerlist = pd.read_csv('modeltickers.csv')
#print(tickerlist)
tickermins = {}

my_ticker = yf.Ticker('QQQM')
info = my_ticker.get_news()
# print json info about the ticker in a pretty way
print(info)
