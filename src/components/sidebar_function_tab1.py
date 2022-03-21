from dash import dcc
from dash import Input, Output, html
import dash_bootstrap_components as dbc
from ..app import app
from datetime import date
from .style import dropdown_style,sub_title_style,checklist_style,time_scale_style,date_picker_style

TAB1_DROPDOWN = dcc.Dropdown(
    id="tab1_dropdown",
    options=[
        {"label": "Room Type", "value": 1},
        {"label": "Sun light", "value": 2},
        {"label": "Floor of House", "value": 3},
        {"label": "Daytime/Nightime", "value": 4},
    ],
    value=1,
    style=dropdown_style,
)

tab1_selector = html.Div(
    [
        dbc.Label("Include:", style=sub_title_style),
        dbc.Checklist(
            id="selection_tab1",
            options=[
                {"label": "Bedroom", "value": "Bedroom"},
                {"label": "Functional Space", "value": "Functional Space"},
                {"label": "Living Area", "value": "Living Area"},
                {"label": "Outside", "value": "Outside"},
            ],
            # Include ALL options to set default graph to full lines.
            # This also matches the initial page load for our data visualizations,
            # as we only filter out options on callback update (which takes
            # a second or two once the page loads).
            value=[
                "Functional Space",
                "Living Area",
                "Outside",
                "Bedroom",
                "West Facing",
                "East Facing",
                "Outside",
                "Ground Floor",
                "Second Floor",
                "Afternoon",
                "Evening",
                "Night",
                "Morning",
            ],
            inline=False,
            style = checklist_style,
        ),
    ],
)


time_scale = html.Div(
    [
        dbc.Label("Averaged By:", style = sub_title_style),
        dbc.RadioItems(
            id="time_scale",
            options=[
                {"label": "No Average (Raw Data)", "value": "full"},
                {"label": "Month of year", "value": "month"},
                {"label": "Day of week", "value": "daily"},
                {"label": "Hour of day", "value": "hourly"},
            ],
            value="full",
            inline=False,
            style = time_scale_style,
        ),
    ],
)


date_picker_tab1 = dcc.DatePickerRange(
    id="date_picker_tab1",
    min_date_allowed=date(2016, 1, 12),
    max_date_allowed=date(2016, 5, 27),
    initial_visible_month=date(2016, 1, 12),
    start_date=date(2016, 1, 12),
    end_date=date(2016, 5, 27),
    style = date_picker_style,
)
