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
# my_robot_controller is package name
# test_node is executable name
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
