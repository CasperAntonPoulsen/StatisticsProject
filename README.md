# Predicting energy production of windmills using weather forecasts

This project proposes a method of modelling weather forecast data with the express purpose of predicting the amount of energy produced by windmills. We will be using energy data from windmills located in Orkney, Scotland aswell as weather forecast data from the region, specifying windspeeds and directions at a given timestep. 

The windmills in Orkney are in charge of the majority of the energy production in the region, with over 500 windmills. Orkney being a cluster of islands off of the northern coast of Scotland, are subject to a lot of heavy wind making it an ideal place for windmills. In periods of incredibly strong wind and low local demand for energy, the network of windmills in Orkney produce an excess of energy which can be sold off to energy companies. 

Selling off spare energy is an active descision which requires knowing when excess energy will be generated and when to stop, as to not be subjected to fees and tarifs. This makes the ability to correctly predict when energy generation will be high an important fiscal tool. 

We therefore propose to use a varying array of supervised methods of regression to predict future energy generation. 

## Data Preperation

Before applying any statistical methods, we need to prepare the data for modelling. This is broken down into two distinct tasks. The first task is to transform and normalize the wind data as it has a mixture of data types and the second is to allign the two data sources. 

### Wind data transformation

The wind data has two distinct data points, being the wind speed (numeric) and the wind direction (nominal). This mixture of data types is usually not ideal. We therefore propose transforming the wind data into a 2d vector. The windspeed is the magnitude of the vector and the wind direction will be the direction of the vector. The values of the vector will then be our new data points. 

### Data alignment


