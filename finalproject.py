#COMPARE TWO DATASETS, AIRBNB AND CONSTRUCTION

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

#get and create pandas dataframes
airbnb = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/airbnb.csv")
const = pd.read_csv("C:/Users/erikh/Desktop/Pratt/Programming/finalproject/construction.csv")

#study column names
for col in airbnb.columns:
    print(col)

#define needed columns
column_neighbourhood = airbnb["neighbourhood_group"]
column_price = airbnb["price"]
#column_sqm = airbnb[""]
#create frame with only Manhattan

#room size defintions
entire_home = 1000
private_room = 250
