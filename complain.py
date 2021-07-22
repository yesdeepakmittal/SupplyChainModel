import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import pandas as pd
import numpy as np
from sentiment import sentiment
import plotly.express as px

complain = pd.read_csv('data/complain.csv')

#sentiment score chart - complain
temp = pd.DataFrame(complain.groupby('time')['sent_value'].sum())
temp.index.name = ''
temp = temp.reset_index()
temp.columns = ['time','sent_value']
sentiment = px.line(x=temp['time'], y=temp['sent_value'],)
sentiment.update_layout(template='plotly_white',height = 400,margin={"r": 150, "t": 20, "l": 150, "b": 110},)
del temp

#%positive v/s %negative
pos = 0
for i in complain['sentiment']:
    if i == 'pos':
        pos += 1
positive = pos/complain['sentiment'].shape[0]*100
negative = 100 - pos/complain['sentiment'].shape[0]*100

import plotly.graph_objects as go
np = go.Figure()
np.add_trace(go.Indicator(
    mode = "number",
    value = positive,
    title = {"text": "Positive Complain<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.1, .5], 'y': [0, 1]}))

np.add_trace(go.Indicator(
    mode = "number",
    value = negative,
    title = {"text": "Negative Complain<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.5, .9], 'y': [0, 1]}))


#complain Location map
map = px.scatter_mapbox(
        complain,
        title='Complain Location',
        lat="lat",
        lon="long",
        color="n_revalid",
        size=complain["n_revalid"].to_list(),
        size_max=10,
        hover_name="complain",
        hover_data=["sentiment", "n_revalid",'confidence'],
    )

map.layout.update(
        margin={"r": 150, "t": 70, "l": 150, "b": 70},
        height=700,
        # width=700,
        coloraxis_showscale=False,
        mapbox_style='stamen-toner',
        mapbox=dict(center=dict(lat=29.0587, lon=77.6455), zoom=3),
    )

del complain
layout = html.Div(children=[
    html.H1(children='Complain'),
    html.Div(children='''What your customers are complaining?'''),
    dcc.Graph(id='example-negpos',figure=np),
    html.H1(children='''Customers Sentiment Score'''),
    dcc.Graph(id='example-sentiment',figure=sentiment),
    html.H1(children='''Where your customers are complaining and how many times reverifying your product?'''),
    dcc.Graph(id='example-map',figure=map),],
    style={'color': 'navy', 'textAlign': 'center'})