import pandas as pd
import numpy as np

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from PIL import Image

from static.model.functions import face_detector, Jarvis

# Create a Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([dbc.Row(id='app-title', children=[html.H1(children='Dog Breed Classifier')],
                                style={
                                    'border':'solid',
                                    'textAlign':'center'
                                }),
            html.Div([dbc.Row(id='input-row',
                            children=[
                                    html.Div(id='upload-container',
                                               children=[dcc.Upload(id='upload-img',
                                                                    children=html.Div(id='upload-text',children=['Drag & Drop or ',
                                                                                                                html.A('upload Files*')]),
                                                                    style={
                                                                        'width': '100%',
                                                                        'height': '60px',
                                                                        'lineHeight': '60px',
                                                                        'borderWidth': '1px',
                                                                        'borderStyle': 'dashed',
                                                                        'borderRadius': '5px',
                                                                        'textAlign': 'center',
                                                                        'padding': '10px'},
                                                                    multiple=False)],
                                                ),

                                    html.Div(id='ext-warning',
                                             children=['*Only .jpg or .png files'],
                                             style={
                                                'padding':'25px',
                                                'font-size':'10px'
                                             })],
                            style={
                                'display':'flex',
                                'align-items':'flex-start',
                                'justify-content':'center',
                                'padding':'5px'
                            }),
                            
                    dbc.Row(id='submit-container',
                            children=[html.Button(id='submit-button', 
                                                n_clicks=0, 
                                                children=['Submit'],
                                                  style={
                                                    'width': '10%',
                                                    'height': '60px'
                                                    })],
                            style={
                                'display': 'flex',
                                'justify-content': 'center',
                                'padding': '20px'}),

                    dbc.Row(id='display-row',
                            children=[dbc.Col(id='img-container', children=[],
                                            style={
                                                'display':'flex',
                                                'justify-content':'center'}),
                                      dbc.Col(id='img-label', children=[])],
                            style={
                                'display':'flex',
                                'justify-content':'space-evenly',
                                'align-items':'center',
                                'padding':'5px'
                                }),
                    dbc.Row(id='output-row',
                            children=[],
                            style={
                                'textAlign': 'center',
                                'font-size':'40px'
                            })
            ])
            ])


@app.callback(Output(component_id='img-container', component_property='children'),
              [Input(component_id='upload-img', component_property='contents')])

def display_input_img(contents):
    if contents is not None:
        return html.Img(src=contents, 
                        style={
                            'width': '400px', 
                            'height': 'auto'
                        })
    else:
        return 'No image uploaded'
    

@app.callback(Output(component_id='img-label', component_property='children'),
              [Input(component_id='upload-img', component_property='contents')])

def label_input_img(contents):
    if contents is not None:
        return html.P('Image Received',
                      style={
                          'textAlign': 'center',
                          'font-size': '50px',
                          'color': 'green'})
    else:
        return html.P('Awating Image',
                      style={
                          'textAlign': 'center',
                          'font-size': '50px',
                          'color': 'red'})


@app.callback(Output(component_id='output-row', component_property='children'),
              Input(component_id='upload-img', component_property='contents'),
              Input(component_id='submit-button', component_property='n_clicks')
        
)
def describe_img(contents, n_clicks):
    if (contents is not None) and (n_clicks>0):
        
        sentence = Jarvis(contents)
        
        return sentence
    else:
        return 'Dog Breed'



if __name__ == '__main__':
    app.run_server(debug=True)
