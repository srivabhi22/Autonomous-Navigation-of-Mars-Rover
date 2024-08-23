#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2

def process_point_cloud(data):
    # Extract the (x, y, z) coordinates of interest
    rospy.loginfo("Processing point cloud data")

def point_cloud_processor_node():
    rospy.init_node('point_cloud_processor_node', anonymous=True)
    
    rospy.Subscriber("/zed/zed_node/point_cloud/cloud_registered", PointCloud2, process_point_cloud)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        point_cloud_processor_node()
    except rospy.ROSInterruptException:
        pass
