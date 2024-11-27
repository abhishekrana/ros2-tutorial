#!/usr/bin/env python3

from functools import partial

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


class TurtleControllerNode(Node):
    def __init__(self) -> None:
        super().__init__("pose_subscriber")  # Can be different from the file name
        self.previous_x_ = 0.0
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

        # ros2 topic hz /turtle1/pose # 60 Hz i.e. this callback is called 60 times per second
        # So we add condition (using previous_x_) to only call the service when we cross the middle.
        if pose.x > 5.5 and self.previous_x_ <= 5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Changing pen color to red.")
            self.call_set_pen_service(255, 0, 0, 3, 0)
        elif pose.x <= 5.5 and self.previous_x_ > 5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Changing pen color to blue.")
            self.call_set_pen_service(0, 0, 255, 3, 0)

    def call_set_pen_service(self, r, g, b, width, off) -> None:
        # ros2 run turtlesim turtlesim_node
        # ros2 service type /turtle1/set_pen
        # turtlesim/srv/SetPen
        # ros2 interface show turtlesim/srv/SetPen
        # uint8 r
        # uint8 g
        # uint8 b
        # uint8 width
        # uint8 off
        # ---
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service not available, waiting again...")

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future) -> None:
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
