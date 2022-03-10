import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import TAB1_DROPDOWN,time_scale,date_slider,tab1_selector
from data.data import temperature_df_full


SIDEBAR1 = [dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px","padding-left": "10px","padding-top": "10px"}),
dbc.Row("___________________________________________"),
html.Br(),
dbc.Row("This dashboard figure out which factors make a difference to house temperature and humidity. You can choose the factors from the dropdown below.",class_name="description"),
html.Br(),
dbc.Label("Compare Across:",class_name="sub_title",style={"font-size":"20px"}),
html.Br(),
dbc.Row(TAB1_DROPDOWN),
html.Br(),
dbc.Row(tab1_selector),
html.Br(),
dbc.Row(time_scale),
html.Br(),
dbc.Row(date_slider),
]


@app.callback(
    Output('selection_tab1', 'options'),
    Input('tab1_dropdown', 'value'))
def set_checkbox(tab1_dropdown):
    if tab1_dropdown==1:
        return [{'label': i, 'value': i} for i in temperature_df_full['room_type'].unique()]
    elif tab1_dropdown==2:
        return [{'label': i, 'value': i} for i in temperature_df_full['direction'].unique()]
    elif tab1_dropdown==3:
        return [{'label': i, 'value': i} for i in temperature_df_full['floor'].unique()]
    elif tab1_dropdown==4:
        return [{'label': i, 'value': i} for i in temperature_df_full['time_of_day'].unique()]
