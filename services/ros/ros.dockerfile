FROM ros:humble as dev

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY src /workspace/src/

# Build the ROS2 workspace
RUN . /opt/ros/humble/setup.sh && colcon build

# Source the ROS2 setup script
RUN echo "source /opt/ros/humble/setup.sh" >> ~/.bashrc
# RUN echo "source /ros2_ws/install/setup.sh" >> ~/.bashrc

# Set the entrypoint
# ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.sh && source /ros2_ws/install/setup.sh && bash"]
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.sh && bash && python3 src/main.py"]
