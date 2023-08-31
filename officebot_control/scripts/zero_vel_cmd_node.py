#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist

class ZeroVelCmdNode:
    def __init__(self) -> None:
        self._zero_bel_cmd_pub = rospy.Publisher(rospy.get_param("~publish_topic"), Twist, queue_size=5)

    def run(self):
        rospy.loginfo("Starting zero vel cmd node")
        r = rospy.Rate(rospy.get_param("~publish_rate"))
        while not rospy.is_shutdown():
            twist_message = Twist()
            twist_message.linear.x = 0.0
            twist_message.linear.y = 0.0
            twist_message.linear.z = 0.0
            twist_message.angular.x = 0.0
            twist_message.angular.y = 0.0
            twist_message.angular.z = 0.0
            self._zero_bel_cmd_pub.publish(twist_message)
            r.sleep()
        rospy.loginfo("Zero vel cmd node shutdown")


if __name__ == "__main__":
    rospy.init_node('zero_vel_cmd_node')
    zero_vel_cmd_node = ZeroVelCmdNode()
    zero_vel_cmd_node.run()
