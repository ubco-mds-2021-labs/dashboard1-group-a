from dash import dcc
from dash import Input, Output, html
import dash_bootstrap_components as dbc
from data.data import temperature_df_full
import altair as alt
from ..app import app

alt.data_transformers.disable_max_rows()


def plot1_altair(temperature_df_full, xcol="Day of Week", cat_compare="Room Type"):

    # Filter data based on needed columns to reduce memory.
    necessary_cols = ["Temperature (C)"]
    necessary_cols.append(xcol)
    necessary_cols.append(cat_compare)
    temperature_df_filtered = temperature_df_full[necessary_cols]

    chart1 = (
        alt.Chart(temperature_df_filtered)
        .mark_line()
        .encode(
            x=alt.X(
                xcol,
                sort=[
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ],
            ),
            y="mean(Temperature (C))",
            color=cat_compare,
        )
        .properties(height=200, width=800)
    )
    return chart1.to_html()


def plot2_altair(temperature_df_full, xcol="Day of Week", cat_compare="Room Type"):

    # Filter data based on needed columns to reduce memory.
    necessary_cols = ["Relative Humidity (%)"]
    necessary_cols.append(xcol)
    necessary_cols.append(cat_compare)
    temperature_df_filtered = temperature_df_full[necessary_cols]

    chart2 = (
        alt.Chart(temperature_df_filtered)
        .mark_line()
        .encode(
            x=alt.X(
                xcol,
                sort=[
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ],
            ),
            y="mean(Relative Humidity (%))",
            color=cat_compare,
        )
        .properties(height=200, width=800)
    )
    return chart2.to_html()


plot1 = html.Iframe(
    id="plot1",
    srcDoc=plot1_altair(temperature_df_full, xcol="Date"),
    style={"width": "100%", "height": "400px"},
)
plot2 = html.Iframe(
    id="plot2",
    srcDoc=plot2_altair(temperature_df_full, xcol="Date"),
    style={"width": "100%", "height": "400px"},
)


TAB1 = dbc.Tab(
    tab_id="tab-0",
    label="House Climate",
    children=[
        "The average of Temperature of the selected rooms is plotted with the selected time range",
        plot1,
        "The average of Relative Humidity of the selected rooms is plotted with the selected time range",
        plot2,
    ],
)


@app.callback(
    Output("plot1", "srcDoc"),
    Output("plot2", "srcDoc"),
    Input("tab1_dropdown", "value"),
    Input("selection_tab1", "value"),
    Input("time_scale", "value"),
)
def update_plot(tab1_dropdown, selection_tab1, time_scale):
    if tab1_dropdown == 1:
        cat_compare = "Room Type"
    elif tab1_dropdown == 2:
        cat_compare = "Direction"
    elif tab1_dropdown == 3:
        cat_compare = "Floor"
    else:
        cat_compare = "Time of Day"
    df1 = temperature_df_full[temperature_df_full[cat_compare].isin(selection_tab1)]
    if time_scale == "full":
        a = "Date"
    elif time_scale == "month":
        a = "Month"
    elif time_scale == "daily":
        a = "Day of Week"
    else:
        a = "hour_of_day"
    return plot1_altair(df1, a, cat_compare), plot2_altair(df1, a, cat_compare)


if __name__ == "__main__":
    app.run_server(debug=True)
