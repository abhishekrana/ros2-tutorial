# ros2-tutorial

## Setup

```bash
./bootstrap.sh && bash
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

## References

- [ROS2 Tutorials - ROS2 Humble For Beginners](https://www.youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy)
