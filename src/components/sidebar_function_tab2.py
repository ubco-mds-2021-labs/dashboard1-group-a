from dash import dcc
from dash import Input, Output,html
import dash_bootstrap_components as dbc
from ..app import app


def choose_fun_tab2(fun=1):
    if fun == 1:
        return humidity_selector
    if fun == 2:
        return temperature_selector
    if fun == 3:
        return wind_selector


TAB2_DROPDOWN = dcc.Dropdown(
    id="tab2-dropdown",
    options=[
        {"label": "Outside Humidity", "value":1},
        {"label": "Outside Temperature ", "value": 2},
        {"label": "Windspeed", "value": 3},
    ],
    style={'color':'blue'},

)

humidity_selector = html.Div(
    [
        dbc.Label("Include:",class_name="sub_title"),
        dbc.Checklist(
            id="humidity_selector",
            options=[
                {"label": "Low Humidity", "value": "low_hum"},
                {"label": "Mid-low Humidity", "value": "mid_low_hum"},
                {"label": "Mid-high Humidity", "value": "mid_high_hum"},
                {"label": "High Humidity", "value": "high_hum"}

            ],

            inline=False,
        ),
    ],
    className="mb-2",
)

temperature_selector = html.Div(
    [
        dbc.Label("Include:",class_name="sub_title"),
        dbc.Checklist(
            id="temperature_selector",
            options=[
            {"label": "Low Temperature", "value": "low_tem"},
            {"label": "Mid-low Temperature", "value": "mid_low_tem"},
            {"label": "Mid-high Temperature", "value": "mid_high_tem"},
            {"label": "High Temperature", "value": "high_tem"}


            ],

            inline=False,
        ),
    ],
    className="mb-2",
)

wind_selector = html.Div(
    [
        dbc.Label("Include:",class_name="sub_title"),
        dbc.Checklist(
            id="wind_selector",
            options=[
            {"label": "Low Windspeed", "value": "low_wind"},
            {"label": "Mid-low Windspeed", "value": "mid_low_wind"},
            {"label": "Mid-high Windspeed", "value": "mid_high_wind"},
            {"label": "High Windspeed", "value": "high_wind"}



            ],

            inline=False,
        ),
    ],
    className="mb-2",
)
