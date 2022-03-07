import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import time_scale,date_slider
from .sidebar_function_tab2 import TAB2_DROPDOWN,choose_fun_tab2

SIDEBAR2 = dbc.Col(md=3,class_name="bar",style={'backgroundColor':'grey','color':'white'},children=[dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px","padding-left": "10px","padding-top": "10px"}),
dbc.Row("___________________________________________"),
html.Br(),
dbc.Row("This dashboard figure out which climate factors make an impact on energy usage. You can choose the factors from the dropdown below.",class_name="description"),
html.Br(),
dbc.Label("Compare Across:",class_name="sub_title",style={"font-size":"20px"}),
html.Br(),
dbc.Row(TAB2_DROPDOWN),
html.Br(),
dbc.Row(id="selection_tab2"),
html.Br(),
dbc.Row(time_scale),
html.Br(),
dbc.Row(date_slider),
],
)

@app.callback(Output("selection_tab2", "children"), Input("tab2_dropdown", "value"))
def output_div(value):
    return choose_fun_tab2(value)
