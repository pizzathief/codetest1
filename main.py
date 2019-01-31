import pandas
import json
import requests

centimetre_to_metre_conversion = 0.01

# So the data has a "weight" column, but the exercise specifies a value of 250
# DHL specifies a conversion factor of 250 or 333 (as does Aust Post) , so
# conversion factor seems to be for all packages, not just air conditioners.
# DHL does demand you use the maximum of w*l*h*conv , or specified weight
cubic_weight_conversion_factor = 250


endpoint_url = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
endpoint_page = '/api/products/1'
reached_end = False
pages = []

# while not at end of paginated endpoint
while not reached_end:
    endpoint = endpoint_url + endpoint_page
    # read in json for current endpoint
    data = requests.get(endpoint)
    data_converted = json.loads(data.text)

    # have to massage the json a bit before converting to dataframe
    # and flatten a few internal dicts
    dataframe_page = \
        pandas.io.json.json_normalize(json.loads(data.text)['objects'])
    pages.append(dataframe_page)

    if data_converted['next']:
        endpoint_page = data_converted['next']
    else:
        reached_end = True


# convert to a single dataframe.  Appending rows to a dataframe creates a new
# dataframe every time, and using the DataFrame.concat() function a lot is
# quite wasteful, so concat all at once

all_data = pandas.concat(pages)
all_data['cubic_weight'] = \
    all_data['size.height'] * centimetre_to_metre_conversion *\
    all_data['size.length'] * centimetre_to_metre_conversion *\
    all_data['size.width'] * centimetre_to_metre_conversion * \
    cubic_weight_conversion_factor

# now get the average of what we're interested in
air_conditioners = all_data.loc[all_data['category'] == 'Air Conditioners']
count = len(air_conditioners.index)
total = air_conditioners['cubic_weight'].sum()
print('average cubic weight of air conditioners is ',
      '%.2f' % (total/count), ' kg')
