from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd
from asset_list import asset_list

import datetime as dt
from datetime import date
from modules import *
import yfinance as yf

app = Dash()
server = app.server



leverage_range = [i/10 for i in range(0,110)]
risk_free = 0.02
default_df = pd.DataFrame(index=["ROI", "CAGR", "SHARPE RATIO", "VOLATILITY", "MAX DRAWDON"])


title = html.H1(children='LEVERAGE SIMULATOR', style={'textAlign':'center'})

subtitle = html.H4(children="Leverage is like hot sauce—just a little can spice things up, but too much will burn everything down.")


asset_dropdown =  dcc.Dropdown(options=[{'label': asset.get("name"), 'value': asset.get("ticker")} for asset in asset_list], id="ticker", className="ticker", value = "TSLA")

#options=[{'label': etf, 'value': etf} for etf in asset_list]

leverage_dropdown = dcc.Dropdown(leverage_range, 2, id="leverage-ratio", className="leverage-ratio")
date_range_picker = dcc.DatePickerRange(
        id='date-range',
        className = "date-range",
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed= dt.datetime.today(),
        start_date=date(2020, 8, 5),
        end_date=dt.date.today(),
    )

table_results = dash_table.DataTable(data = default_df.to_dict("records"), id = "table", style_cell={'textAlign': 'left'},
             style_as_list_view=True,),


input_div = html.Div(id = "input-div", children = [asset_dropdown, leverage_dropdown,    date_range_picker,
 ])


mention_footer = html.A("Made with ♥ by Giacomo Maggiore", href='https://www.linkedin.com/in/giacomo-maggiore-499994263/', target="_blank")
footer = html.Div(id = "footer", children=mention_footer)


app.layout = [
    
    #HEADER
    html.Header([title,
             subtitle
            ],
             className = "header"),
    
    
    html.Div(className="content", children = [
        
    input_div,
        
    html.Div(
        className = "content-graph",
        children = [dcc.Graph(id ="graph", figure=False)]),
    html.Div(className = "content-table",
             children = table_results,             )],
    
    
            ),
    footer

    

    

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
    results_df = pd.DataFrame(index = ["ROI", "CAGR", "VOLATILITY", "SHARPE RATIO", "MAX DRAWDOWN"],
                              columns=[" ", ticker, ticker + " "+ str(leverage_ratio)+"x"])
    
    results_df[ticker] = [roi(data["price"]), cagr(data["price"]),volatility(data["price"]), sharpe_ratio(data["price"], risk_free), max_drawdown(data["price"])]
    results_df[ticker + " "+ str(leverage_ratio)+"x"] = [roi(data["lev_price"]), cagr(data["lev_price"]),volatility(data["lev_price"]), sharpe_ratio(data["lev_price"], risk_free), max_drawdown(data["lev_price"])]
    results_df[" "] = ["ROI", "CAGR", "VOLATILITY", "SHARPE RATIO", "MAX DRAWDOWN"]

    data = data.rename(columns={"price": "Price", "lev_price": "Price"+str(leverage_ratio)+"x"})
   
    results_df = results_df.to_dict("records")
    print(results_df)
    figure = px.line(data)
    
    return figure, results_df

if __name__ == '__main__':
    app.run(debug=False)