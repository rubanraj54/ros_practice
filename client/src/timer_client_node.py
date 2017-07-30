#!/usr/bin/env python

import roslib
import rospy
import time

from server.srv import Timer,TimerRequest

# create node
rospy.init_node('timer_client_node')

# wait for the service is up and running
rospy.wait_for_service('timer')

# create a client instance
client = rospy.ServiceProxy('timer',Timer)

# create request instance
request = TimerRequest()
# request.sleep_time = rospy.Duration.from_sec(5)
request.sleep_time = rospy.Duration.from_sec(11)

#make a request from client

response = client(request)

print response.elapsed_time.to_sec()
