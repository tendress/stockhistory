import yfinance as yf
import pandas as pd



class StockInfo:
    
    def __init__(self, ticker, startdate, enddate):
        """Initialize the Ticker Symbol"""
        self.ticker = ticker
        self.startdate = startdate
        self.enddate = enddate
        self.new_ticker = yf.Ticker(ticker)
        
    def getStockInfo(self):
        """Get Stock Company Information """
        stockinfo = self.new_ticker.info
        self.stockinfo = pd.DataFrame(stockinfo)
        self.stockinfo.to_csv('Outputs/stockinfo.csv')

    def getInstitutionalShareholders(self):
        """Get Institutional Shareholders"""
        inst_shareholders = self.new_ticker.institutional_holders
        self.inst_shareholders = pd.DataFrame(inst_shareholders)
        self.inst_shareholders.to_csv('Outputs/institutional_shareholders.csv')
        
    def getMajorHolders(self):
        """Get Major Holders"""
        major_holders = self.new_ticker.major_holders
        insider_roster = self.new_ticker.get_insider_roster_holders()
        self.major_holders = pd.DataFrame(major_holders)
        self.major_holders.to_csv('Outputs/major_holders.csv')
        self.insider_roster = pd.DataFrame(insider_roster)
        self.insider_roster.to_csv('Outputs/insider_roster.csv')
        
        


my_ticker = StockInfo('HODL.CN', startdate='2020-05-19', enddate='2024-09-09')
#my_ticker.getStockInfo()
#my_ticker.getInstitutionalShareholders()
my_ticker.getMajorHolders()

