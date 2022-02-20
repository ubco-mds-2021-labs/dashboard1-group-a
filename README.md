#  Energy Usage Dashboard (Group A)

The dashboard created based on a dataset of appliances energy use data in a low energy building. The dashboard will allow users to explore different aspects of the data, like how external factors like temperature, humidity and windspeed contribute to energy consumption. Other factors such as time of day (morning, afternoon, evening) and day of week (weekday,weekend) and sunlight(east/west) can also be explored by users.  We would like to figure out the house climate and energy use in different time period and if there is a relation between the energy consumptions and the factors. 

## Team Members

- Disha DH loves cooking, solo travelling and bagpacking.
- Gavin Grochowski is busy trying to pull the perfect espresso shot.
- Kristy Phipps loves to dance, cuddle puppies and to learn cool new stuff!
- Yilin Sun likes reading and coding but hate leetcode. 

## Describe your topic/interest in about 150-200 words

Designers, engineers, companies, and individuals everywhere are looking for ways to reduce their carbon footprint. A crucial first step in understanding how to reduce to reduce energy waste is understanding common energy usage patterns.  Therefore, we propose creating a dashboard that will facilitate exploring energy usage patterns in a typical 3-bedroom home. 

We are interested in which factors make a difference to house temperature and which climate factors make an impact on energy usage. We want to figure out whether the energy consumption is effected by the factors such as temperature and humidity. We are interested in if the consumption of energy has big variance in different hours in a day. In addition, we are curious about some relevant topics such as if the type of room make a meaningful difference to room temperature and humidity and the windspeed make an impact on energy usage. 

This dashboard is primarily designed for engineers interested in creating energy efficient homes. However, this dashboard could also be useful as an educational tool for savvy individuals looking to find ways to reduce energy consumption in their homes. 



## About this Dashboard

Currently we have decided that the dashboard will have two tabs. The first tab will contain information about the house climate. We will be using this tab to know the variations in humidity and temperature within the house. The user can compare the conditions between multiple rooms at once. The first dropdown box is used to select the type of room which is frequently and less frequently used rooms. The next component which will be a radio button is used to select two or more types of rooms. We will have 4 different time scales which can be Full (For all the 5 months), Daily, Weekly and Monthly. We will also include a slider which will be used to select the date range. The result plot will show the varying changes of temperature and humidity across the house in the specified time range. 

The second tab is about energy use. It also has the comparison factor dropdown box.  The second checkbox is used to choose the level of humidity. The third and the fiurth component is used to choose the timescale and date range. The resulting plot will show the energy consumed by lights and appliances in the house for varying levels of conditions specified and the time range specified. It also shows the total energy consumption separately and its relationship with the factor. Below we will include a plot which shows how the selected factor changes over time within the specified range.


<img src ="assets/sketch_tab1.png" width="500px">
<img src ="assets/sketch_tab2.png" width="500px">



## Describe your dataset in about 150-200 words

* The data set was donated in the year 2017 by Luis Candanedo, University of Mons (UMONS). The data was collected to create regression models of appliances energy use in a low energy building.
* Each appliance in the house were attached with a sensor node and the temperature and the humidity was recorded every 3.3 minutes. The average of these temperature was recorded for every 10 minutes.
* The data was collected in the year 2016, January 11th to May 27th.
* The outside temperatures were also recorded to check the appliances energy use in low energy buildings.
* The data was divided into training and testing set to perform regression models to reduce the MSE of the model to predict the energy use by an appliance.

## Acknowledgements and references 

Dataset link: http://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction