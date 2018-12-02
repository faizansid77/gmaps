#!/usr/bin/env python
import rospy
import utm
import yaml
from sensor_msgs.msg import NavSatFix


import json, urllib
from urllib import urlencode
import googlemaps
key= "AIzaSyC_Pgah9riL6k2aG326mxW1v6oCiODgjEg"

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def getGPS(gps_data):
    global latit
    global longit
    latit = gps_data.latitude
    longit = gps_data.longitude


def direction():
    
    rospy.init_node('direction',anonymous=True)
    rospy.Subscriber("mavros/global_postion/raw/fix",NavSatFix,getGPS)

    global latit
    global longit

    start = "%s,%s" % (latit,longit)

    # start = "Hall Of Residence 5, IIT Kanpur, Kalyanpur, Kanpur"
    finish = "New Core Labs, Nankari, Kalyanpur, Kanpur"


    url = 'https://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
                ('origin', start),
                ('destination', finish),
                ('key', key)
    ))

    ur = urllib.urlopen(url)
    result = json.load(ur)

    dataList=[None]
    try:
        for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
            utmData=utm.from_latlon(result['routes'][0]['legs'][0]['steps'][i]['end_location']['lat'],result['routes'][0]['legs'][0]['steps'][i]['end_location']['lng'])
            dataList.append(utmData[:2])
        rospy.set_param("utm",dataList)
    except:
        print "Error in getting waypoints!"


if __name__=='__main__':
    direction()