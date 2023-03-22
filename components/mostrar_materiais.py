import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from components import home

# ============== Layout ==================
layout = dbc.Modal([
    dbc.ModalHeader([dbc.ModalTitle('Materiais Cadastrados')]),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.Div(id = 'tabela_materiais', className='dbc')
            ])
        ])
    ])
])