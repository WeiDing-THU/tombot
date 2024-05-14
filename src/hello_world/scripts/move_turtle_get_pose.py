#!/usr/bin/env python3

import rospy
#Importing Twist message: Used to send velocity to Turtlesim
#就是你要发布topic的type
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#Handling command line arguments
import sys
robot_x = 0

#/turtle1/Pose topic callback
def pose_callback(pose):
    global robot_x
    rospy.loginfo("Robot X = %f : Y=%f : Z=%f\n",pose.x,pose.y,pose.theta)
    robot_x = pose.x

#Function to move turtle: Linear and angular velocities are arguments
def move_turtle(lin_vel,ang_vel,distance):
    global robot_x
    
    rospy.init_node('move_turtle', anonymous=False)
    #The /turtle1/cmd_vel is the topic in which we have to send Twist messages
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #Creating new subscriber: Topic name= /turtle1/pose: Callback name: pose_callback
    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    rate = rospy.Rate(10) # 10hz

    #Creating Twist message instance
    vel = Twist()
    while not rospy.is_shutdown():
        #Adding linear and an gular velocity to the message
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel
        rospy.loginfo(f'Linear Vel = {lin_vel}, Angular Vel = {ang_vel}')
        #Checking the robot distance is greater than the commanded distance
        # If it is greater, stop the node
        if(robot_x >= distance):
                rospy.loginfo("Robot Reached destination")
                rospy.logwarn("Stopping robot")
                break
        #Publishing Twist message
        pub.publish(vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        #Providing linear and angular velocity through command line
        move_turtle(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    except rospy.ROSInterruptException:
        pass