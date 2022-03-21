import dash
from dash import dcc
from dash import html,Input, Output
import dash_bootstrap_components as dbc
from ..app import app
from .sidebar_function_tab2 import TAB2_DROPDOWN,tab2_selector,date_picker,choice
from data.data import energy_df_full
from .style import title_style,description_style,sub_title_style,line_style

SIDEBAR2 = [dbc.Row("Energy Dashboard",style=title_style),
dbc.Row("___________________________________________",style = line_style),
html.Br(),
dbc.Row("This part of the dashboard explores energy usage over time in the home. You can choose date range from the dropdown below. You can also explore what the weather was doing during the same time frame using the Climate Factor dropdown. ",class_name="description"),
html.Br(),
dbc.Label("Choose Date Range:",style=sub_title_style),
html.Br(),
dbc.Row(date_picker),
html.Br(),
dbc.Label("Choose Climate Factor:",style=sub_title_style),
html.Br(),
dbc.Row(choice),
# html.Br(),
# dbc.Row(TAB2_DROPDOWN),
# html.Br(),
# dbc.Row(tab2_selector),



]



# @app.callback(
#     Output('selection_tab2', 'options'),
#     Input('tab2_dropdown', 'value'))
# def set_checkbox2(tab2_dropdown):
#     if tab2_dropdown==1:
#         return [{'label': i, 'value': i} for i in energy_df_full['outside_humidity_status'].unique()]
#     elif tab2_dropdown==2:
#         return [{'label': i, 'value': i} for i in energy_df_full['outside_temperature_status'].unique()]
#     elif tab2_dropdown==3:
#         return [{'label': i, 'value': i} for i in energy_df_full['windspeed_status'].unique()]
