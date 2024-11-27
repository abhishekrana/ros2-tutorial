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

Topics

```bash
$:/workspace# ros2 topic list
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose

$:/workspace# ros2 topic info /turtle1/cmd_vel
Type: geometry_msgs/msg/Twist
Publisher count: 0
Subscription count: 1

$:/workspace# ros2 interface show geometry_msgs/msg/Twist
# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
        float64 x
        float64 y
        float64 z
Vector3  angular
        float64 x
        float64 y
        float64 z
```

Services

- Services are used for
  1. Computation
  2. Change of settings

```bash
$:/workspace# ros2 interface show example_interfaces/srv/AddTwoInts
# Request
int64 a
int64 b
---
# Response
int64 sum
```

```bash
$:/workspace# ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{'a': 2, 'b': 5}"
requester: making request: example_interfaces.srv.AddTwoInts_Request(a=2, b=5)

response:
example_interfaces.srv.AddTwoInts_Response(sum=7)
```

```bash
$:/workspace# ros2 run turtlesim turtlesim_node

$:/workspace# ros2 service list
/clear
/kill
/reset
/rqt_gui_py_node_1444/describe_parameters
/rqt_gui_py_node_1444/get_parameter_types
/rqt_gui_py_node_1444/get_parameters
/rqt_gui_py_node_1444/list_parameters
/rqt_gui_py_node_1444/set_parameters
/rqt_gui_py_node_1444/set_parameters_atomically
/spawn
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/describe_parameters
/turtlesim/get_parameter_types
/turtlesim/get_parameters
/turtlesim/list_parameters
/turtlesim/set_parameters
/turtlesim/set_parameters_atomically

$:/workspace# ros2 service type /turtle1/set_pen
turtlesim/srv/SetPen

$:/workspace# ros2 interface show turtlesim/srv/SetPen
uint8 r
uint8 g
uint8 b
uint8 width
uint8 off
---

$:/workspace# ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{'r': 255, 'g': 0, 'b': 0, 'width': 3, 'off': 0}"
waiting for service to become available...
requester: making request: turtlesim.srv.SetPen_Request(r=255, g=0, b=0, width=3, off=0)

response:
turtlesim.srv.SetPen_Response()
```
