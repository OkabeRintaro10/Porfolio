import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#!pip install geopy
from geopy.geocoders import GoogleV3, Nominatim
import seaborn as sns
import streamlit as st
import io

import warnings

warnings.filterwarnings("ignore")
@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename, on_bad_lines="skip", verbose=False)
    return data
st.title("Bus Stops")
st.subheader("Total bus stops")
df = get_data("Dataset/020230701APSRTC_BOOKED_TICKETS.csv")
st.write(df.head())
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.text(s)

st.subheader("Relevant info")

df = df[['Date of Journey', 'Traveled From', 'Traveled To', 'Route Description',
        'DepotName', 'ServiceStartDate', 'ServiceStartTime', 'BookedDate', 'RegionName',
        'DepartureTime', 'OriginCityName', 'DestinationCity',
        'Created Date Time', 'Arrival Time']]

st.write(df.head())
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.text(s)

st.subheader("Bus stops in AP")
BusStops = get_data("Dataset/Busstop.csv")
buffer = io.StringIO()
BusStops.info(buf=buffer)
s = buffer.getvalue()

st.text(s)

st.map(BusStops, latitude = 'lat', longitude = 'log')