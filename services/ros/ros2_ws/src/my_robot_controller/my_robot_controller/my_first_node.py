#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self) -> None:
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1, self.timer_callback)

    def timer_callback(self) -> None:
        self.get_logger().info("Hello from timer " + str(self.counter_))
        self.counter_ += 1


def main(args=None) -> None:
    rclpy.init(args=args)

    # Can also create multiple nodes from the same program
    node = MyNode()

    # Keep node running until stopped (e.g. Ctrl+C). Returns when Ctrl+C is pressed.
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
