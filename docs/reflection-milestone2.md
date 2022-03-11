
*For milestone 2, we have created the framework and base components of our dashboard to examine factors impacting energy and temperature of a European house through the year.*

**KNOWN HEROKU BUG:** Small jitters and frusteration in trying to switch from one tab to the other, despite working as expected locally. 

**Workaround:** Click multiple times on the tab you intend to switch to.

# Features Implemented
Our dashboard is spread across a sidebar and 2 tabs of content.

### Sidebar

* Sidebar updates dynamically in place based on selected tab.
* Dropdown 'compare' values in sidebar update based on the data being used in that tap.
* Multiselect 'include' values in sidebar update dynamically based on the Dropdown 'compare' values selected.
* 'Timescale' radio select features options to aggregate the data to see patterns in time-groups.
* Date Range and Date picker implemented (but not yet linked to data with callbacks)

### Tab 1
* Tab 1 Visualizations of Temperature and Humidity against time.
* Figures dynamically interact with dropdown category selection.
* Displayed categories dynamically interact with sidebar multi-select.
* Displayed figures update dynamically with timescale selected.
### Tab 2
* Energy use visualization created (statically).
* Time series visualization with sidebar dropdown integration for variable selection.

# Features Not Yet Implemented

* Bug fix for switching tabs on Heroku.
* App styling and formatting not yet tidied and formalized. Appearance is still a rough draft, not a final product.
* Tab 2 may end up adding another visualization in our final dashboard to compare dropdown items.
* "Date Range" slider and date picker not yet connected to vizualizations in first or second tab.