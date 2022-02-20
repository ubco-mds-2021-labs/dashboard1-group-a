#  Energy Usage Dashboard (Group A)

The dashboard created based on a dataset of appliances energy use data in a low energy building. The dashboard will allow users to explore different aspects of the data, like how external factors like temperature, humidity and windspeed contribute to energy consumption. Other factors such as time of day (morning, afternoon, evening) and day of week (weekday,weekend) and sunlight(east/west) can also be explored by users.  We would like to figure out the house climate and energy use in different time period and if there is a relation between the energy consumptions and the factors. 

## Team Members

- Disha DH loves cooking, solo travelling and bagpacking.
- Gavin Grochowski is busy trying to pull the perfect espresso shot.
- Kristy Phipps loves to dance, cuddle puppies and to learn cool new stuff!
- Yilin Sun likes reading and coding but hate leetcode. 

## Describe your topic/interest in about 150-200 words

We are interested in which factors make a difference to house temperature and which climate factors make an impact on energy usage. We want to figure out whether the energy consumption is effected by the factors such as temperature and humidity. We are interested in if the consumption of energy has big variance in different hours in a day. In addition, we are curious about some relevant topics such as if the type of room make a meaningful difference to room temperature and humidity and the windspeed make an impact on energy usage.  


## About this Dashboard

The dashboard has 2 tabs. The first tab is about house climate. The user can choose the comparison factors from the dropdown box and choose the timescale for the plot. In addition, the user can change the date range using the filter bar. The result plot will show the relation between the factors and the temperature/humidity in the house.

The second tab is about energy use. It also has the comparison factor dropdown box and the user can choose the timescale and date range. The result plot will show the lighting energy consumption, appliance consumption and total consumption separately and its relation with the factor. Also there is a plot of the factors changing with date on energy consumption in the tab.

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