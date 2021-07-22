#https://plotly.com/python/indicator/
import plotly.graph_objects as go

  
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import pandas as pd
product = pd.read_csv('data/product.csv')
validation = pd.read_csv('data/validation.csv')
complain = pd.read_csv('data/complain.csv')

product_verified_count = 0
for i in validation.id:
    product_verified_count += int(validation[validation['id'] == i]['time'] < product[product['id'] == i]['doe'])

reverified_count = 0
for i in complain.id:
    reverified_count += int(complain[complain['id'] == i]['time'] < product[product['id'] == i]['doe'])

import datetime
product_not_expired_count = sum([1 for i in product.id if int(datetime.datetime.now() < pd.to_datetime(product[product['id'] == i]['doe']))])
product_not_expired_count = 6

verified_percentage =     round(product_verified_count/product_not_expired_count*100,2)
unverified_percentage = 100 - verified_percentage
reverified_percentage = round(reverified_count/product_not_expired_count*100,2)

fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "number",
    value = verified_percentage,
    title = {"text": "Products Verified<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0, .33], 'y': [0, 1]}))

fig.add_trace(go.Indicator(
    mode = "number",
    value = unverified_percentage,
    title = {"text": "Products Unverified<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.33, .66], 'y': [0, 1]}))
fig.add_trace(go.Indicator(
    mode = "number",
    value = reverified_percentage,
    title = {"text": "Products Reverified<br><span style='font-size:0.8em;color:gray'>(in percentage)</span><br>"},
    domain = {'x': [0.66, 1], 'y': [0, 1]}))

import plotly.express as px
map = px.scatter_mapbox(
        validation,
        title='Customer Location',
        lat="lat",
        lon="long",
        size=[1 for i in range(validation.shape[0])],
    )

map.layout.update(
        margin={"r": 150, "t": 70, "l": 150, "b": 70},
        height=700,
        # width=700,
        coloraxis_showscale=False,
        mapbox_style='stamen-toner',
        mapbox=dict(center=dict(lat=29.0587, lon=77.6455), zoom=3),
    )

layout = html.Div([
                    html.H1(children='Product'), 
                    html.H6(children='Visualising where your costumers are..'), 
                    dcc.Graph(id='dist-chart', figure=fig),
                    html.H1(children='Product Verification Location'),
                    dcc.Graph(id='map', figure=map),
                ],
            style={'color': 'navy', 'textAlign': 'center'})
