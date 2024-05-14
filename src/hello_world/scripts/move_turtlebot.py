#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import sys

robot_x = 0
obstacle_detected = False

def pose_callback(msg):
    global robot_x
    #Reading x position from the Odometry message
    robot_x = msg.pose.pose.position.x
    rospy.loginfo("Robot X = %f\n",robot_x)

def scan_callback(msg):
    global obstacle_detected
    # Consider an obstacle detected if the distance to any scan point is less than 0.5 meters
    min_distance = 1  # minimum safe distance in meters
    for distance in msg.ranges:
        if distance < min_distance:
            rospy.logwarn("Obstacle detected! Stopping robot.")
            obstacle_detected = True
            return

def move_turtle(lin_vel,ang_vel,distance):
    global robot_x, obstacle_detected
    rospy.init_node('move_turtlebot', anonymous=False)
    #The Twist topic is /cmd_vel
    # pub = rospy.Publisher('/cmd_vel/teleop', Twist, queue_size=10)
    pub = rospy.Publisher('/four_wheel_steering_controller/cmd_vel', Twist, queue_size=10)
    #Position topic is /odom
    rospy.Subscriber('/four_wheel_steering_controller/odom', Odometry, pose_callback)
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rate = rospy.Rate(10) # 10hz
    vel = Twist()

    while not rospy.is_shutdown():
        if obstacle_detected:
            vel.linear.x = 0
            vel.angular.z = 0
            pub.publish(vel)
            rospy.sleep(1)  # pause for a bit after detecting an obstacle
            obstacle_detected = False  # reset the obstacle detection
            continue

        vel.linear.x = lin_vel
        vel.angular.z = ang_vel
        rospy.loginfo("Linear Vel = %f: Angular Vel = %f",lin_vel,ang_vel)
        
        if(robot_x >= distance):
            rospy.loginfo("Robot Reached destination")
            rospy.logwarn("Stopping robot")
            vel.linear.x = 0
            vel.angular.z = 0
            pub.publish(vel)
            break
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    except rospy.ROSInterruptException:
        pass