from geopy.geocoders import ArcGIS

geolocator = Nominatim()
query = ("45.421153, -122.77")
location = geolocator.reverse(query)

print(location)
