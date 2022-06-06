#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped

import sys, select

TwistMsg = Twist

rospy.init_node('teleop_twist_keyboard')

publisher = rospy.Publisher('cmd_vel', TwistMsg, queue_size = 1)



velocity_x_set = [0.05,0,-0.05,0]
walk_timer = 2 #seconds



twist = TwistMsg()
twist.linear.x = 0
twist.linear.y = 0
twist.linear.z = 0
twist.angular.x = 0
twist.angular.y = 0
twist.angular.z = 0

rospy.sleep(1)
i = 0
# twist.linear.x = velocity_x_set[i]
# publisher.publish(twist)
# rospy.sleep(2)

while not rospy.is_shutdown():
    twist.linear.x = velocity_x_set[i]
    i = i+1 if i<(len(velocity_x_set)-1) else 0

    
    publisher.publish(twist)
    rospy.sleep(walk_timer)