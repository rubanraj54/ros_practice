#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import String

rospy.init_node('latched_talker_node')


pub = rospy.Publisher('some_string',String,queue_size=10,latch=True)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
	pub.publish('f*** off!!!')
	# print 'latched message published successfully'
	rate.sleep()
