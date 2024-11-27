#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self) -> None:
        super().__init__("first_node")
        self.get_logger().info("Hello from ROS2")


def main(args=None) -> None:
    rclpy.init(args=args)

    # Can also create multiple nodes from the same program
    node = MyNode()

    # Keep node running until stopped (e.g. Ctrl+C). Returns when Ctrl+C is pressed.
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
