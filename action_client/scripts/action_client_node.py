#!/usr/bin/env python

import roslib
import rospy
import actionlib
import time

from action_server.msg import TimerAction,TimerGoal,TimerResult

def feedback_cb(feedback):
    print 'Time elapsed: ',feedback.time_elapsed.to_sec()
    print 'Time remaining: ',feedback.time_remaining.to_sec()


rospy.init_node('action_client_node')

client = actionlib.SimpleActionClient('timer',TimerAction)
client.wait_for_server()

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(6.0)
# uncomment the below lines to check aborted state
# goal.time_to_wait = rospy.Duration.from_sec(64.0)

client.send_goal(goal,feedback_cb=feedback_cb)

# uncomment the lines below to check preempted state
# time.sleep(3.0)
# client.cancel_goal()

client.wait_for_result()

print 'Result state: ', client.get_state()
print 'Result status: ', client.get_goal_status_text()
print 'Result Time elapsed: ', client.get_result().time_elapsed.to_sec()
print 'Result update sent: ', client.get_result().updates_sent
