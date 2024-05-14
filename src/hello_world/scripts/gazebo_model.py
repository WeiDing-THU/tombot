#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import PoseStamped
from gazebo_msgs.msg import ModelStates
from tf.transformations import quaternion_from_euler
from math import atan2

def get_object_pose(msg, object_name):
    """Callback function to find and return the pose of the specified object."""
    for i in range(len(msg.name)):
        if msg.name[i] == object_name:
            return msg.pose[i]
    return None

def go_to_object(target_pose, object_pose):
    """Function to publish goal to move_base to navigate to the object."""
    # Publisher to send goal to the navigation stack
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)

    # Calculate orientation to face the object
    angle_to_object = atan2(object_pose.position.y - target_pose.position.y, object_pose.position.x - target_pose.position.x)
    quaternion = quaternion_from_euler(0, 0, angle_to_object)
    print("angle_to_object: ", angle_to_object)
    # Create and send a goal pose
    goal = PoseStamped()
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "/four_wheel_steering_controller/odom"
    goal.pose.position = target_pose.position
    goal.pose.orientation.x = quaternion[0]
    goal.pose.orientation.y = quaternion[1]
    goal.pose.orientation.z = quaternion[2]
    goal.pose.orientation.w = quaternion[3]
    print("publishing goal")
    print(goal)
    goal_pub.publish(goal)

def main(object_name):
    """Main function to initialize node and subscribe to model states."""
    rospy.init_node('navigate_to_object')
    x_offset = -0.2
    y_offset = -0.2
    object_pose = None

    def callback(msg):
        nonlocal object_pose
        object_pose = get_object_pose(msg, object_name)

    rospy.Subscriber('/gazebo/model_states', ModelStates, callback)

    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown() and object_pose is None:
        rate.sleep()

    if object_pose is not None:
        # Assuming target_pose is initially set as the robot's current location
        target_pose = object_pose  # This should be adjusted based on your specific requirements
        target_pose.position.x = target_pose.position.x + x_offset  # Ensure the robot is at the same x-coordinate as the object - 0.2
        target_pose.position.y = target_pose.position.y + y_offset  # Ensure the robot is at the same y-coordinate as the object - 0.2
        target_pose.position.z = 0.0  # Ensure the robot is at the same z-coordinate as 0 (?possibly change for the initial robot height?)
        go_to_object(target_pose, object_pose)

if __name__ == '__main__':
    try:
        object_name = str(sys.argv[1]) if len(sys.argv) > 1 else 'beer'
        main(object_name)
    except rospy.ROSInterruptException:
        pass
