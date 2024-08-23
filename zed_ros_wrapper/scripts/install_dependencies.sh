#!/bin/bash

# Install ROS and ZED dependencies
sudo apt-get update
sudo apt-get install -y ros-noetic-vision-msgs ros-noetic-image-transport ros-noetic-tf2-geometry-msgs ros-noetic-cv-bridge

# Install Python dependencies
pip install -r requirements.txt

echo "Dependencies installed successfully."
