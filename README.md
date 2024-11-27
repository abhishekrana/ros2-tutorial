# ros2-tut

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

## NOTES

- Package can have multiple nodes
- ament is the build system
- colcon is the build tool that uses ament

Commands

- ros2 node list
- ros2 node info /first_node
- ros2 topic list
- ros2 topic info /chatter
- ros2 interface show std_msgs/msg/String
- ros2 topic echo /chatter # listen to topic chatter
