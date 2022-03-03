from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .sidebar_function_tab1 import TAB1_DROPDOWN,room_selector,time_scale,date_slider


SIDEBAR = dbc.Col(md=3, style={'backgroundColor':'black','color':'white'},children=[dbc.Row("Energy Dashboard",style={"font-size":"30px"}),
dbc.Row("___________________________________________"),
dbc.Row("Add description here"),

dbc.Label("Compare Across:",style={"font-size":"20px"}),
dbc.Row(TAB1_DROPDOWN),

dbc.Row(room_selector),
dbc.Row(time_scale),
dbc.Row(date_slider),



],
)
