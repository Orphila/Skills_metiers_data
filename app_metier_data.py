#---------------Construction app st-----------------------------------------

import streamlit as st  
import plotly.express as px  
import matplotlib.pyplot as plt

st.set_page_config(page_title="Skills pour métiers data", 
                   page_icon=":bar_chart:",
                   layout="wide")
# ---- MAINPAGE ----
st.title(":bar_chart: Skills pour métiers de la data")

import pymongo
import os

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(st.secrets["mongo"]["lien"])

client = init_connection()
st.markdown("debug 8 lancé, client créé")
# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.dashboard_metiers_data
    items = db.data.find()
    items = list(items) 
    return items

items = get_data()

# Print results.
for item in items[:5]:
    st.write(f"{item['poste']} has a :{item['contrat']}:")

"""
#lien = str(os.getenv("lien"))
lien = st.secrets['mongo']['lien']
client = pymongo.MongoClient(lien)
db = client["dashboard_metiers_data"]
collection = db["data"]
cursor = collection.find({})

import pandas as pd
st.markdown("debug 7 lancé")
st.markdown(lien)
"""





