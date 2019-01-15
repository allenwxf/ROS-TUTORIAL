#!/usr/bin/env python 

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO


def CommandCallback(commandMessage):
    command = commandMessage.data
    if command == "forwards":
        print("Moving forwards...")
        # pesudo Forwards function
    elif command == "backwards":
        print("Moving backwards...")
        # pesudo Backwards function
    elif command == "left":
        print("Moving left...")
        # pesudo Left function
    elif command == "right":
        print("Moving right...")
        # pesudo Right function



rospy.init_node("driver")
rospy.Subscriber("command", String, CommandCallback)
rospy.spin()

print "Shutting down: stopping motors"