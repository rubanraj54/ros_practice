#!/usr/bin/env python

import roslib
import rospy

from server.srv import LastMessage,LastMessageResponse
from std_msgs.msg import String

last_message_var = 'empty'

def last_message(request):
    data = request.data
    print 'given data argument', data
    return LastMessageResponse(last_message_var)

def last_message_cb(msg):
    global last_message_var
    last_message_var = msg.data
    print last_message_var

rospy.init_node('last_message_server_node')

service = rospy.Service('last_message',LastMessage,last_message)

sub = rospy.Subscriber('some_string',String,last_message_cb)
rospy.spin()
