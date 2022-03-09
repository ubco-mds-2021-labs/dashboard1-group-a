from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import altair as alt
import pandas as pd

from data.data import energy_df_full
from ..app import app

alt.data_transformers.enable("data_server")
alt.data_transformers.disable_max_rows()


# Plots
def energy_plot():
    start_date = "2016-01-12"
    end_date = "2016-01-13"
    mask = (energy_df_full["date"] > start_date) & (energy_df_full["date"] <= end_date)
    single_day = energy_df_full[mask]

    chart1a = (
        alt.Chart(single_day)
        .transform_fold(["energy_appliances", "energy_lights"], as_=["total", "value"])
        .mark_bar()
        .encode(
            alt.X("hours(date):T", axis=alt.Axis(title="Elapsed Time")),
            alt.Y("value:Q", axis=alt.Axis(title="Energy Usage in wH")),
            color="total:N",
        )
        .properties(height=300, width=500)
    )
    return chart1a.to_html()


def weather_plot():
    start_date = "2016-01-12"
    end_date = "2016-01-13"
    mask = (energy_df_full["date"] > start_date) & (energy_df_full["date"] <= end_date)
    single_day = energy_df_full[mask]

    chart1b = (
        alt.Chart(single_day)
        .mark_line()
        .encode(
            alt.X("date:T", axis=alt.Axis(title="Elapsed Time")),
            alt.Y("temperature_outside"),
        )
        .properties(height=200, width=500)
    )
    return chart1b.to_html()


plot1a = html.Iframe(
    srcDoc=energy_plot(),
    style={"border-width": "0", "width": "100%", "height": "400px"},
)
plot1b = html.Iframe(
    srcDoc=weather_plot(),
    style={"border-width": "0", "width": "100%", "height": "400px"},
)


TAB2 = dbc.Tab(label="Energy Usage", children=["Tab 2 Content", plot1a, plot1b])

if __name__ == "__main__":
    app.run_server(debug=True)
