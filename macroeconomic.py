import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pandas as pd

india = pd.read_csv('data/india.csv')
india = px.line(x=india['year'], y=india.inflation,title='Inflation')
india.update_layout(template='simple_white',height = 600,margin={"r": 150, "t": 50, "l": 150, "b": 50},)

world = pd.read_csv('data/world.csv')
world = px.choropleth(world, locations="country", 
                    color=world['inflation'],
                    locationmode='country names', hover_name="country", 
                    animation_frame=world['year'],
                    title='Inflation over time', color_continuous_scale=px.colors.sequential.matter)

layout = html.Div([
                    html.H1(children='Macronomics Indicators'), 
                    html.H6(children='Visualising Inflation Data Over Time'), 
                    dcc.Graph(id='dist-chart', figure=india),
                    dcc.Graph(id='map', figure=world),
                ],
            style={'color': 'navy', 'textAlign': 'center'})
