import yfinance as yf
import pandas as pd
import streamlit as st

class StockHistory:
    
    def __init__(self, ticker, startdate, enddate, initialamt):
        """Initialize the Ticker Symbol"""
        self.ticker = ticker
        self.startdate = startdate
        self.enddate = enddate
        self.initialamt = initialamt
        self.new_ticker = yf.Ticker(ticker)
        
    def getHistory(self):
        """Get Stock Price History"""
        stockhistory = self.new_ticker.history(start=str(self.startdate), end=str(self.enddate), actions=False)
        #just get the closing price
        self.stockhistory = stockhistory['Close']
        self.stockhistory = pd.DataFrame(stockhistory)
        
    def getMyPortfolio(self):
        """Provided an initial amount, calculate the portfolio value"""
        # calculate the percent change in share price from the previous day
        self.stockhistory['DailyReturn'] = self.stockhistory['Close'].pct_change()
        # create a column that takes the initial amount and adds the daily return
        self.stockhistory['PortfolioValue'] = self.initialamt * (1 + self.stockhistory['DailyReturn']).cumprod()
        # self.stockhistory.to_csv('Outputs/portfolio.csv')
        return self.stockhistory

# Streamlit app
st.title("Stock History App")

# Input fields
ticker = st.text_input("Ticker:")
startdate = st.date_input("Start Date")
enddate = st.date_input("End Date")
initialamt = st.number_input("Initial Amount", min_value=0.0, step=100.0)

if st.button("Get Portfolio"):
    stock_history = StockHistory(ticker, startdate, enddate, initialamt)
    stock_history.getHistory()
    portfolio = stock_history.getMyPortfolio()
    st.success("Portfolio calculated")
    st.dataframe(portfolio)
