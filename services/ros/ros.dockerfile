FROM ros:humble as dev

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-ros2cli \
    ros-humble-demo-nodes-cpp \
    ros-humble-rqt-graph \
    ros-humble-turtlesim \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# This workspace is an overlay on top of the ROS2 workspace
COPY ros2_ws/src /workspace/ros2_ws/src/

# Build the ROS2 workspace
# RUN . /opt/ros/humble/setup.sh && colcon build

# Source the ROS2 setup script
RUN echo "source /opt/ros/humble/setup.sh" >> ~/.bashrc && \
    echo "source /opt/ros/humble/local_setup.bash" >> ~/.bashrc && \
    echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc && \
    echo "source /workspace/ros2_ws/install/setup.bash" >> ~/.bashrc

# Set the entrypoint
ENTRYPOINT ["/bin/bash", "-c", "python3 ros2_ws/src/main.py"]
