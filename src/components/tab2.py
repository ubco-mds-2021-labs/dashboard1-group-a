from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import altair as alt
from dash.dependencies import Input, Output

from data.data import energy_df_full
from ..app import app
from .style import plot_style_tab2,title_style_tab2

alt.data_transformers.disable_max_rows()


# Plots
def energy_plot(start_date = "2016-01-12", end_date = "2016-01-19"):
    # Filtering values
    necessary_cols = [
        "Date",
        "Energy Use - Appliances (Wh)",
        "Energy Use - Lights (Wh)",
    ]

    # Apply Filters
    energy_df_filtered = energy_df_full[necessary_cols]
    mask = (energy_df_filtered["Date"] > start_date) & (
        energy_df_filtered["Date"] <= end_date
    )
    energy_df_filtered = energy_df_filtered[mask]

    chart1a = (
        alt.Chart(energy_df_filtered)
        .transform_fold(
            ["Energy Use - Appliances (Wh)", "Energy Use - Lights (Wh)"],
            as_=["total", "value"],
        )
        .mark_bar()
        .encode(
            alt.X("Date:T", axis=alt.Axis(title="Elapsed Time")),
            alt.Y("value:Q", axis=alt.Axis(title="Energy Usage in wH")),
            color="total:N",
        )
        .properties(height=300, width=700)
    )
    return chart1a.to_html()


def weather_plot(start_date = "2016-01-12", end_date = "2016-01-19", ycol="Temperature Outside (C)"):
    # Filtering values
    necessary_cols = ["Date"]
    necessary_cols.append(ycol)

    # Apply Filters
    energy_df_filtered = energy_df_full[necessary_cols]
    mask = (energy_df_filtered["Date"] > start_date) & (
        energy_df_filtered["Date"] <= end_date
    )
    energy_df_filtered = energy_df_full[mask]

    chart1b = (
        alt.Chart(energy_df_filtered)
        .mark_line(color="firebrick")
        .encode(alt.X("Date:T", axis=alt.Axis(title="Elapsed Time")), y=ycol)
        .properties(height=200, width=700)
    )
    return chart1b.to_html()


plot1a = html.Iframe(
    id="plot1a",
    srcDoc=energy_plot(),
    style=plot_style_tab2,
)
plot1b = html.Iframe(
    id="plot1b",
    srcDoc=weather_plot(ycol="Temperature Outside (C)"),
    style=plot_style_tab2,
)


TAB2 = dbc.Tab(
    label="Energy Usage",
    tab_id="tab-1",
    children=[
        dbc.Row("Total Energy Usage over Time",style=title_style_tab2),
        plot1a,
        dbc.Row("Climate Factor over Time",style =title_style_tab2),
        plot1b,
    ],
)

## Callback functions
@app.callback(
    Output("plot1a", "srcDoc"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
)
def update_plot1a(start_date, end_date):
    return energy_plot(start_date,end_date)

@app.callback(
    Output("plot1b", "srcDoc"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input("chart_dropdown", "value")
)
def update_plot1b(start_date, end_date, ycol):
    return weather_plot(start_date, end_date, ycol)


if __name__ == "__main__":
    app.run_server(debug=True)
