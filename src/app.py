import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Group A Dashboard v0.1",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
