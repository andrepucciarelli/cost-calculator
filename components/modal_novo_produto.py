import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from components import home

# ================== Layout do Modal novo Produto ===========================
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Crie um Produto')),
    dbc.ModalBody([
    
    ]),
    dbc.ModalFooter([
        dbc.Col([
            dbc.Button('Salvar', id = 'botao_salvar_produto', color = 'success')
        ]),
        dbc.Col([
            html.H5(id = 'mensagem_sucesso_salvar_produto')
        ])
    ])

], id = 'modal_novo_produto', size = 'lg', is_open = True)
