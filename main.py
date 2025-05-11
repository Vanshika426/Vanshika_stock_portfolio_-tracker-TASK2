import pandas as pd
import yfinance as yf
from tabulate import tabulate

portfolio = pd.read_csv("portfolio.csv")
portfolio["Current Price"] = 0.0
portfolio["Total Value"] = 0.0
portfolio["Profit/Loss"] = 0.0

for i in range(len(portfolio)):
    symbol = portfolio.loc[i, "Symbol"]
    shares = portfolio.loc[i, "Shares"]
    bought_price = portfolio.loc[i, "Bought_Price"]

    stock = yf.Ticker(symbol)
    live_price = stock.history(period="1d")["Close"].iloc[-1]

    portfolio.at[i, "Current Price"] = round(live_price, 2)
    total_value = shares * live_price
    portfolio.at[i, "Total Value"] = round(total_value, 2)
    profit_loss = (live_price - bought_price) * shares
    portfolio.at[i, "Profit/Loss"] = round(profit_loss, 2)

print(tabulate(portfolio, headers="keys", tablefmt="pretty", showindex=False))
