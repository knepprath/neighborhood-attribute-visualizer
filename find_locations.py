import sys
import requests

url = 'http://api.openstreetmap.org/api/0.6/map?bbox=-122.77,45.42,-122.763,45.428'

request = requests.get(url=url)

print request.status_code
print request.headers
print request.text
print request.encoding
print request.json
print request.content

with open("test.osm", "wb") as code:
    code.write(request.content)