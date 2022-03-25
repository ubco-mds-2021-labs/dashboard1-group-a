import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab1 import TAB1_DROPDOWN,time_scale,date_picker_tab1,tab1_selector
from data.data import temperature_df_full
from .style import title_style,description_style,sub_title_style,line_style


SIDEBAR1 = [dbc.Row("Home Environment",style=title_style),
dbc.Row("___________________________________________",style=line_style),
html.Br(),
dbc.Row("This dashboard figure out which factors make a difference to house temperature and humidity. You can choose the factors from the dropdown below.",style=description_style),
html.Br(),
dbc.Label("Compare Across:",style=sub_title_style),
html.Br(),
dbc.Row(TAB1_DROPDOWN),
html.Br(),
dbc.Row(tab1_selector),
dbc.Row("___________________________________________",style=line_style),
#dbc.Label("Choose Date Range:",style = sub_title_style),
# dbc.Row(date_picker_tab1),
# html.Br(),
dbc.Row(time_scale),
html.Br(),

]


@app.callback(
    Output('selection_tab1', 'options'),
    Input('tab1_dropdown', 'value'))
def set_checkbox(tab1_dropdown):
    if tab1_dropdown==1:
        return [{'label': i, 'value': i} for i in temperature_df_full['Room Type'].unique()]
    elif tab1_dropdown==2:
        return [{'label': i, 'value': i} for i in temperature_df_full['Direction'].unique()]
    elif tab1_dropdown==3:
        return [{'label': i, 'value': i} for i in temperature_df_full['Floor'].unique()]
    elif tab1_dropdown==4:
        return [{'label': i, 'value': i} for i in temperature_df_full['Time of Day'].unique()]
