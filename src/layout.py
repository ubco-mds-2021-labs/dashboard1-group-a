from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .components.sidebar import SIDEBAR
from .components.tab1 import TAB1
from .components.tab2 import TAB2

LAYOUT = dbc.Container(
    fluid=True,
    children=dbc.Row(
        children=[
            SIDEBAR,
            dbc.Col(
                width={"size": 9, "offset": 3},
                children=dbc.Tabs(
                    children=[TAB1, TAB2], id="tab_selection", active_tab="tab-0"
                ),
            ),
        ]
    ),
)
