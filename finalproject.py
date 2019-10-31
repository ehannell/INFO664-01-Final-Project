#AIRBNB DATASET PROGRAMMING

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
#import geopandas as gpd
import requests
from urllib import request

#define variable for planned construction dataset
const_csv_url = "http://bit.ly/2zCmlts"

#get and create pandas dataframe
#do i have to incorporate REGEX to capture different file versions?
const = pd.read_csv(const_csv_url)
airbnb = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/airbnb.csv")

#new airbnb subset, with desired columns
airbnb1 = airbnb[["neighbourhood_group", "price", "room_type"]]

#create list of borough price
mean_borough_price = airbnb1.groupby("neighbourhood_group")["price"].mean()
print(mean_borough_price)

#create variables holding mean airbnb price per borough
mean_brooklyn_price = mean_borough_price["Brooklyn"]
mean_manhattan_price = mean_borough_price["Manhattan"]
mean_queens_price = mean_borough_price["Queens"]
mean_bronx_price = mean_borough_price["Bronx"]
mean_staten_island_price = mean_borough_price["Staten Island"]

#create construction sebset, with desired data
const1 = const[["borough", "proposed_dwelling_units", "proposed_occupancy_class", "longitude", "latitude"]]
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

#create new column with airbnb price
const1["airbnb_price_unit"] = const1["borough"].apply(get_borough_price)

#create new column with dwelling units * airbnb price
const1["airbnb_price_total"] = const1["borough"].apply(get_borough_price) * const1["proposed_dwelling_units"]

for col in const1:
    print(col)

#write data to a CSV-file
const1.to_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/const1.csv")

