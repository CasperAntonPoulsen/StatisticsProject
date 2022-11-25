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

The energy data has 2 data points, a timestamp and the energy produced in the past hour. The energy data has no missing values and one time step is one hour

The weather forecast data has 4 data points, a timestamp, wind direction, wind speed and lead time. The interesting data for alligment is the lead time measured in hours and the timestamp. Lead time is the amount of time the prediction was made ahead of time. We are going to make the assumption that the lower the lead time, the more accurate the weather forecast is. Therefor for every hour we choose the forecast for that timestep with the lowest lead time. For any missing values, we assume the weather is unchanged ince the last none missing timestep and fill it in.

Now the data can be alligned by the timestamp and there will be a data point for each hour

### Data size

Since weather is seasonal, it is not always sound to use data from the entire year. We propose that we limit the data to 90 days (3 months) to limit the amount of temporal bias from previous seasons where the weather is different.

This also better for simpler statistical models, which cannot take the added complexity of the changing seasons into account. 

More complex models like multi-layer perceptrons and other neural models, might be able to take the added complexity into account, but our hypothosis is that the added complexity and computation time this approach would cost, is not worth the meager accucary increase we expect to get from this approach over a more simple one.

