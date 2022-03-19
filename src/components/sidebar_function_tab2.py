from dash import dcc
from dash import Input, Output, html
import dash_bootstrap_components as dbc
from ..app import app
from datetime import date


TAB2_DROPDOWN = dcc.Dropdown(
    id="tab2_dropdown",
    options=[
        {"label": "Outside Humidity", "value": 1},
        {"label": "Outside Temperature ", "value": 2},
        {"label": "Windspeed", "value": 3},
    ],
    value=1,
    style={"color": "blue"},
)

tab2_selector = html.Div(
    [
        dbc.Label("Include:", class_name="sub_title_2"),
        dbc.Checklist(
            id="selection_tab2",
            options=[
                {"label": "Low Humidity", "value": "Low Outside Humidity"},
                {"label": "Mid-low Humidity", "value": "Mid-Low Outside Humidity"},
                {"label": "Mid-high Humidity", "value": "Mid-High Outside Humidity"},
                {"label": "High Humidity", "value": "High Outside Humidity"},
            ],
            value=["Low Outside Humidity"],
            inline=False,
        ),
    ],
    className="mb-2",
)


date_picker = dcc.DatePickerRange(
    id="my-date-picker-range",
    min_date_allowed=date(2016, 1, 12),
    max_date_allowed=date(2016, 5, 26),
    initial_visible_month=date(2016, 1, 12),
    start_date=date(2016, 1, 12),
    end_date=date(2016, 1, 19),
)


weather_list = [
    "Temperature Outside (C)",
    "Humidity Outside (%)",
    "Dewpoint (C)",
    "Air Pressure (mm Hg)",
    "Windspeed (m / s)",
    "Visibility (km)",
]
choice = dcc.Dropdown(
    id="chart_dropdown",
    value="Temperature Outside (C)",
    style={"color": "blue"},
    options=[{"label": i, "value": i} for i in weather_list],
)
