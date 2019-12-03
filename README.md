
<img src="https://github.com/ehannell/INFO664-01-Final-Project/blob/master/manhattan.jpeg" class="img-responsive" alt="">


**PLANNED CONSTRUCTION AS UNTAPPED POTENTIAL AIRBNB REVENUE**

**Project Overview**

New York City is one of the largest real estate markets, as well as one of the world’s leading tourist destinations. This combination makes it a highly valuable market for Airbnb. According to a June 2019 report by Statista, New York City was Airbnb’s second-largest market in the US in terms of number of listings at the time. The growth of the city shows no sign of slowing down, with many large construction projects underway or scheduled.  
This project was carried out to function as a tool for analyzing and geospatially visualizing planned construction in New York City in terms of potential future Airbnb revenue. The end product could be used either internally by Airbnb, or externally by the City of New York, financial companies, or other stakeholders. For example, Airbnb could benefit by observing the areas with the strongest potential in terms of future supply, consequently planning their physical marketing campaigns to target Airbnb hosts in those areas. As another example, financial companies could use the information as a tool for determining future growth, a foundational part of calculating company valuation.


<iframe width="100%" height="520" frameborder="0" src="https://erikhannell.carto.com/builder/ebd3ebe6-a48f-427e-bcd1-67fd74617154/embed" allowfullscreen webkitallowfullscreen mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>

**Project Recreation Instructions:**

PROJECT MAP - Follow the steps below to recreate the project map.
1.	Download [AB_NYC_2019.csv](https://github.com/ehannell/INFO664-01-Final-Project/blob/master/AB_NYC_2019.csv), [final_project_code.py](https://github.com/ehannell/INFO664-01-Final-Project/blob/master/final_project_code.py) and [final_project_bar_chart.py](https://github.com/ehannell/INFO664-01-Final-Project/blob/master/final_project_bar_chart.py) from the [Github repository](https://github.com/ehannell/INFO664-01-Final-Project). Disregard the planned_construction_11-25-19.csv. This file contains the planned construction in New York City. However, the code will automatically collect this CSV file, given that you are connected to the Internet. 
2.	Open **final_project_code.py** and change the file directory on row 13 to correspond to the location where you put the **AB_NYC_2019.csv** file.
3.	Change the file directory on row 70 to correspond to the local directory of your computer where you are hosting the other project files, the generated CSV-file is used for creating the bar chart (instructions to follow below).
4.	Run the script
5.	If executed correctly, there should now be an HTML-file named **“airbnb_potential_revenue_NYCmap”** in your local project file directory. This should be the same as the map picured below (afer step 6).
6.	Open the HTML file and interact with the map. Click on the red data points to see what the total potential Airbnb revenue is per night for the planned construction location. 

<img src="https://github.com/ehannell/INFO664-01-Final-Project/blob/master/map_snapshot.JPG" class="img-responsive" alt="">


BAR CHART - Follow the below steps to recreate the bar chart.
1.	Open the [final_project_bar_chart.py](https://github.com/ehannell/INFO664-01-Final-Project/blob/master/final_project_bar_chart.py) that you downloaded in step one for PROJECT MAP.
2.	Change the row 4 file directory to the location where you saved the dataset created in step 3 for the PROJECT MAP recreation.
3.	Run the **final_project_bar_chart.py** script. 
4.	If executed correctly, a bar chart should show up on the screen. Download this to the project file directory. The bar chart should look like this one:

<img src="https://github.com/ehannell/INFO664-01-Final-Project/blob/master/bar_chart.png" class="img-responsive" alt="">


**Project Method/Work Process:** 
1.	Airbnb data was collected from Kaggle.com, and the planned construction data was derived from NYC Department of Building's Active Major Construction. Both CSV-files are attached in the Github repository.
2.	The Pandas software library was used for data analysis and manipulation in Python. Two Pandas data frames were created, holding the Airbnb and construction data respectively.
3.	Average price per Airbnb unit per borough was assigned to five variables (one for each borough).
4.	A subset data frame, named “const1”, was created from the planned construction data set. This subset contained only the required columns, as well as a new column holding the total potential Airbnb revenue per row (i.e. per project). This column was derived from multiplying the mean unit price variables per borough with the planned residential units per row, and then additionally adjusted to represent Airbnb’s revenue by multiplying with a variable holding [Airbnb’s average fee](https://www.airbnb.com/help/topic/1120/pricing-fees).
5.	The Python library Folium was used to integrate a Javascript Leaflet library for creating a map of the potential Airbnb revenue areas. The longitude, latitude, and Airbnb potential revenue columns were fed to the Folium code, generating an end product in the form of a geospatial bubble map of New York, with the bubble location representing each planned residential construction site, and the bubble size representing the total potential Airbnb revenue from each construction site. 
6.	Labels were added to provide enhanced understandability of the map so that when a bubble is clicked, a window opens up and displays the potential revenue. 
7.	To generate additional insight, I create a bar chart visualization using Matplotlib in another Python script. 

**Data Sources:**

- [Airbnb data (as of 2019)](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
- [New York City construction (updated continuously)](https://www1.nyc.gov/assets/buildings/html/nyc-active-major-construction.html)
