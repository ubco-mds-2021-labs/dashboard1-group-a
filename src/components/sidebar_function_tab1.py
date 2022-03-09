from dash import dcc
from dash import Input, Output,html
import dash_bootstrap_components as dbc
from ..app import app


# # REPLACED WITH DYNAMIC SELECTOR OPTIONS
# def choose_fun_tab1(fun=1):
#     if fun == 1:
#         return room_selector
#     if fun == 2:
#         return sun_light_selector
#     if fun == 3:
#         return floor_selector
#     if fun == 4:
#         return day_night_selector


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


# # INDIVIDUAL COMPONENTS REPLACED WITH DYNAMICLY GENERATED
# # SELECTOR OPTIONS 
# room_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="room_selector",
#             options=[
#                 {"label": "Bedroom", "value": "Bedroom"},
#                 {"label": "Functional Space", "value": "Functional Space"},
#                 {"label": "Living Area", "value": "Living Area"},
#                 {"label": "Outside", "value": "Outside"}
#             ],
#             value=['Functional Space'],

#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )

# sun_light_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="sun_light_selector",
#             options=[
#                 {"label": "East Facing", "value": "East Facing"},
#                 {"label": "West Facing", "value": "West Facing"},
#                 {"label": "Outside", "value": "Outside"}
#             ],

#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )

# floor_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="floor_selector",
#             options=[
#                 {"label": "Ground", "value": "Ground"},
#                 {"label": "Second", "value": "Second"},
#                 {"label": "Outside", "value": "Outside"}

#             ],

#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )

# day_night_selector = html.Div(
#     [
#         dbc.Label("Include:",class_name="sub_title"),
#         dbc.Checklist(
#             id="day_night_selector",
#             options=[
#                 {"label": "Morning", "value": "Morning"},
#                 {"label": "Afternoon", "value": "Afternoon"},
#                 {"label": "Evening", "value": "Evening"},
#                 {"label": "Night", "value": "Night"},

#             ],

#             inline=False,
#         ),
#     ],
#     className="mb-2",
# )


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
