#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Bool

import sys, select

start_motion = False

def callback(data):
    global start_motion
    start_motion = data.data

TwistMsg = Twist

rospy.init_node('walk_front_back')

publisher = rospy.Publisher('cmd_vel', TwistMsg, queue_size = 1)
rospy.Subscriber("/start_motion", Bool, callback)


velocity_x_set = [0.05,0,-0.05,0]
action_x_set = ["Forward", "Nowhere", "Backwards", "Nowhere"]
walk_timer = 2 #seconds
freq = 10
r = rospy.Rate(freq)



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

ns = rospy.get_namespace()
while not rospy.is_shutdown():
    if not (start_motion):
        twist.linear.x = 0
    else:
        twist.linear.x = velocity_x_set[i]
        print(ns, " going ", action_x_set[i])
        i = i+1 if i<(len(velocity_x_set)-1) else 0
        
        for j in range(walk_timer*freq):
            publisher.publish(twist)
            r.sleep()
