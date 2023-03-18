from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

from app import *
from components import home, sidebar




# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[





], fluid=True,)




if __name__ == '__main__':
    app.run(debug=True)