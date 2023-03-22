import dash
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from components import home

# ================== Layout do Modal novo Material ===========================
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Novo Material')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.H5('Código:'),
                dbc.Input(id = 'codigo_material')
            ], sm = 12, md = 4, style = {'paddingRight': '30px'}),
            dbc.Col([
                html.H5('Tipo:'),
                dcc.Dropdown([],id = 'tipo_material')
            ], sm = 12, md = 4, style = {'paddingRight': '30px'}),
            dbc.Col([
                html.H5('Descrição:'),
                dbc.Input(id = 'descricao_material')
            ], sm = 12, md = 4)
        ]),
        dbc.Row([
            dbc.Col([
                html.H5('Unidade:'),
                dcc.Dropdown([], id = 'unidade_material')
            ], sm = 12, md = 5, style = {'paddingRight': '30px'}),
            dbc.Col([
                html.H5('Preço:'),
                dbc.Input(id = 'preco_material', type = 'number', step = 0.01)
            ], sm = 12, md = 5, style = {'paddingRight': '30px'})
        ], style = {'marginTop': '30px', 'marginBottom': '30px'})
    
    ]),
    dbc.ModalFooter([
        dbc.Col([
            dbc.Button('Salvar', id = 'botao_salvar_material', color = 'success')
        ]),
        dbc.Col([
            html.H5(id = 'mensagem_sucesso_salvar_material')
        ])
    ])

], id = 'modal_novo_material', size = 'lg', is_open = False)



# ================== Callbacks do Modal novo Material ===========================
@app.callback(
    Output('store_material', 'data'),
    Output('mensagem_sucesso_salvar_material', 'children'),
    Input('botao_salvar_material', 'n_clicks'),
    State('store_material', 'data'),
    State('codigo_material', 'value'),
    State('tipo_material', 'value'),
    State('descricao_material', 'value'),
    State('unidade_material', 'value'),
    State('preco_material', 'value')
)
def cadastra_material(n, dataset, codigo, tipo, descricao, unidade, preco):
    erro = []
    if n:
        if None in [codigo, tipo, descricao, unidade, preco]:
            return dataset, ['Insira todos dados necessários.']
        
        df_material = pd.DataFrame(dataset)

        if codigo in df_material['Codigo'].values:
            return dataset, [f'Código {codigo} já cadastrado.']
        if descricao in df_material['Descricao'].values:
            return dataset, [f'Descrição {descricao} já utilizada.']
        
        df_material.loc[df_material.shape[0]] = [codigo, tipo, descricao, unidade, preco]
        dataset = df_material.to_dict()

        return dataset, ['Material Cadastrado com Sucesso!']
    return dataset, erro

        