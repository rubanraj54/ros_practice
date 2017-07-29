#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import Int32

rospy.init_node('number_talker')


pub = rospy.Publisher('number',Int32,queue_size=10)

rate = rospy.Rate(2)

# give some sleep time to make sure publisher connect with all Subscriber
rate.sleep()

number = 1;

while not rospy.is_shutdown():
	pub.publish(number)
	number += 1
	rate.sleep()
