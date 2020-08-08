#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def stringListenerCallback(data):
    rospy.loginfo('The contents of topic: %s',data.data)

def stringListener():
    rospy.init_node('node_2' , anonymous = False)
    rospy.Subscriber('topic_1', String, stringListenerCallback)
    rospy.spin()

if __name__='__main__':
    stringListener()
