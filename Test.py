import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#!pip install geopy
from geopy.geocoders import GoogleV3, Nominatim
import seaborn as sns
import streamlit as st

import warnings

warnings.filterwarnings("ignore")

st.title("Number of Bus Stops in Vijayawada")


@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename, on_bad_lines="skip", verbose=False)
    return data


df = get_data(filename="../Xelp/Dataset/020230701APSRTC_BOOKED_TICKETS.csv")
st.write(df.head())
st.header("Information on Data")
st.write(df.describe())


st.header("Updated Data")
df = df[
    [
        "Date of Journey",
        "Traveled From",
        "Traveled To",
        "Route Description",
        "DepotName",
        "ServiceStartDate",
        "ServiceStartTime",
        "BookedDate",
        "RegionName",
        "DepartureTime",
        "OriginCityName",
        "DestinationCity",
        "Created Date Time",
        "Arrival Time",
    ]
]
import io

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.text(s)
# # Plot Stops on Map
# plot all the stops in the cities of Vijayawada and Vishkapatnam on map using Longitude and Latitude

from geopy.geocoders import ArcGIS


nom = ArcGIS()


def get_stop_long_lat(city_symb, assistance_text=None):
    # Filter the DataFrame to rows where column 'A' matches the selected value and column 'B' matches the selected value
    filtered_df = df[
        (df["OriginCityName"] == city_symb) & (df["DestinationCity"] == city_symb)
    ]
    from_unique_point = filtered_df["Traveled From"].unique()
    to_unique_point = filtered_df["Traveled To"].unique()

    unique_values_set = set(from_unique_point).union(set(to_unique_point))

    unique_points = list(unique_values_set)

    stop_points_info = []
    for point in unique_points:
        point_info = {}
        point_info["data_name"] = point

        if assistance_text is not None:
            point = point + " " + assistance_text

        loc = nom.geocode(point)

        point_info["log"] = loc.longitude
        point_info["lat"] = loc.latitude
        stop_points_info.append(point_info)

    return stop_points_info


#vijaywada_points = get_stop_long_lat("VJA", "Vijaywada, Andhra Pradesh")
#vishakapatnam_points = get_stop_long_lat("VSP", "Vishakapatnam")

#total_busstops = vijaywada_points + vishakapatnam_points

st.header('List of all Bus Stops with their Longitude and Latitude')

#Busstop_df = pd.DataFrame(total_busstops)
#df.to_csv("../Xelp/Dataset/Busstop.csv")

BusStops = get_data("../Xelp/Dataset/Busstop.csv")
buffer = io.StringIO()
BusStops.info(buf=buffer)
s = buffer.getvalue()

st.text(s)

st.map(BusStops, latitude = 'lat', longitude = 'log')