import folium
import pandas as pd
import json
# Load the cleaned rainfall data
df = pd.read_csv("Rainfall_Data_Cleaned.csv")  # Update filename if needed
df.columns = df.columns.str.strip()  # Remove spaces
df.columns = df.columns.str.lower()  # Convert to lowercase

# Load GeoJSON file
with open("india_state.geojson", "r", encoding="utf-8") as f:
    india_geo = json.load(f)

# Function to get color based on rainfall
def get_color(rainfall):
    if rainfall > 2000:
        return 'darkblue'
    elif rainfall > 1500:
        return 'blue'
    elif rainfall > 1000:
        return 'lightblue'  # Replace 'yellow' (invalid) with 'lightblue'
    elif rainfall > 500:
        return 'orange'
    else:
        return 'red'  # Replace 'brown' (invalid) with 'red'

# Initialize the map
m = folium.Map(location=[22.5, 80.0], zoom_start=5)

# Add Choropleth Layer
folium.Choropleth(
    geo_data=india_geo,
    name="Rainfall",
    data=df,
    columns=["subdivision", "annual rainfall"],  # Use lowercase
    key_on="feature.properties.NAME_1",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Annual Rainfall (mm)"
).add_to(m)

# Add markers
for _, row in df.iterrows():
    if not pd.isna(row["latitude"]) and not pd.isna(row["longitude"]):  # Use lowercase
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['subdivision']}: {row['annual rainfall']} mm",
            icon=folium.Icon(color=get_color(row["annual rainfall"]))
        ).add_to(m)

# Save map
m.save("rainfall_map.html")
print("✅ Map saved as rainfall_map.html")

