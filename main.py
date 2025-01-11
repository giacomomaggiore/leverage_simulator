from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


import datetime as dt
from datetime import date
from modules import *
import yfinance as yf

app = Dash(
        external_stylesheets=[dbc.themes.BOOTSTRAP]

    
)

asset_list = ["TSLA", "AAPL"]
leverage_range = [i/10 for i in range(0,110)]


title = html.H1(children='LEVERAG E SIMULATOR', style={'textAlign':'center'})
asset_dropdown =  dcc.Dropdown(asset_list, "TSLA", id="ticker")
leverage_dropdown = dcc.Dropdown(leverage_range, 2, id="leverage-ratio")



date_range_picker = dcc.DatePickerRange(
        id='date-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed= dt.datetime.today(),
        start_date=date(2020, 8, 5),
        end_date=dt.date.today(),
    )

default_df = pd.DataFrame(columns=["ROI", "CAGR", "SHARPE RATIO", "VOLATILITY", "MAX DROWDON"])

app.layout = [
    
    #HEADER
    html.Div(title),
    html.Div(children = [asset_dropdown,leverage_dropdown,date_range_picker]),

    dcc.Graph(id ="graph", figure=False),

    dash_table.DataTable(data = default_df.to_dict("records"), id = "table"),

]



@callback(
    Output('graph', 'figure'),
    Output("table", "data"),
    Input("ticker", "value"),
    Input("leverage-ratio", "value"),
    Input("date-range",  "start_date"),
    Input("date-range", "end_date"),
)
def update_graph(ticker, leverage_ratio, start_date, end_date):
    
    data = apply_leverage(ticker, start_date, end_date, leverage_ratio)
    results_df = pd.DataFrame(columns = ["ROI", "CAGR", "SHARPE RATIO", "VOLATILITY", "MAX DROWDON"])
    results_df["ROI"] = [roi(data["price"]), roi(data["lev_price"])]
    results_df["CAGR"] = [ cagr(data["price"]), cagr(data["lev_price"])]
    results_df["VOLATILITY"] = [volatility(data["price"]), volatility(data["lev_price"])]
    
    results_df = results_df.to_dict("records")
    print(results_df)
    figure = px.line(data)
    
    return figure, results_df

if __name__ == '__main__':
    app.run(debug=False)