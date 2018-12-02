#!/usr/bin/env python
class loc_to_waypoint:
    import rospy
    import utm
    from sensor_msgs.msg import NavSatFix
    from tf import tf


    import json, urllib
    from urllib import urlencode
    import googlemaps
    key= "AIzaSyAySdaV-jpPrC20lkpzGJou2De65Hnl1l8"

    def dist(x1,y1,x2,y2):
        return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

    def getGPS(gps_data):
        global latit = gps_data.latitude
        global longit = gps_data.longitude


    def direction:
        ur = urllib.urlopen(url)
        result = json.load(ur)
        
        rospy.init_node('direction',anonymous=True)
        rospy.Subscriber("mavros/global_postion/raw/fix",NavSatFix,getGPS)

        start = latit,",",longit
        finish = "Allahabad, India"
        url = 'https://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
                    ('origin', start),
                    ('destination', finish),
                    ('key', key)
        ))


        for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
            print result['routes'][0]['legs'][0]['steps'][i]['start_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['start_location']['lng']
            print result['routes'][0]['legs'][0]['steps'][i]['end_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']
            print ""
