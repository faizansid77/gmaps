import json, urllib
from urllib import urlencode
import googlemaps
# start = "Kanpur, India"
# finish = "Allahabad, India"


start = "Hall Of Residence 5, IIT Kanpur, Kalyanpur, Kanpur"
finish = "New Core Labs, Nankari, Kalyanpur, Kanpur"


key= "AIzaSyDOGfCVo3YCdYmMfzlLirZpWK4v4pD5hKo"
url = 'https://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', finish),
            ('key', key)
 ))
ur = urllib.urlopen(url)
result = json.load(ur)
# for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
#     print result['routes'][0]['legs'][0]['steps'][i]['start_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['start_location']['lng']
#     print result['routes'][0]['legs'][0]['steps'][i]['end_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']
#     print ""

print result