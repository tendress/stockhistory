import yfinance as yf
import pandas as pd



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
        #self.stockhistory.to_csv('stockhistory.csv')
        
    def getMyPortfolio(self):
        """Provided an initial amount, calculate the portfolio value"""
        # calculate the percent change in share price from the previous day
        self.stockhistory['DailyReturn'] = self.stockhistory['Close'].pct_change()
        # create a column that takes the initial amount and adds the daily return
        self.stockhistory['PortfolioValue'] = self.initialamt * (1 + self.stockhistory['DailyReturn']).cumprod()
        self.stockhistory.to_csv(f'Outputs/portfolio{self.ticker}-{self.startdate}-{self.enddate}.csv')
        
        


my_ticker = StockHistory('PEP', startdate='2024-12-11', enddate='2025-01-15', initialamt=32155.60)
my_ticker.getHistory()
my_ticker.getMyPortfolio()

