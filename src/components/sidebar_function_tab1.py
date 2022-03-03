from dash import dcc
from dash import Input, Output,html
import dash_bootstrap_components as dbc
from ..app import app

TAB1_DROPDOWN = dcc.Dropdown(
    id="tab1-dropdown",
    options=[
        {"label": "Room Type", "value":1},
        {"label": "Sun light", "value": 2},
        {"label": "Floor of House", "value": 3},
        {"label": "Daytime/Nightime", "value": 4},
    ],
    style={'color':'blue'},

)

room_selector = html.Div(
    [
        dbc.Label("Include:"),
        dbc.RadioItems(
            id="room_selector",
            options=[
                {"label": "Bedroom", "value": "bed"},
                {"label": "Bathroom", "value": "bath"},
                {"label": "Kitchen", "value": "kich"}
            ],
            value="bed",
            inline=False,
        ),
    ],
    className="mb-2",
)


time_scale= html.Div(
    [
        dbc.Label("Timescale:"),
        dbc.RadioItems(
            id="time_scale",
            options=[
                {"label": "Full", "value": "full"},
                {"label": "Weekly", "value": "weekly"},
                {"label": "Daily", "value": "daily"},
                {"label": "Hourly", "value": "hourly"}
            ],
            value="full",
            inline=False,
        ),
    ],
    className="mb-2",
)


date_slider = html.Div(
    [
        dbc.Label("Date Range:"),

        dcc.RangeSlider(
        id='date-range-slider',
        min=0,
        max=10,
        marks={
        0: '0%',
        3: '30%',
        5: '50%',
        7: '70%',
        10: '100%'
    },
    value=[3, 7]),
    ],
    className="mb-2",
)
