from dash import dcc
from dash import Input,Output,html
import dash_bootstrap_components as dbc
from data.data import temperature_df_full
import altair as alt
from ..app import app

alt.data_transformers.enable('data_server')
alt.data_transformers.disable_max_rows()

from .example_slider import EXAMPLE_SLIDER


def plot1_altair(temperature_df_full,xcol="day_of_week",col="room_type"):
    
    chart1=alt.Chart(temperature_df_full).mark_line().encode(
        x=alt.X(xcol,sort=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),
        y='mean(temperature)',
        color=col
        ).properties(height=500,width=500)
    return chart1.to_html()

def plot2_altair(temperature_df_full,xcol="day_of_week",col="room_type"):
    chart2=alt.Chart(temperature_df_full).mark_line().encode(
        x=alt.X(xcol,sort=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']),
        y='mean(humidity)',
        color=col
        ).properties(height=500,width=500)
    return chart2.to_html()

plot1=html.Iframe(id='plot1',srcDoc=plot1_altair(temperature_df_full,xcol="day_of_week",col="room_type"),style={'width': '100%', 'height': '400px'})
plot2=html.Iframe(id='plot2',srcDoc=plot2_altair(temperature_df_full,xcol="day_of_week",col="room_type"),style={'width': '100%', 'height': '400px'})



TAB1 = dbc.Tab(label="House Climate", children=["The average of temperature or the humidity of the selected rooms is plotted with the selected time range", 
                                                plot1,plot2,
                                                EXAMPLE_SLIDER])

@app.callback(
    Output('plot1', 'srcDoc'),
    Output('plot2', 'srcDoc'),
    Input('time_scale', 'value'),
    Input('tab1_dropdown', 'value'),
    Input('room_selector', 'value'))
def update_plot(time_scale,tab1_dropdown,room_selector):
    if time_scale=="full":
        a="workday"
    elif time_scale=="daily":
        a="day_of_week"
    else:
        a="workday"
    if tab1_dropdown==1:
        if room_selector=="bed":
            newdata=temperature_df_full.loc[temperature_df_full["room_type"]=="Bedroom"]
        elif room_selector=="bath":
            newdata=temperature_df_full.loc[temperature_df_full["room_type"]=="Functional Space"]
        else:
            newdata=temperature_df_full.loc[temperature_df_full["room_type"]=="Living Area"]


    elif tab1_dropdown==2:
        b="direction"
    elif tab1_dropdown==3:
        b="floor"
    else:
        b="time_of_day"
    return plot1_altair(newdata,a,b),plot2_altair(newdata,a,b)

if __name__ == '__main__':
    app.run_server(debug=True)
