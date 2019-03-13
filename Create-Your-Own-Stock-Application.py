import pandas_datareader as web 
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import yahoo_finance as yahoo
import time
from collections import deque
import plotly.graph_objs as go
#import random

app = dash.Dash('stock-data')
#use deque to add to the list fast using pop
max_length = 50
times = deque(maxlen=max_length)
SClose = deque(maxlen=max_length)
SOpen = deque(maxlen=max_length)
#SCloseAvg = deque(maxlen=max_length)
#SOpenAvg = deque(maxlen=max_length)
SVolume = deque(maxlen=max_length)
#SMACD = deque(maxlen=max_length)
#SRSI = deque(maxlen=max_length)

data_dict = {
"Close":SClose,
"Open":SOpen,
#"Close Avg":SCloseAvg,
#"Open Avg":SOpenAvg,
"Volume":SVolume
}

app.layout = html.Div(children=[
    html.Div(children='''
    Symbol to graph:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
    ])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start=datetime.datetime(2018, 1, 1)
    end=datetime.datetime.now()
    df= web.DataReader(input_data, 'yahoo', start, end)


    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': df.index, 'y':df.Close, 'type':'line', 'name':'Close'},
                {'x': df.index, 'y':df.Open, 'type':'line', 'name':'Open'},
                #{'x': df.index, 'y':df.Volume, 'type':'line', 'name':'Volume'},
                #{'x': df.index, 'y':df['Close'].pct_change(), 'type':'line', 'name':'%Change'},
                #{'x': df.index, 'y':df['Open'].pct_change(), 'type':'line', 'name':'%Change'},
            ],
            'layout':{
                'title':input_data
            }
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
