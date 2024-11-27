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

```bash
root@0d6f6d5da78b:/workspace# ros2 topic list
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

root@0d6f6d5da78b:/workspace# ros2 topic info /turtle1/cmd_vel
Type: geometry_msgs/msg/Twist
Publisher count: 0
Subscription count: 1

root@0d6f6d5da78b:/workspace# ros2 interface show geometry_msgs/msg/Twist
# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
        float64 x
        float64 y
        float64 z
Vector3  angular
        float64 x
        float64 y
        float64 z
root@0d6f6d5da78b:/workspace#
```
