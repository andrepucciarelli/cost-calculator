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
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\t INÍCIO'], href = '/home', active=True, style = {'text_align': 'center'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa-brands fa-font-awesome'), '\t NOVO MATERIAL'], href = '/home', active=True, style = {'text_align': 'center'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\t NOVO PRODUTO'], href = '/home', active=True, style = {'text_align': 'center'})),
                html.Br(),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), '\t NOVO ORÇAMENTO'], href = '/home', active=True, style = {'text_align': 'center'})),
                html.Br()
            ])
        ])
    ])

], style = {'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center')





# =========  Callbacks  =========== #

