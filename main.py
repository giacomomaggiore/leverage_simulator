from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
app = Dash()
import datetime as dt
from datetime import date
from modules import *
import yfinance as yf



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

def prova(param):
    df = pd.DataFrame(columns=["prova"])
    df["prova"] = [0,1,2,3]
    
    figure = px.scatter(df, title=param)
    return figure


app.layout = [
    html.H1(children='LEVERAGE SIMULATOR', style={'textAlign':'center'}),
    html.H3("Please enter your asset, starting ending date, leverage ratio"),
    
    dcc.Input(id="ticker", type="text",  debounce=True, value = "TSLA"),
    
    dcc.Input(id="leverage-ratio", type="number", min=0, max= 10, value = 2),
    
    dcc.DatePickerRange(
        id='date-range',
        min_date_allowed=date(1995, 8, 5),
        start_date=date(2020, 8, 5),
        end_date=date(2023, 8, 25)
    ),

    dcc.Graph(id ="graph", figure=False),
    html.Div(id = "prova", children = "")
]



@callback(
    Output('graph', 'figure'),
    Input("ticker", "value"),
    Input("leverage-ratio", "value"),
    Input("date-range",  "start_date"),
    Input("date-range", "end_date"),
)
def update_graph(ticker, leverage_ratio, start_date, end_date):
    
    data = apply_leverage(ticker, start_date, end_date, leverage_ratio)
    
    figure = px.line(data)
    
    return figure

if __name__ == '__main__':
    app.run(debug=False)