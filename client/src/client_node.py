#!/usr/bin/env python

import roslib
import rospy

from server.srv import WordCount

rospy.init_node('client_node')

rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count',WordCount)

words = 'one two three four'

response = word_counter(words)

print 'Count:', response.count

rospy.spin()
