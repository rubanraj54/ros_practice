#!/usr/bin/env python
import roslib
#roslib.load_manifest('basics')
import rospy
from ruby_msgs.msg import Complex
from random import random
rospy.init_node('complex_msg_talker')
pub = rospy.Publisher('complex_msg',Complex,queue_size=10)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
	complex_msg = Complex()
	complex_msg.real = random()
	complex_msg.imaginary = random()
	pub.publish(complex_msg)
	rate.sleep()
