import folium
from folium.features import add_marker

# Create a new map object
m = folium.Map(location=[37.7833, -122.4167], zoom_start=13)

# Add nodes to the map
m.add_marker(location=[37.7833, -122.4167], popup="Golden Gate Park")
m.add_marker(location=[37.7900, -122.4000], popup="Alcatraz Island")
m.add_marker(location=[37.7900, -122.3900], popup="Fisherman's Wharf")

# Connect the nodes
m.add_polyline([
    [37.7833, -122.4167],
    [37.7900, -122.4000],
    [37.7900, -122.3900]
])

# Hide certain names at certain levels
m.set_zoom_label(zoom_level=12, name="Golden Gate Park", enabled=False)
m.set_zoom_label(zoom_level=11, name="Alcatraz Island", enabled=False)
m.set_zoom_label(zoom_level=11, name="Fisherman's Wharf", enabled=False)

# Display cluster relations
m.add_cluster(location=[37.7833, -122.4167], nodes=["Golden Gate Park", "Alcatraz Island", "Fisherman's Wharf"])

# Save the map
m.save("map.html")
