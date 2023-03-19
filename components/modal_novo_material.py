import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from components import home

layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Novo Material')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                
            ], sm = 12, md = 6)
        ])
    
    ])

], id = 'modal_novo_material', size = 'sm', is_open = False)