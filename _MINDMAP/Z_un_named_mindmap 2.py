'''
using folium
add a single dot on a map and make a html file to view it

'''
import folium

# Create a new map object
m = folium.Map(location=[37.7833, -122.4167], zoom_start=13)

# Import the Marker class
from folium.features import Marker

# Create a new Marker object
marker = Marker(location=[37.7833, -122.4167], popup="Golden Gate Park")

# Add the Marker object to the Map object
m.add_child(marker)

# Save the map
m.save("map.html")
