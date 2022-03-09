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

time_scale_2= html.Div(
    [
        dbc.Label("Timescale:",class_name="sub_title"),
        dbc.RadioItems(
            id="time_scale_2",
            options=[

                {"label": "Full", "value": "full"},
                {"label": "Month", "value": "month"},
                {"label": "Day of the week", "value": "daily"},
                {"label": "Hour of the day", "value": "hourly"}
            ],
            value="full",
            inline=False,
        ),
    ],
    className="mb-2",
)


date_slider_2 = html.Div(
    [
        dbc.Label("Date Range:",class_name="sub_title"),

        dcc.RangeSlider(
        id='date-range-slider_2',
        min=0,
        max=10,
        marks = None
    ),
    ],
    className="mb-2",

)
