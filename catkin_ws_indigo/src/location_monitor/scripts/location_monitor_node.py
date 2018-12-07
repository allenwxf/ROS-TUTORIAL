#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

landmarks = []
landmarks.append(("Cube", 0.31, -0.99));
landmarks.append(("Dumpster", 0.11, -2.42));
landmarks.append(("Cylinder", -1.14, -2.88));
landmarks.append(("Barrier", -2.59, -0.83));
landmarks.append(("Bookshelf", -0.09, 0.53));

def distance(x1, y1, x2, y2):
	xd = x1 - x2
	yd = y2 - y2

def callback(msg):
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	closest_name = None
	closest_distance = None
	for l_name, l_x, l_y in landmarks:
		dist = distance(x, y, l_x, l_y)
		if closest_distance is None or dist < closest_distance:
			closest = l_name
			closest_distance = dist
	rospy.loginfo("x: {}, y: {}".format(x, y))

def main():
	rospy.init_node("location_monitor")
	rospy.Subscriber("/odom", Odometry, callback)
	rospy.spin()

if __name__ == "__main__":
	main()
