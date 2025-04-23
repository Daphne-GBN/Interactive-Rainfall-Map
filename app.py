import streamlit as st
import os

st.title("India Rainfall Map")
st.write("This is an interactive map showing rainfall patterns across India.")

# Get absolute path
map_path = os.path.join(os.getcwd(), "rainfall_map.html")

# Read the map file
with open(map_path, "r", encoding="utf-8") as file:
    map_html = file.read()

# Display map with scrolling enabled
st.components.v1.html(map_html, height=600, scrolling=True)

