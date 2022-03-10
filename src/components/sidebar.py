import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar1 import SIDEBAR1
from .sidebar2 import SIDEBAR2

SIDEBAR = dbc.Col(id="sidebar",md=3,class_name="bar",style={'backgroundColor':'grey','color':'white'})

@app.callback(Output("sidebar", "children"), Input("tab_selection", "active_tab"))
def output_div(value):

    if value == "tab-0":
        return SIDEBAR1
    if value == "tab-1":
        return SIDEBAR2
