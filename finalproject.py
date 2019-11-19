#AIRBNB DATASET PROGRAMMING

import pandas as pd
import json
import folium
from folium import plugins
from folium.plugins import HeatMap
from folium.plugins import FastMarkerCluster
import colorsys
import requests

#define variable for planned construction dataset
const_csv_url = "http://bit.ly/2zCmlts"

#get and create pandas dataframe
#do i have to incorporate REGEX to capture different file versions?
const = pd.read_csv(const_csv_url)
airbnb = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/airbnb.csv")

#new airbnb subset, with desired columns
airbnb1 = airbnb[["neighbourhood_group", "price", "room_type"]]

#list of borough price
mean_borough_price = airbnb1.groupby("neighbourhood_group")["price"].mean()
#print(mean_borough_price)

#variables holding mean airbnb price per borough
mean_brooklyn_price = mean_borough_price["Brooklyn"]
mean_manhattan_price = mean_borough_price["Manhattan"]
mean_queens_price = mean_borough_price["Queens"]
mean_bronx_price = mean_borough_price["Bronx"]
mean_staten_island_price = mean_borough_price["Staten Island"]

#new construction sebset, with desired data
const1 = const[["borough", "applicant_business_name", "proposed_dwelling_units", "proposed_occupancy_class", "longitude", "latitude"]]
const1 = const1[const1["proposed_dwelling_units"] > 0.0]

#get borough price
def get_borough_price(borough):
    if borough == "Manhattan":
        return mean_borough_price["Manhattan"]
    elif borough == "Brooklyn":
        return mean_borough_price["Brooklyn"]
    elif borough == "Queens":
        return mean_borough_price["Queens"]
    elif borough == "Bronx":
        return mean_borough_price["Bronx"]
    elif borough == "Staten Island":
        return mean_borough_price["Staten Island"]

#create new column with airbnb price per unit
const1["airbnb_price_unit"] = const1["borough"].apply(get_borough_price)
#make numeric
const1["airbnb_price_unit"] = const1["airbnb_price_unit"].apply(pd.to_numeric)

#create new column with dwelling units * airbnb price
const1["airbnb_price_total"] = const1["borough"].apply(get_borough_price) * const1["proposed_dwelling_units"]
#make numeric
const1["airbnb_price_total"] = const1["airbnb_price_total"].apply(pd.to_numeric)

#create new column with airbnb potential revenue
const1["airbnb_potential_revenue"] = const1["airbnb_price_total"] * 0.16

print(" ")
for col in const1:
    print(col)

#write data to a CSV-file
const1.to_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/const1.csv")

###########################################################################
#_______________________________BUILD MAP__________________________________
###########################################################################

#Create Map Object
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

def generateBaseMap(default_location=[40.7128, -74.0060], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map

#Generate BaseMap
base_map = generateBaseMap()

#GET COLOR CODE PER BOROUGH TO MAP TO "FILL-COLOR"
#def get_color(borough):
#    if borough == "Brooklyn":
#        return 'blue'
#    elif borough == "Manhattan":
#        return "blue"
#    elif borough == "Queens":
#        return "blue"
#    elif borough == "Staten Island":
#        return "blue"
#    elif borough == "Bronx":
#        return "blue"
#    else:
#        return "blue"

for i in zip(range(0, len(const1))):
    bl = "blue"
    label = "Potential revenue: $" + str(format(const1.iloc[i]["airbnb_potential_revenue"], ",.0f"))
    #print(label)
    folium.Circle(
        location=[const1.iloc[i]['latitude'], const1.iloc[i]['longitude']],
        radius=const1.iloc[i]['airbnb_potential_revenue']/60,
        fill=True,
        fill_color=bl,
        color=bl,
        fill_opacity=0.5,
    ).add_child(folium.Popup(label)).add_to(base_map)

#ADD BOROUGH BUONDARIES
#borough_boundaries = f"C:/Users/erikh/Desktop/Pratt/Programming/finalproject/borough_boundaries.geojson"
#base_map.add_child(folium.GeoJson(borough_boundaries,
#                                  name='geojson'))

#Save map
base_map.save("airbnb_potential_revenue_NYCmap.html")
