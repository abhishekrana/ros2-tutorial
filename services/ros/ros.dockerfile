FROM ros:humble as dev

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-ros2cli \
    ros-humble-demo-nodes-cpp \
    ros-humble-rqt-graph \
    libgl1-mesa-glx \
    libxkbcommon-x11-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY src /workspace/src/

# Build the ROS2 workspace
# RUN . /opt/ros/humble/setup.sh && colcon build

# Source the ROS2 setup script
RUN echo "source /opt/ros/humble/setup.sh" >> ~/.bashrc && \
    echo "source /opt/ros/humble/local_setup.bash" >> ~/.bashrc

# Set the entrypoint
ENTRYPOINT ["/bin/bash", "-c", "export DISPLAY=${DISPLAY} && python3 src/main.py"]
