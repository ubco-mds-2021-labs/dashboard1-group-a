from dash import dcc
from dash import Input, Output, html
import dash_bootstrap_components as dbc
from data.data import temperature_df_full
import altair as alt
from ..app import app
from .style import plot_style_tab1,whole_tab_style,label_style_active,label_style_init
alt.data_transformers.disable_max_rows()


def plot1_altair(temperature_df_full, xcol="Day of Week", cat_compare="Room Type"):
    #Changing the plot for hour_of_day and Daytime/Nighttime
    if (xcol=="Hour of Day") and (cat_compare=="Time of Day"):
        chart1 = (
            alt.Chart(temperature_df_full,title="The average of Temperature of the selected rooms is plotted with the selected time range").mark_boxplot()
            .encode(x="Hour of Day",y="mean(Temperature (C))", color="Time of Day").properties(height=250,width=800)
            .interactive()
        )
        return chart1.to_html()

    # Filter data based on needed columns to reduce memory.
    necessary_cols = ["Temperature (C)"]
    necessary_cols.append(xcol)
    necessary_cols.append(cat_compare)
    temperature_df_filtered = temperature_df_full[necessary_cols]

    chart1 = (
        alt.Chart(temperature_df_filtered,title="The average of Temperature of the selected rooms is plotted with the selected time range")
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
                ],axis=alt.Axis(grid=False),
            ),
            y="mean(Temperature (C))",
            color=cat_compare,
        )
        .properties(height=250, width=800)
        .interactive()
    )
    return chart1.to_html()


def plot2_altair(temperature_df_full, xcol="Day of Week", cat_compare="Room Type"):
    #Changing the plot for hour_of_day and Daytime/Nighttime
    if (xcol=="Hour of Day") and (cat_compare=="Time of Day"):
        chart1 = (
            alt.Chart(temperature_df_full,title="The average of Relative Humidity of the selected rooms is plotted with the selected time range").mark_boxplot()
            .encode(x="Hour of Day",y="mean(Relative Humidity (%))", color="Time of Day").properties(height=250,width=800)
            .interactive()
        )
        return chart1.to_html()

    # Filter data based on needed columns to reduce memory.
    necessary_cols = ["Relative Humidity (%)"]
    necessary_cols.append(xcol)
    necessary_cols.append(cat_compare)
    temperature_df_filtered = temperature_df_full[necessary_cols]

    chart2 = (
        alt.Chart(temperature_df_filtered,title="The average of Relative Humidity of the selected rooms is plotted with the selected time range")
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
                ], axis=alt.Axis(grid=False),
            ),
            y="mean(Relative Humidity (%))",
            color=cat_compare,
        )
        .properties(height=250, width=800)
        .interactive()
    )
    return chart2.to_html()


plot1 = html.Iframe(
    id="plot1",
    srcDoc=plot1_altair(temperature_df_full, xcol="Date"),
    style=plot_style_tab1,
)
plot2 = html.Iframe(
    id="plot2",
    srcDoc=plot2_altair(temperature_df_full, xcol="Date"),
    style=plot_style_tab1,
)


TAB1 = dbc.Tab(
    tab_id="tab-0",
    label="House Climate",
    label_style = label_style_init,
    active_label_style=label_style_active,
    children=[
        plot1,
        plot2,
    ],
    style =whole_tab_style,
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
        a = "Hour of Day"
    return plot1_altair(df1, a, cat_compare), plot2_altair(df1, a, cat_compare)


if __name__ == "__main__":
    app.run_server(debug=True)
