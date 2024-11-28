# ros2-tutorial

## Setup

```bash
./bootstrap.sh
bash

task install:pre-commit
```

## Build

```bash
cd ros2_ws
colcon build --symlink-install
source ~/.bashrc
```

## Run

```bash
# ros2 run package_name executable_name
ros2 run my_robot_controller test_node
```

## Create package

```bash
cd ros2_ws/src
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
```

## Commands

Nodes

- ros2 node list
- ros2 node info /first_node

Topics

- ros2 topic list
- ros2 topic info /chatter
- ros2 interface show std_msgs/msg/String
- ros2 topic echo /chatter # listen to topic chatter

Services

- ros2 run demo_nodes_cpp add_two_ints_server
- ros2 service list
- ros2 service type /add_two_ints
- ros2 interface show example_interfaces/srv/AddTwoInts

# References

- ROS2 Tutorials - ROS2 Humble For Beginners https://www.youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy
