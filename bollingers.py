import yfinance as yf
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Fetch price history from Yahoo Finance
def fetch_price_history(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

# Calculate Bollinger Bands
def calculate_bollinger_bands(df, window=20, num_std_dev=2):
    df['SMA'] = df['Close'].rolling(window=window).mean()
    df['Upper Band'] = df['SMA'] + (df['Close'].rolling(window=window).std() * num_std_dev)
    df['Lower Band'] = df['SMA'] - (df['Close'].rolling(window=window).std() * num_std_dev)
    return df

# Plot candlestick chart with Bollinger Bands
def plot_candlestick_with_bollinger_bands(df, ticker):
    # Create a new DataFrame for mplfinance
    df_mpf = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
    
    # Add Bollinger Bands to the plot
    apds = [
        mpf.make_addplot(df['Upper Band'], color='r'),
        mpf.make_addplot(df['Lower Band'], color='r'),
        mpf.make_addplot(df['SMA'], color='g')
    ]
    
    # Plot the candlestick chart
    mpf.plot(df_mpf, type='candle', style='charles', addplot=apds, title=f'{ticker} Price History with Bollinger Bands', ylabel='Price', volume=True)
    
# Main function
def main():
    ticker = 'SPY'  # Example ticker
    start_date = '2000-01-01'
    end_date = '2023-01-01'
    
    # Fetch price history
    df = fetch_price_history(ticker, start_date, end_date)
    
    # Calculate Bollinger Bands
    df = calculate_bollinger_bands(df)
    
    # Plot candlestick chart with Bollinger Bands
    plot_candlestick_with_bollinger_bands(df, ticker)

if __name__ == "__main__":
    main()