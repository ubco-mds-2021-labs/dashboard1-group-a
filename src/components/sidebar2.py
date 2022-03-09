import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab2 import TAB2_DROPDOWN,tab2_selector,time_scale_2,date_slider_2
from data.data import energy_df_full

SIDEBAR2 = [dbc.Row("Energy Dashboard",class_name="title",style={"font-size":"30px","padding-left": "10px","padding-top": "10px"}),
dbc.Row("___________________________________________"),
html.Br(),
dbc.Row("This dashboard figure out which climate factors make an impact on energy usage. You can choose the factors from the dropdown below.",class_name="description"),
html.Br(),
dbc.Label("Compare Across:",class_name="sub_title_2",style={"font-size":"20px"}),
html.Br(),
dbc.Row(TAB2_DROPDOWN),
html.Br(),
dbc.Row(tab2_selector),
html.Br(),
dbc.Row(time_scale_2),
html.Br(),
dbc.Row(date_slider_2),
]



@app.callback(
    Output('selection_tab2', 'options'),
    Input('tab2_dropdown', 'value'))
def set_checkbox2(tab2_dropdown):
    if tab2_dropdown==1:
        return [{'label': i, 'value': i} for i in energy_df_full['outside_humidity_status'].unique()]
    elif tab2_dropdown==2:
        return [{'label': i, 'value': i} for i in energy_df_full['outside_temperature_status'].unique()]
    elif tab2_dropdown==3:
        return [{'label': i, 'value': i} for i in energy_df_full['windspeed_status'].unique()]
