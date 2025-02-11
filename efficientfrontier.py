import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import datetime as dt
import mplcursors

riskfreerate = 0.02

def fetch_price_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data[ticker] = stock.history(start=start_date, end=end_date)
    return data

def calculate_daily_returns(data):
    for ticker in data:
        data[ticker]['Daily Return'] = data[ticker]['Close'].pct_change()
    return data

def align_data(data, tickers):
    # Align data to ensure all tickers have the same length and fill missing values
    df = pd.DataFrame({ticker: data[ticker]['Daily Return'] for ticker in tickers})
    df = df.dropna()
    return df

def generate_random_portfolios(data, tickers, num_portfolios=10000):
    aligned_data = align_data(data, tickers)
    mean_daily_returns = aligned_data.mean().values
    cov_matrix = aligned_data.cov().values
    
    results = np.zeros((3, num_portfolios))
    weights_record = []
    
    for i in range(num_portfolios):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        weights_record.append(weights)
        
        portfolio_return = np.sum(mean_daily_returns * weights) * 252
        portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
        
        results[0, i] = portfolio_return
        results[1, i] = portfolio_std_dev
        #Get the Risk Free Rate from the input
        risk_free_rate = entry_risk_free_rate.get()
        
        try:
            risk_free_rate = float(risk_free_rate)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid risk free rate")
            return
        
        results[2, i] = (results[0, i] - risk_free_rate) / results[1, i]  # Sharpe Ratio
    
    return results, weights_record

def plot_efficient_frontier(results, weights_record, tickers):
    fig, ax = plt.subplots(figsize=(12, 8))
    scatter = ax.scatter(results[1, :], results[0, :], c=results[2, :], cmap='YlGnBu', marker='o')
    ax.set_title('Efficient Frontier')
    ax.set_xlabel('Volatility (Std. Deviation)')
    ax.set_ylabel('Expected Returns')
    plt.colorbar(scatter, label='Sharpe Ratio')

    # Add interactive cursor
    cursor = mplcursors.cursor(scatter, hover=True)

    @cursor.connect("add")
    def on_add(sel):
        index = sel.index
        weights = weights_record[index]
        portfolio_str = "\n".join([f"{ticker}: {weight:.2%}" for ticker, weight in zip(tickers, weights)])
        sel.annotation.set(text=f"Portfolio {index + 1}\n{portfolio_str}", fontsize=8)

    plt.show()
    

def calculate_and_plot():
    tickers = entry_tickers.get().split(',')
    tickers = [ticker.strip() for ticker in tickers]
    
    if not tickers:
        messagebox.showerror("Input Error", "Please enter at least one ticker.")
        return
    
    start_date_str = entry_start_date.get()
    try:
        start_date = dt.datetime.strptime(start_date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid start date in MM/DD/YYYY format.")
        return
    
    end_date = dt.datetime.now().strftime('%Y-%m-%d')
    
    try:
        data = fetch_price_data(tickers, start_date, end_date)
        data = calculate_daily_returns(data)
        
        # Debugging: Print the aligned data
        aligned_data = align_data(data, tickers)
        print("Aligned Data:")
        print(aligned_data)
        
        results, weights_record = generate_random_portfolios(data, tickers)
        
        # Debugging: Print the results
        print("Results:")
        print(results)
        
        plot_efficient_frontier(results, weights_record, tickers)
        
        portfolio = weights_record[np.argmax(results[2])]
        portfolio_str = "\n".join([f"{ticker}: {weight:.2%}" for ticker, weight in zip(tickers, portfolio)])
        messagebox.showinfo("Optimal Portfolio", f"Optimal Portfolio:\n{portfolio_str}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Efficient Frontier Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Enter tickers (comma separated):").grid(row=0, column=0, padx=10, pady=10)
entry_tickers = tk.Entry(root, width=50)
entry_tickers.grid(row=0, column=1, padx=10, pady=10)

# Create and place the input field for dates
tk.Label(root, text="Enter Start Date for Estimated Returns (MM/DD/YYYY):").grid(row=1, column=0, padx=10, pady=10)
entry_start_date = tk.Entry(root, width=50)

entry_start_date.grid(row=1, column=1, padx=10, pady=10)


# Create and place the input field for the Risk Free Rate
tk.Label(root, text="Enter the Risk Free Rate:").grid(row=2, column=0, padx=10, pady=10)
entry_risk_free_rate = tk.Entry(root, width=50)
entry_risk_free_rate.grid(row=2, column=1, padx=10, pady=10)


# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_and_plot)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()