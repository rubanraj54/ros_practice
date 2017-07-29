#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import String

rospy.init_node('bindutalker')

pub = rospy.Publisher('blablabla',String,queue_size=10)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
	pub.publish('I miss you!!!')
	rate.sleep()
