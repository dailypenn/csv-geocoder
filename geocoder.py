import os
import sys
import pandas as pd
import googlemaps
import json
from urllib.request import urlopen
from urllib.parse import quote

# change city and state if this is for anywhere other than Philly
api_key = os.environ['API_KEY']
city = 'Philadelphia'
state = 'PA'

if len(sys.argv) is not 2:
    raise Exception('Please enter one CSV file name.')

input_file = sys.argv[1]
output_file = 'geocoded_' + input_file
data = pd.read_csv(input_file, encoding='utf8')

if 'address' not in data.columns:
	raise ValueError('Input has no address column')

# create latitude and longitude columns
data['lat'] = 0.0
data['lng'] = 0.0

# use Google's geocoding API to get lat/lng from addresses and update data
for index, row in data.iterrows():
    address = row['address']
    address = address.replace(' ', '+')
    address += '+' + city + '+' + state
    address = quote(address) # encode address for special characters
    api_url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, api_key)

    response = urlopen(api_url)
    result = json.load(response)

    if result['results']:
        lat = result['results'][0]['geometry']['location']['lat']
        lng = result['results'][0]['geometry']['location']['lng']
        data.at[index, 'lat'] = lat
        data.at[index, 'lng'] = lng
    else:
        data.at[index, 'lat'] = 0.0
        data.at[index, 'lng'] = 0.0

data.to_csv(output_file, index=False, encoding='utf8')
