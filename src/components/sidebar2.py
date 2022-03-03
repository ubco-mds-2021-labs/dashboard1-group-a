import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import time_scale,date_slider
from .sidebar_function_tab2 import TAB2_DROPDOWN,choose_fun_tab2

SIDEBAR2 = dbc.Col(md=3,class_name="bar",style={'backgroundColor':'black','color':'white'},children=[dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px"}),
dbc.Row("___________________________________________"),
dbc.Row("Add description here",class_name="description"),

dbc.Label("Compare Across:",class_name="sub_title",style={"font-size":"20px"}),
dbc.Row(TAB2_DROPDOWN),
dbc.Row(id="selection_tab2"),
dbc.Row(time_scale),
dbc.Row(date_slider),
],
)

@app.callback(Output("selection_tab2", "children"), [Input("tab2-dropdown", "value")])
def output_div(value):
    return choose_fun_tab2(value)
