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

st.title("Number of Bus Stops in Vijayawada")


@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename, on_bad_lines="skip", verbose=False)
    return data

BusStops = get_data("Dataset/Busstop.csv")
buffer = io.StringIO()
BusStops.info(buf=buffer)
s = buffer.getvalue()

st.text(s)

st.map(BusStops, latitude = 'lat', longitude = 'log')
