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

    def pose_callback(self, msg: Pose) -> None:
        self.get_logger().info(
            f"Received pose: x={msg.x}, y={msg.y}, theta={msg.theta}"
        )

        # Move the turtle to the right
        if msg.x < 8:
            msg1 = Twist()
            msg1.linear.x = 1.0
            msg1.angular.z = 0.0
            self.cmd_vel_pub.publish(msg1)

        if msg.x > 8:
            msg1 = Twist()
            msg1.linear.x = 0.0
            msg1.angular.z = 0.0
            self.cmd_vel_pub.publish(msg1)
            self.get_logger().info("Reached the destination.")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
