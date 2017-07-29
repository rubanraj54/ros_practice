#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import Int32


rospy.init_node('doubler')

# this method, receive the number from the 'number' topic and double it and publish the result on 'doubled' topic
def doubler(msg):
	doubled_number = Int32()
	doubled_number.data = msg.data * 2
	pub.publish(doubled_number)


sub = rospy.Subscriber('number',Int32,doubler)
pub = rospy.Publisher('doubled',Int32,queue_size=10)

rospy.spin()
