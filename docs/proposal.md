### Proposal

## Motivation and Purpose

Role: Consultantcy
Target Audience: Engineers designing energy efficient homes

Designers, engineers, companies, and individuals everywhere are looking for ways to reduce their carbon footprint. A crucial first step in understanding how to reduce to reduce energy waste is understanding common energy usage patterns.  Therefore, we propose creating a dashboard that will facilitate exploring energy usage patterns in a typical 3-bedroom home. The dashboard will allow users to explore different aspects of the data, like how external factors like temperature, humidity and windspeed contribute to energy consumption. Other factors such as time of day (morning, afternoon, evening) and day of week (weekday,weekend) and sunlight(east/west) can also be explored by users. This dashboard is primarily designed for engineers interested in creating energy efficient homes. However, this dashboard could also be useful as an educational tool for savvy individuals looking to find ways to reduce energy consumption in thier homes. 

## Data Description

The dataset being used to build this dashboard is comprised of nearly 20,000 observations made across a 4.5-month time period. Each observation represents a 10-minute time interval and records the appliance and lights energy usage in watt-hours (Wh) for the entire home in that interval. Each interval also includes measurements of temperature and relative humidity in each of the rooms in the home. Weather data was collected from the nearest airport weather station (including temperature, relative humidity, pressure, windspeed, visibility and dewpoint) and was added into the dataset to help understand how external weather conditions contribute to energy consumption in the home. Additionally, some new variables were derived from the base dataset to help explore whether energy consumption habits vary by day of week, as well as during the week versus weekends.

## Research Questions

Which factors make a difference to house temperature?

* Does sunlight (eg. east vs west) make a meaningful difference to room temperature? Humidity?
* Does floor-of-house (eg. ground or second floor) make a meaningful difference to room temperature? Humidity?
* Does Daytime / Nightime make a meaningful difference to room temperature? Humidity?
* Does the type of the room (bedroom, kitchen) make a meaningful difference to room temperature? Humidity?

Which climate factors make an impact on energy usage?

* Does time of day (morning, afternoon, evening) make an impact to energy usage?  
* Does day of week (weekday, weekend) make an impact to energy usage?  
* Does outside humidity make an impact to energy usage?  
* Does outside temperature make an impact to energy usage?
* Does windspeed make and impact on energy usage?

## Usage Scenario

Collin leads a team of engineers who focus on developing technologies that reduce energy waste. He is interested in understanding typical consumer energy consumption patterns to inform product development. Ultimately, his team intends to build a fully integrated smart home as a proof of concept, where the lights, individual appliances and even the building itself can work in harmony to reduce energy consumption. When Collin and his team use the dashboard, they are able to quickly see energy usage patterns on a daily, weekly and monthly scales and how external weather factors contribute to energy consumption. Collin and his team discover that appliance energy usage peaks in the evenings during the week, and overall energy consumption is higher on weekends as consumers are home and using more appliances and lights. Using this information, Collin and his team decide to explore integrated appliance automation in the home. Thier thinking is that during peak usage, one potential way to reduce energy consumption would be to recognise when heat generating appliances like a stove or dryer are in use, the furnace could be turned down to offset the energy usage while maintaining the temperature in that room and surrounding areas. To test this further, Collin and his team request further data that explores appliance and light usage on a room by room basis in the home. A follow-up study is needed as that granular information is not captured in the current data set. 
