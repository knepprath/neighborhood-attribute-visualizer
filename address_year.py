import os
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails

ZILLOW_API_KEY = os.environ['ZILLOW_API_KEY']

address = '13680 SW Berea Dr Tigard OR'
zipcode = '97223'

zillow_data = ZillowWrapper(ZILLOW_API_KEY)
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

zillow_id = result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails

zillow_data = ZillowWrapper(ZILLOW_API_KEY)
updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
result = GetUpdatedPropertyDetails(updated_property_details_response)

print result.year_built # number of rooms of the home