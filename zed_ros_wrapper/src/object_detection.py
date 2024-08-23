#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2

def detect_objects(data):
    # Implement object detection logic
    rospy.loginfo("Detecting objects in the point cloud")

def object_detection_node():
    rospy.init_node('object_detection_node', anonymous=True)
    
    rospy.Subscriber("/zed/zed_node/point_cloud/cloud_registered", PointCloud2, detect_objects)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        object_detection_node()
    except rospy.ROSInterruptException:
        pass
