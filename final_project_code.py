#AIRBNB REVENUE PREDCTION PROJECT

import pandas as pd
import folium

#_____________CREATE DATASETS______________

#create construction data frame, automated retrieval
const_csv_url = "http://bit.ly/2zCmlts"
const = pd.read_csv(const_csv_url)

#create airbnb data frame
airbnb = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/airbnb.csv")

#new airbnb subset, with desired columns
airbnb1 = airbnb[["neighbourhood_group", "price", "room_type"]]

#___________DATA MANIPULATION______________

#get list of mean airbnb borough prices
mean_borough_price = airbnb1.groupby("neighbourhood_group")["price"].mean()

#create variables holding mean airbnb price per borough
mean_brooklyn_price = mean_borough_price["Brooklyn"]
mean_manhattan_price = mean_borough_price["Manhattan"]
mean_queens_price = mean_borough_price["Queens"]
mean_bronx_price = mean_borough_price["Bronx"]
mean_staten_island_price = mean_borough_price["Staten Island"]

#create variable for calculating airbnb revenue from rent price
airbnb_fee = 0.16

#new construction subset, with selected data
const1 = const[["borough", "applicant_business_name", "proposed_dwelling_units", "proposed_occupancy_class", "longitude", "latitude"]]

#filter to keep only residential construction
const1 = const1[const1["proposed_dwelling_units"] > 0.0]

#function for calculating borough price
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

#new column with airbnb price per unit
const1["airbnb_price_unit"] = const1["borough"].apply(get_borough_price)
const1["airbnb_price_unit"] = const1["airbnb_price_unit"].apply(pd.to_numeric)

#new column with dwelling units * airbnb price = airbnb_price_total
const1["airbnb_price_total"] = const1["borough"].apply(get_borough_price) * const1["proposed_dwelling_units"]
const1["airbnb_price_total"] = const1["airbnb_price_total"].apply(pd.to_numeric)

#new column with airbnb_potential_revenue
const1["airbnb_potential_revenue"] = const1["airbnb_price_total"] * airbnb_fee

#observe columns
for col in const1:
    print(col)
print(" ")
print(const1)

#write data to a CSV-file
const1.to_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/const1.csv")

############################################################################
#_______________________________BUILD MAP__________________________________#
############################################################################

#Build basemap over New York City
def generateBaseMap(default_location=[40.7128, -74.0060], default_zoom_start=12):
    base_map = folium.Map(location=default_location, tiles="Stamen Terrain", control_scale=True, zoom_start=default_zoom_start)
    return base_map

#Generate BaseMap
base_map = generateBaseMap()

#Integrate Airbnb data
for i in zip(range(0, len(const1))):
    airbnb_brand = "#FF5A5F"
    label = "Potential revenue: $" + str(format(const1.iloc[i]["airbnb_potential_revenue"], ",.0f"))
    #print(label)
    folium.Circle(
        location=[const1.iloc[i]['latitude'], const1.iloc[i]['longitude']],
        radius=const1.iloc[i]['airbnb_potential_revenue']/60,
        fill=True,
        fill_color=airbnb_brand,
        color=airbnb_brand,
        fill_opacity=0.5,
    ).add_child(folium.Popup(label)).add_to(base_map)



#Save map
base_map.save("airbnb_potential_revenue_NYCmap.html")