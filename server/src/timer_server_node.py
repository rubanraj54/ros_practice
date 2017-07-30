#!/usr/bin/env python

import roslib
import rospy
import time

from server.srv import Timer,TimerResponse


def timer_cb(request):
    print 'call back called'
    # if the sleep time is greater than 10 seconds, then return 0 seconds as elapsed_time
    if request.sleep_time > rospy.Duration.from_sec(10):
        return TimerResponse(rospy.Duration.from_sec(0.0))
    start_time = time.time()
    sleep_time = request.sleep_time.to_sec()
    time.sleep(sleep_time)
    elapsed_time = rospy.Duration.from_sec(time.time() - start_time)
    response = TimerResponse(elapsed_time)
    return response

rospy.init_node('timer_server_node')

service = rospy.Service('timer',Timer,timer_cb)

rospy.spin()
