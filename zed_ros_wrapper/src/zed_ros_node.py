#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import String

def zed_camera_node():
    rospy.init_node('zed_camera_node', anonymous=True)

    # Subscribe to the ZED point cloud topic
    rospy.Subscriber("/zed/zed_node/point_cloud/cloud_registered", PointCloud2, point_cloud_callback)

    rospy.spin()

def point_cloud_callback(data):
    # Forward the point cloud data to the processing node
    rospy.loginfo("Point cloud received")

if __name__ == '__main__':
    try:
        zed_camera_node()
    except rospy.ROSInterruptException:
        pass
