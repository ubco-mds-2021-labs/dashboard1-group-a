from dash import dcc
from dash.dependencies import Input, Output

from app import app

EXAMPLE_DROPDOWN = dcc.Dropdown(
    id="example-dropdown",
    options=[
        {"label": "one", "value": 1},
        {"label": "two", "value": 2},
        {"label": "three", "value": 3},
    ],
    placeholder="Example Dropdown Select",
)

# This callback function needs to be imported into the server.py for the app to see it.
@app.callback(Output("example-slider", "value"), Input("example-dropdown", "value"))
def update_example_slider_from_example_dropdown(dropdown_value):
    return dropdown_value
