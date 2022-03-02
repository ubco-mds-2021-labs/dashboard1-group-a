from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .example_dropdown import EXAMPLE_DROPDOWN

SIDEBAR = dbc.Col(md=3, children=[dbc.Row("Sidebar"), dbc.Row(EXAMPLE_DROPDOWN)])
