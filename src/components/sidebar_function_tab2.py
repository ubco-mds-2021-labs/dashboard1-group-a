from dash import dcc
from dash import Input, Output,html
import dash_bootstrap_components as dbc
from ..app import app



TAB2_DROPDOWN = dcc.Dropdown(
    id="tab2_dropdown",
    options=[
        {"label": "Outside Humidity", "value":1},
        {"label": "Outside Temperature ", "value": 2},
        {"label": "Windspeed", "value": 3},
    ],
    value = 1,
    style={'color':'blue'},

)

tab2_selector = html.Div(
    [
        dbc.Label("Include:",class_name="sub_title_2"),
        dbc.Checklist(
            id="selection_tab2",
            options=[
                {"label": "Low Humidity", "value": "Low Outside Humidity"},
                {"label": "Mid-low Humidity", "value": "Mid-Low Outside Humidity"},
                {"label": "Mid-high Humidity", "value": "Mid-High Outside Humidity"},
                {"label": "High Humidity", "value": "High Outside Humidity"}
            ],
            value=['Low Outside Humidity'],

            inline=False,
        ),
    ],
    className="mb-2",
)
# humidity_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="humidity_selector",
#             options=[
#                 {"label": "Low Humidity", "value": "low_hum"},
#                 {"label": "Mid-low Humidity", "value": "mid_low_hum"},
#                 {"label": "Mid-high Humidity", "value": "mid_high_hum"},
#                 {"label": "High Humidity", "value": "high_hum"}
#
#             ],
#
#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )
#
# temperature_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="temperature_selector",
#             options=[
#             {"label": "Low Outside Temperature", "value": "low_tem"},
#             {"label": "Mid-low Outside Temperature", "value": "mid_low_tem"},
#             {"label": "Mid-high Outside Temperature", "value": "mid_high_tem"},
#             {"label": "High Outside Temperature", "value": "high_tem"}
#
#
#             ],
#
#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )
#
# wind_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="wind_selector",
#             options=[
#             {"label": "Low Windspeed", "value": "low_wind"},
#             {"label": "Mid-low Windspeed", "value": "mid_low_wind"},
#             {"label": "Mid-high Windspeed", "value": "mid_high_wind"},
#             {"label": "High Windspeed", "value": "high_wind"}
#
#
#
#             ],
#
#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )
