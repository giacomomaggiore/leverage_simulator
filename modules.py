import yfinance as yf
import datetime as dt
import pandas as pd

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

print(apply_leverage("AAPL", start, end, 2))

