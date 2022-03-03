import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import TAB1_DROPDOWN,time_scale,date_slider,choose_fun


SIDEBAR = dbc.Col(md=3, style={'backgroundColor':'black','color':'white'},children=[dbc.Row("Energy Dashboard",style={"font-size":"30px"}),
dbc.Row("___________________________________________"),
dbc.Row("Add description here"),

dbc.Label("Compare Across:",style={"font-size":"20px"}),
dbc.Row(TAB1_DROPDOWN),
dbc.Row(id="selection"),
dbc.Row(time_scale),
dbc.Row(date_slider),
],
)

@app.callback(Output("selection", "children"), [Input("tab1-dropdown", "value")])
def output_div(value):
    return choose_fun(value)
