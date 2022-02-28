from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .example_slider import EXAMPLE_SLIDER

TAB1 = dbc.Tab(label="Tab 1", children=["Tab 1 Content", EXAMPLE_SLIDER])
