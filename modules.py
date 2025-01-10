import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np

start = "2020-01-01"
end= "2022-01-01"

def get_data(ticker, start, end):
    df = yf.download(ticker, start, end)
    data = pd.DataFrame(index = df.index)
    data["price"] = df["Adj Close"]
    
    return data


def apply_leverage(ticker, start, end, leverage_ratio):
    data = get_data(ticker, start, end)
    
    data["return"] = (data["price"] - data["price"].shift(1)) / data["price"].shift(1)
    
    for x in range(len(data.index.to_list())):
        if x == 0:
            data.loc[data.index[x], "lev_price"] = data.loc[data.index[x], "price"]
        if x != 0:
            data.loc[data.index[x], "lev_price"] = data.loc[data.index[x-1], "lev_price"] * (1 + (data.loc[data.index[x], "return"]*leverage_ratio))

    data.drop(["return"], axis = 1, inplace = True)
    return data


def roi(df):
  return (df.iloc[-1] - df.iloc[0]) / df.iloc[0]*100

def cagr(df):
  return ((df.iloc[-1] / df.iloc[0]) ** (1 / (len(df) / 252)) - 1)*100

def sharpe_ratio(df, risk_free):
  average_return = float(df.pct_change(fill_method=None).mean()) * 252

  sigma = volatility(df)
  print(average_return)
  sharpe_ratio = (average_return - risk_free * 0.01) / sigma

  sharpe_ratio = '%.3f'%(sharpe_ratio)
  sharpe_ratio = float(sharpe_ratio)

  return sharpe_ratio

def volatility(df):
  return df.pct_change(fill_method=None).std() * np.sqrt(252)