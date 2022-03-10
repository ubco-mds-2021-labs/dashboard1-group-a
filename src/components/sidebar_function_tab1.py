from dash import dcc
from dash import Input, Output,html
import dash_bootstrap_components as dbc
from ..app import app





TAB1_DROPDOWN = dcc.Dropdown(
    id="tab1_dropdown",
    options=[
        {"label": "Room Type", "value":1},
        {"label": "Sun light", "value": 2},
        {"label": "Floor of House", "value": 3},
        {"label": "Daytime/Nightime", "value": 4},
    ],
    value=1,
    style={'color':'blue'},

)

tab1_selector = html.Div(
    [
        dbc.Label("Include:",class_name="sub_title"),
        dbc.Checklist(
            id="selection_tab1",
            options=[
                {"label": "Bedroom", "value": "Bedroom"},
                {"label": "Functional Space", "value": "Functional Space"},
                {"label": "Living Area", "value": "Living Area"},
                {"label": "Outside", "value": "Outside"}
            ],
            value=['Functional Space'],

            inline=False,
        ),
    ],
    className="mb-2",
)





time_scale= html.Div(
    [
        dbc.Label("Timescale:",class_name="sub_title"),
        dbc.RadioItems(
            id="time_scale",
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


date_slider = html.Div(
    [
        dbc.Label("Date Range:",class_name="sub_title"),

        dcc.RangeSlider(
        id='date-range-slider',
        min=0,
        max=10,
        marks = None
    ),
    ],
    className="mb-2",

)
