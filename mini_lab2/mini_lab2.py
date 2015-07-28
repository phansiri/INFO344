__author__ = 'Phansiri'

import csv
from geopy import Bing
geocoder = Bing(api_key='AmfMoSCD5H_hlMzXRoyNh9Gt1pc2tVuyEljxxworN1ghVevEfyZX_Y2Awwk-GST8', timeout=3)


# generate new file and write to it
csvfilewrite = open('address_extented.csv', 'w')
headerNames = ['address', 'city', 'state', 'zip', 'county', 'latitude', 'longitude']
writer = csv.DictWriter(csvfilewrite, fieldnames=headerNames)
writer.writeheader()

# open up csv and for loop through each line
csvfile = open('addresses.csv', 'r')
reader = csv.DictReader(csvfile)
for row in reader:
    loc = geocoder.geocode(row['address'] + ' ' + row['city'] + ', ' + row['state'] + ' ' + row['zip'])
    # write them to the new file
    try:
        print loc
        county = loc.raw['address']['adminDistrict2']
        lat = loc.raw['point']['coordinates'][0]
        long = loc.raw['point']['coordinates'][1]
        writer.writerow({'address': row['address'], 'city': row['city'], 'state': row['state'],
                         'zip': row['zip'], 'county': county, 'latitude': lat, 'longitude': long})
    except ValueError as e:
        print e.message

