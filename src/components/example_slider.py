from dash import dcc

EXAMPLE_SLIDER = dcc.Slider(
    id="example-slider",
    min=0,
    max=3,
    step=1,
)
