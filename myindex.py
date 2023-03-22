from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

from app import *
from components import home, sidebar

from sql_beta import df_material


# =========  Layout  =========== #

app.layout = dbc.Container([

    ## Stores vindos do banco de dados
    dcc.Location(id = "url"),
    dcc.Store(id = 'store_intermediario', data = {}),
    dcc.Store(id = 'store_material', data = df_material.to_dict()),
    dcc.Store(id = 'store_produto', data = {}),
    dcc.Store(id = 'store_orcamento', data = {}),
    html.Div(id = 'div_fantasma'),


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

# Callback para anexar dados no Banco de dados 
@app.callback(
    Output('div_fantasma', 'children'),
    Input('store_material', 'data')
)
def atualizar_banco(material_data):
    #Retranformar o dict em dataframe novamente
    df_material_aux = pd.DataFrame(material_data)

    #Preencher o SQL
    conn = sqlite3.connect('sistema.db')

    df_material_aux.to_sql('materiais', conn, if_exists = 'replace', index = False)
    conn.commit()
    conn.close()

    return []



if __name__ == '__main__':
    app.run(debug=True)