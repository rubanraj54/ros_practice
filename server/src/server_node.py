#!/usr/bin/env python

import roslib
import rospy

from server.srv import WordCount,WordCountResponse


def count_words(request):
    words = request.words
    response = WordCountResponse(len(words.split()))
    return response
    
rospy.init_node('word_count_server')

service = rospy.Service('word_count',WordCount,count_words)

rospy.spin()
