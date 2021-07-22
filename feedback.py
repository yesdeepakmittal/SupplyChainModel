import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import pandas as pd
import numpy as np
from sentiment import sentiment
import plotly.express as px

feed = pd.read_csv('data/feedback.csv')
temp = pd.DataFrame(feed.groupby('time')['sent_value'].sum())
temp.index.name = ''
temp = temp.reset_index()
temp.columns = ['time','sent_value']
sentiment = px.line(x=temp['time'], y=temp['sent_value'],)
sentiment.update_layout(template='plotly_white',height = 400,margin={"r": 150, "t": 20, "l": 150, "b": 110},)
del temp

map = px.scatter_mapbox(
        feed,
        title='feedback Location',
        lat="lat",
        lon="long",
        color="sentiment",
        # size=feed["score"].to_list(),
        size_max=10,
        hover_name="feedback",
        hover_data=["sentiment", "score",'confidence'],
    )

map.layout.update(
        margin={"r": 150, "t": 70, "l": 150, "b": 70},
        height=700,
        # width=700,
        coloraxis_showscale=False,
        mapbox_style='stamen-toner',
        mapbox=dict(center=dict(lat=29.0587, lon=77.6455), zoom=3),
    )

#%positive v/s %negative
pos = 0
for i in feed['sentiment']:
    if i == 'pos':
        pos += 1
positive = pos/feed['sentiment'].shape[0]*100
negative = 100 - pos/feed['sentiment'].shape[0]*100

import plotly.graph_objects as go
np = go.Figure()
np.add_trace(go.Indicator(
    mode = "number",
    value = positive,
    title = {"text": "Positive<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0, .25], 'y': [0, 1]}))

np.add_trace(go.Indicator(
    mode = "number",
    value = negative,
    title = {"text": "Negative<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.25, .5], 'y': [0, 1]}))

#NPS
promoters = 0
detractors = 0
for i in feed['score']:
    if i <= 6:
        detractors += 1
    elif i >= 9:
        promoters += 1
nps_score = (promoters-detractors)/feed['score'].shape[0]*100

np.add_trace(go.Indicator(
    mode = "number",
    value = nps_score,
    title = {"text": "<span style='font-size:300%;font-family:courier;color:darkgreen;'>NPS</span><br><span style='font-size:0.8em;color:gray'>range[-100,100]</span><br>"},
    domain = {'x': [0.5, 1], 'y': [0, 1]}))

del feed
layout = html.Div(children=[
    html.H1(children='Feedback'),
    html.Div(children='''Know about the customer experience with your product'''),
    dcc.Graph(id='example-np',figure=np),
    html.H1(children='''Customers Sentiment Score'''),
    dcc.Graph(id='example-sentiment',figure=sentiment),
    html.H1(children='''Customer Feedback Location'''),
    dcc.Graph(id='example-map',figure=map),],
    style={'color': 'navy', 'textAlign': 'center'})