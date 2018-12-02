#!/usr/bin/env python

import rospy
import utm
from nav_msgs.msg import Odometry
from tf import tf


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

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def getOdom(odom_data):
    pose = odom_data.pose.pose


def direction:
    ur = urllib.urlopen(url)
    result = json.load(ur)
    
    rospy.init_node('direction',anonymous=True)
    rospy.Subscriber("odom",Odometry,getOdom)



    for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
        print result['routes'][0]['legs'][0]['steps'][i]['start_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['start_location']['lng']
        print result['routes'][0]['legs'][0]['steps'][i]['end_location']['lat']," , ",result['routes'][0]['legs'][0]['steps'][i]['end_location']['lng']
        print ""
