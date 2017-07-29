#!/usr/bin/env python

import roslib
import rospy

from std_msgs.msg import Int32

rospy.init_node('talker')


pub = rospy.Publisher('counter',Int32,queue_size=10,latch=True)

rate = rospy.Rate(2)

rate.sleep()

counter = 1;

# pub.publish(counter)
# print 'published successfully ' + str(counter)
# rospy.spin()
while not rospy.is_shutdown():
	pub.publish(counter)
	counter += 1
	rate.sleep()
