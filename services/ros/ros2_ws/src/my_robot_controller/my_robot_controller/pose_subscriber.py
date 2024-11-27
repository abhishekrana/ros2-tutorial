#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSubscriberNode(Node):
    def __init__(self) -> None:
        super().__init__("pose_subscriber")  # Can be different from the file name
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )
        self.get_logger().info("Pose Subscriber Node has been started.")

    def pose_callback(self, msg: Pose) -> None:
        self.get_logger().info(
            f"Received pose: x={msg.x}, y={msg.y}, theta={msg.theta}"
        )


def main(args=None) -> None:
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
