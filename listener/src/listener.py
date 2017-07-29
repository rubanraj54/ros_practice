#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import Int32


rospy.init_node('listener')


def display(msg):
	print msg.data

sub = rospy.Subscriber('counter',Int32,display)

rospy.spin()


