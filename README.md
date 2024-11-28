# ros2-tutorial

## Setup

```bash
./bootstrap.sh
bash

task install:pre-commit
```

## Build

Build and start docker container

```bash
docker:build-ros
docker:start-ros
```

Build ROS code inside docker container

```bash
task docker:exec-ros
source ~/.bashrc
task build
```

## Run

Run turtlesim inside docker container

```bash
task docker:exec-ros
source ~/.bashrc
ros2 run turtlesim turtlesim_node
```

Run robot controller inside docker container

```bash
task docker:exec-ros
source ~/.bashrc
task run-turtle-controller
```

## ROS Commands

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

## References

- [ROS2 Tutorials - ROS2 Humble For Beginners](https://www.youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy)
