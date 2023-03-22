import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import pandas as pd
import json

from components import modal_novo_material, modal_novo_orcamento, modal_novo_produto






# ========= Layout ========= #
layout = dbc.Container([
    modal_novo_material.layout,
    modal_novo_produto.layout,
    modal_novo_produto.layout,
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1('EREXATAS')
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H3('Calculadora')
            ])
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\t INÍCIO'], href = '/home', active=True, style = {'text_align': 'center', 'font-size': '25px', 'margin-bottom': '10px', 'width':'100%'})),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-cube'), '\t NOVO MATERIAL'], id = 'botao_material', active=True, style = {'text_align': 'left', 'font-size': '25px', 'margin-bottom': '10px'})),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-cubes'), '\t NOVO PRODUTO'], id = 'botao_produto', active=True, style = {'text_align': 'left', 'font-size': '25px', 'margin-bottom': '10px'})),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-square'), '\t NOVO ORÇAMENTO'], id = 'botao_orcamento', active=True, style = {'text_align': 'left', 'font-size': '25px', 'margin-bottom': '10px'})),
            ])
        ])
    ])

], style = {'padding-top': '50px', 'margin-bottom': '100px', 'height': '90vh'}, className='text-center')





# =========  Callbacks  =========== #
@app.callback(
    Output('modal_novo_material', 'is_open'),
    #Input('modal_botao_salvar_material', 'n_clicks'),
    #Input('modal_botao_cancelar_material', 'n_clicks'),
    Input('botao_material', 'n_clicks'),
    State('modal_novo_material', 'is_open')
)
def modal_novo_material(n,is_open):
    if n:
        return not is_open
    return is_open
