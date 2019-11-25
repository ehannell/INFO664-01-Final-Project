# pythonproject
This repository contains code for my final project in the programming for cultural heritage course at Pratt Institute

PROJECT NAME: NYC construction projects – untapped Airbnb revenue

Overview
New York City is one of the largest real estate markets in the world and combined with being a top tourist destination, it puts the city among the most important markets for tech giant Airbnb. According to data from June 2019, New York was the second-largest market in the US in terms of number of listings at the time (reference: https://www.statista.com/chart/18963/most-popular-us-cities-for-airbnb-homeaway/). The growth of the city shows no sign of slowing down, with many large construction projects currently undergoing or planned.
This project was carried out to function as a tool for the analysis and visualization of planned construction in New York City in the form of potential future Airbnb revenue. The end product could be used either internally by Airbnb, or externally by the City of New York, financial companies, or other stakeholders. For example, Airbnb could benefit by observing the areas with the strongest potential in terms of future supply, consequently deciding on targeted physical marketing to attract Airbnb hosts. Furthermore, financial companies could use the information as a mean for determining future growth, a foundational part of calculating company valuation. 

Instructions:
The end product is an interactive map of the five New York boroughs, with a vast amount of data points. These data points represent an area of planned or undergoing residential construction projects. When the user clicks on one of the dots, a label with a dollar value will popup. This dollar value corresponds to the total potential Airbnb revenue of that particular location. 

Method: 
This project was carried out with the objective to analyze future Airbnb locations in the five boroughs of New York City. The resulting product of this project can be used in various ways; AirBnb can use it to decide where they should focus their physical marketing, while financial companies could leverage the data to analyze potential Airbnb sales growth in certain areas, the later purpose would have to be combined with many other variables in order to generate accurate insights.

Data Sources: 
Airbnb data (as of 2019): 
https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data
New York City construction (updated continuously): 
https://www1.nyc.gov/assets/buildings/html/nyc-active-major-construction.html
Once the estimates were in place, they were applied to another dataset about planned construction in New York City. This resulted in a new column with Airbnb sales. Once in place, the longitude and latitudes were used to generate a geospatial visualization of predicted future sales in the five boroughs of New York. This second dataset is regularly updated, and thanks to the Python-code, the updates have been incorporated into the project.
