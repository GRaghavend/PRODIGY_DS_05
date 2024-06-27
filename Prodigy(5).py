import folium
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns',30)
df=pd.read_csv('/Users/raghavender/Datasets:Research/sample_traffic_accidents.csv')
#weather condition dataset
weather_counts= df['weather_condition'].value_counts().reset_index()
weather_counts.columns = ['weather_condition', 'count']
#road condition dataset
roadCon_counts= df['road_condition'].value_counts().reset_index()
roadCon_counts.columns = ['road_condition', 'count']
#weather condition graph
plt.figure(figsize=(10,6))
sns.set_palette("RdBu")
sns.barplot(x="weather_condition", y="count", data=weather_counts)
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.title('Number of Accidents by Weather Condition')
plt.xticks(rotation=45)
plt.show()
#road condition graph
plt.figure(figsize=(10,6))
sns.set_palette("PRGn")
sns.barplot(x='road_condition',y='count',data=roadCon_counts)
plt.xlabel("Road Condition")
plt.ylabel("Number of Accidents")
plt.title("Number of Accidents by Road Condition")
plt.xticks(rotation=45)
plt.show()
#Create map object and circle marker
# Chennai coordinates
chennai_coords = [13.0827, 80.2707]
# Create a map centered at Chennai
accident_map = folium.Map(location=chennai_coords, zoom_start=12)
# Add CircleMarkers for each accident location
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='red',
        popup="Accident Hotspots",
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(accident_map)
# Save the map to an HTML file
accident_map.save('accident_hotspots.html')
print("Map generated")

