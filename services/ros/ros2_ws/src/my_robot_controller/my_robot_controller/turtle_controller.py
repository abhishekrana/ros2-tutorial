#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleControllerNode(Node):
    def __init__(self) -> None:
        super().__init__("pose_subscriber")  # Can be different from the file name
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )
        self.cmd_vel_pub = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10
        )  # 10 is the queue size
        self.get_logger().info("Turtle Controller Node has been started.")

    def pose_callback(self, pose: Pose) -> None:
        self.get_logger().info(
            f"Received pose: x={pose.x}, y={pose.y}, theta={pose.theta}"
        )

        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
