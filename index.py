import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import server
from app import app

import complain,feedback,home,macroeconomic,socialmedia

#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
navbar = dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink("Home", href="/home")),
                        dbc.NavItem(dbc.NavLink("Social Media", href="/socialmedia")),
                        dbc.NavItem(dbc.NavLink("Macroeconomic Indicators", href="/macroeconomic")),
                        dbc.NavItem(dbc.NavLink("Feedback", href="/feedback")),
                        dbc.NavItem(dbc.NavLink("Complain", href="/complain")),
                        ])

app.layout = html.Div([
	dcc.Location(id='url',refresh=False),
	navbar,
	html.Div(id='page-content')
	])

@app.callback(Output('page-content','children'),
	[Input('url','pathname')])
def display_page(pathname):
    if pathname == '/socialmedia':
        return socialmedia.layout
    elif pathname == '/macroeconomic':
        return macroeconomic.layout
    elif pathname == '/feedback':
        return feedback.layout
    elif pathname == '/complain':
        return complain.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)