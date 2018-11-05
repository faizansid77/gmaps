import json, urllib
from urllib import urlencode
import googlemaps
start = "Kanpur, India"
finish = "Allahabad, India"
key= "AIzaSyAySdaV-jpPrC20lkpzGJou2De65Hnl1l8"
url = 'https://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', finish),
            ('key', key)
 ))
ur = urllib.urlopen(url)
result = json.load(ur)

for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    print result['routes'][0]['legs'][0]['steps'][i]['start_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['start_location']['lng']
    print result['routes'][0]['legs'][0]['steps'][i]['end_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']
    print ""

# print(result)