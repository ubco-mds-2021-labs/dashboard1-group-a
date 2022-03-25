Our dashboard investigates different  the weather conditions with the energy consumption patterns of a European house.

# Features Implemented
We have two tabs in the dashboard with a sidebar and a variety of plots in each tab. 

### Sidebar

* The sidebar is linked to the plots and allows the plot to be updated dynamically.
* Dropdown 'compare' values in sidebar update based on the data being used in that tap.
* The multi select is removed in the R version of this dashboard as this feature is built in in R and we can select the required legends instead.
* 'Averaged By' radio select features options to aggregate the data to see patterns in time-groups.
* 'Date Range' date picker allows users to filter data on visualizations.

### Tab 1
* Tab 1 has visualizations of average of Temperature and Humidity against time.
* Figures dynamically interact with dropdown category selection.
* Displayed figures update dynamically with timescale selected.


### Tab 2
* Energy use visualizations aggregated by day-of-week and hour-of-day.
* Time series visualizations to compare energy use with sidebar-selected variable.
* Plots updated with data range selected in date pickers.

# Features Not Yet Implemented
* Initially we planned on including a floor plan of the house from the dataset for clarity in storytelling. However, we decided that most of our visualizations do not rely on the floor plan, and we did not want to clutter up the tab.

---

# Reflections on implementing feedback 
* As we recieved no major TA or professor feedback, we were able to move forward with small improvements to our existing dashboard to prepare for milestone 4.
* In general our app has been easy to use, and the main persistent bug that users experienced (a frusterating "sticky" tab selection) was a result of Heroku and Dash interacting strangely, not our code. This problem disappeared in later releases.
* It was extremely helpful to recieve peer feedback on user experience. Watching peers use the dashboard for the first time informed us what sort of language was clear and what sort of language caused friction in use. As a result, we were able to optimize our language to be clear and non-distracting while using the dashboard.
