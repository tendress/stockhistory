import yfinance as yf
import pandas as pd

class StockSplits:
        
        def __init__(self, ticker):
            """Initialize the Ticker Symbol"""
            self.ticker = ticker
            self.new_ticker = yf.Ticker(ticker)
            
        def getStockSplits(self):
            """Get Stock Splits"""
            stocksplit = self.new_ticker.splits
            self.stocksplit = stocksplit
            self.stocksplit.to_csv('Outputs/stocksplit.csv')
            

my_ticker = StockSplits('NVDA')
my_ticker.getStockSplits()
# The StockSplits class is used to get the stock splits for a given ticker symbol. The getStockSplits method is used to get the stock splits and save the data to a CSV file. The StockSplits class is similar to the StockHistory class, but it is used to get stock splits instead of stock price history.