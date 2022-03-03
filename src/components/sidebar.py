import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import TAB1_DROPDOWN,time_scale,date_slider,choose_fun_tab1


SIDEBAR = dbc.Col(md=3,class_name="bar",style={'backgroundColor':'black','color':'white'},children=[dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px"}),
dbc.Row("___________________________________________"),
dbc.Row("Add description here",class_name="description"),

dbc.Label("Compare Across:",class_name="sub_title",style={"font-size":"20px"}),
dbc.Row(TAB1_DROPDOWN),
dbc.Row(id="selection_tab1"),
dbc.Row(time_scale),
dbc.Row(date_slider),
],
)

@app.callback(Output("selection_tab1", "children"), [Input("tab1-dropdown", "value")])
def output_div(value):
    return choose_fun_tab1(value)
