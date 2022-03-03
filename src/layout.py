from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .components.sidebar import SIDEBAR
from .components.sidebar2 import SIDEBAR2
from .components.tab1 import TAB1
from .components.tab2 import TAB2

LAYOUT = dbc.Container(
    fluid=True,
    children=dbc.Row(
        children=[
            SIDEBAR2,
            dbc.Col(
                md=9,
                children=dbc.Tabs(children=[TAB1, TAB2]),
            ),
        ]
    ),
)
