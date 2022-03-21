from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import altair as alt
from dash.dependencies import Input, Output

from data.data import energy_df_full
from ..app import app

alt.data_transformers.disable_max_rows()


# Plots
def energy_plot(start_date = "2016-01-12", end_date = "2016-01-19"):
    # Filtering values
    necessary_cols = [
        "Date",
        "Day of Week", 
        "Hour of Day",
        "Energy Use - Appliances (Wh)",
        "Energy Use - Lights (Wh)",
    ]
    
    # Apply Filters
    energy_df_filtered = energy_df_full[necessary_cols]
    mask = (energy_df_filtered["Date"] > start_date) & (
        energy_df_filtered["Date"] < end_date
    )
    energy_df_filtered = energy_df_filtered[mask]

    ##first chart - layer 1
    AA = alt.Chart(energy_df_filtered, title = "Average Energy Usage by Weekday").mark_bar(color="darkorange").encode(
            alt.X("Day of Week", sort=[ "Monday",
                                        "Tuesday",
                                        "Wednesday",
                                        "Thursday",
                                        "Friday",
                                        "Saturday",
                                        "Sunday",
                                    ],
                  axis=alt.Axis(title="Day of Week")),
            alt.Y("Energy Use - Lights (Wh)", title = ""),
        ).properties(height=200, width=400)
    
    ##first chart - layer 2
    BB = alt.Chart(energy_df_filtered).mark_bar(color="blue").encode(
            alt.X("Day of Week", sort=[ "Monday",
                                        "Tuesday",
                                        "Wednesday",
                                        "Thursday",
                                        "Friday",
                                        "Saturday",
                                        "Sunday",
                                    ]),
            alt.Y("Energy Use - Appliances (Wh)", title = "Energy Usage in Wh"),
        ).properties(height=200, width=400)
    
    #combining layer 1 and layer 2 for first chart
    chart1 = BB + AA
    
    ##second chart - layer 1
    CC = alt.Chart(energy_df_filtered, title = "Average Energy Usage by Hour of Day").mark_line(color="blue").encode(
            alt.X("Hour of Day", axis=alt.Axis(title="Hour of Day"), scale=alt.Scale(domain=[1,23])),
            alt.Y("mean(Energy Use - Appliances (Wh))"),
        ).properties(height=200, width=400)
    
    ## second chart - layer 2
    DD = alt.Chart(energy_df_filtered).mark_line(color="darkorange").encode(
            alt.X("Hour of Day", scale=alt.Scale(domain=[1,23])),
            alt.Y("mean(Energy Use - Lights (Wh))", axis=alt.Axis(title="Energy Usage in Wh")),
        ).properties(height=200, width=400)
    
    #combining layer 1 and layer 2 for secn chart
    chart2 = CC + DD
    
     
    #third chart (original chart)
    chart3 = (
        alt.Chart(energy_df_filtered, title = "Total Energy Usage in the Home by Hour")
        .transform_fold(
            ["Energy Use - Appliances (Wh)", "Energy Use - Lights (Wh)"],
            as_=["total", "value"],
        )
        .mark_bar()
        .encode(
            alt.X("Date:T", axis=alt.Axis(title="Elapsed Time", format="%b %d %I%p", labelOverlap=False, labelAngle=-45)),
            alt.Y("value:Q", axis=alt.Axis(title="Energy Usage in wH")),
            color="total:N",
        )
        .properties(height=200, width=400)
    )
    
    chart1a = alt.vconcat(alt.hconcat(chart1, chart2), chart3.properties(width=870))

    return chart1a.to_html()


def weather_plot(start_date = "2016-01-12", end_date = "2016-01-19", ycol="Temperature Outside (C)"):
    # Filtering values
    necessary_cols = ["Date"]
    necessary_cols.append(ycol)
    
    # Apply Filters
    energy_df_filtered = energy_df_full[necessary_cols]
    mask = (energy_df_filtered["Date"] > start_date) & (
        energy_df_filtered["Date"] < end_date
    )
    energy_df_filtered = energy_df_full[mask]

    chart1b = (
        alt.Chart(energy_df_filtered, title ="Trend of Climate Factor over Time")
        .mark_line(color="firebrick")
        .encode(alt.X("Date:T", axis=alt.Axis(title="Elapsed Time", format="%b %d %I%p", labelOverlap=False, labelAngle=-45)), y=ycol)
        .properties(height=200, width=870)
    )
    return chart1b.to_html()


plot1a = html.Iframe(
    id="plot1a",
    srcDoc=energy_plot(),
    style={"border-width": "10", "width": "100%", "height": "650px"},
)
plot1b = html.Iframe(
    id="plot1b",
    srcDoc=weather_plot(ycol="Temperature Outside (C)"),
    style={"border-width": "0", "width": "100%", "height": "380px"},
)


TAB2 = dbc.Tab(
    label="Energy Usage",
    tab_id="tab-1",
    children=[
        " ",
        plot1a,
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
