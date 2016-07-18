# neighborhood-attribute-visualizer
What: Utility for mapping homes built in a specified date range.  

Why: Portland has a housing crisis. http://www.oregonlive.com/portland/index.ssf/2016/06/portland_city_council_to_discu.html

Discussing this article with my wife and found ourselves thinking you really need the data in order to know if this is an effective strategy:
How many houses does this really impact? 
Are these houses located in dense pockets or scattered?

Realized we have the technology to answer these questions quite easily.

Libraries I've evaluated for initial POC:
- Convenient wrapper for Zillow's API: pyzillow (https://github.com/hanneshapke/pyzillow)
- Grabbing locations within a given radius: openstreetmap (http://wiki.openstreetmap.org/wiki/Downloading_data)
- Might need to be used to derive address from coordinate: geopy (https://github.com/geopy/geopy)
- Stretch goal would be to visualize this in a heatmap using Google Maps: (https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap)
