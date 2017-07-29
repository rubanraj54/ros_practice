#!/usr/bin/env python

import roslib
import rospy

from ruby_msgs.msg import Complex


rospy.init_node('complex_msg_listener')


def display(msg):
	print 'Real number: ', msg.real
	print 'Imaginary number: ', msg.imaginary

sub = rospy.Subscriber('complex_msg',Complex,display)

rospy.spin()
