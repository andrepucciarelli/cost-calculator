from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

from app import *
from components import home, sidebar


# =========  Layout  =========== #

app.layout = dbc.Container(children=[

    ## Stores vindos do banco de dados
    dcc.Location(id = "url"),
    dcc.Store(id = 'store_intermediario', data = {}),
    dcc.Store(id = 'store_material', data = {}),
    dcc.Store(id = 'store_produto', data = {}),
    dcc.Store(id = 'store_orcamento', data = {}),


    ## Layout da Página
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md = 2, style = {'padding': '0px'}),
        dbc.Col([
            dbc.Container(id = 'page_content', fluid = True, style = {'heigh': '100%', 'width': '100%'})
        ], md = 10, style = {'padding': '0px'})
    ])
], fluid=True)


# =========== Callbacks ============= #

# Callback para URL da Página
@app.callback(Output('page_content', 'children'), Input('url', 'pathname'))
def render_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home.layout
    else:
        return dbc.Container([
            html.H1('Página não encontrada')
        ])


if __name__ == '__main__':
    app.run(debug=True)