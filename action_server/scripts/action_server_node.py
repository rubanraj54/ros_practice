#!/usr/bin/env python

import roslib
import rospy
import time
import actionlib

from action_server.msg import TimerAction,TimerGoal,TimerFeedback,TimerResult

def do_timer(goal):
    start_time = time.time()
    update_count = 0

    if goal.time_to_wait.to_sec() > 60.0:
        result = TimerResult()
        result.updates_sent = update_count
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        server.set_aborted(result,'time to wait is too long, so the request is aborted')

    while (time.time() - start_time) < goal.time_to_wait.to_sec():
        if server.is_preempt_requested():
            result = TimerResult()
            result.updates_sent = update_count
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            server.set_preempted(result,'Request is preempted by client')
            return

        feedback = TimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.time_remaining = rospy.Duration.from_sec(goal.time_to_wait.to_sec() - feedback.time_elapsed.to_sec())
        server.publish_feedback(feedback)
        update_count += 1

        time.sleep(1.0)

    result = TimerResult()
    result.updates_sent = update_count
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    server.set_succeeded(result,'Timer completed successfully')


rospy.init_node('action_server_node')
server = actionlib.SimpleActionServer('timer',TimerAction,do_timer,False)
server.start()
rospy.spin()
