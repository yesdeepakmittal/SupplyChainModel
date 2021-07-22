# import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

#🎯for checking purpose uncomment these lines
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

temp = pd.read_csv('data/yesdeepakmittal_tweets.csv')
temp = pd.DataFrame(temp.groupby('time')['sent_value'].sum())
temp.index.name = ''
temp = temp.reset_index()
temp.columns = ['time','sent_value']
fig = px.line(x=temp['time'], y=temp['sent_value'],)
fig.update_layout(template='plotly_white',height = 400,margin={"r": 150, "t": 50, "l": 150, "b": 50},
                    title='')

del temp
#🎯for checking purpose, use app.layout instead of layout
layout = html.Div([    
                    html.H1(children='Social Media'), 
                    html.H6(children='Visualising Customer Tweets Sentiment Score'), 
                    dcc.Graph(id='tw-sentiment', figure=fig),
                ],
            style={'color': 'navy', 'textAlign': 'center'})

#🎯for checking purpose uncomment these lines
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8049, host='127.0.0.1')