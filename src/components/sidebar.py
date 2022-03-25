import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar1 import SIDEBAR1
from .sidebar2 import SIDEBAR2
from .style import sidebar_style
SIDEBAR = dbc.Col(id="sidebar",width=3,style=sidebar_style)

@app.callback(Output("sidebar", "children"), Input("tab_selection", "active_tab"))
def output_div(value):

    if value == "tab-0":
        return SIDEBAR1
    if value == "tab-1":
        return SIDEBAR2
