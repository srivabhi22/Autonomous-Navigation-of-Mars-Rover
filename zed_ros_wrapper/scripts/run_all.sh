#!/bin/bash

# Source the ROS environment
source /opt/ros/noetic/setup.bash
source devel/setup.bash

# Run the launch file for ZED and object detection
roslaunch your_package_name object_detection.launch
