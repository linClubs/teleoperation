#!/home/lin/software/miniconda3/envs/yolo/bin/python3
# coding=utf-8
from vision_pro import VisionProStreamer
import time
from pytransform3d import rotations 
import numpy as np

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

avp_ip = "192.168.8.214"
deg2rad = 3.14 / 180
rad2deg = 180 / 3.14


class VisionNode(Node):
    def init__(self):
        super().__init__('tf_publisher')
        print("init vision_node")
        self.s = VisionProStreamer(ip = avp_ip, record = False)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.timer_callback)  # 每

    def timer_callback(self):

        r = self.s.latest

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'map'
        t.child_frame_id = 'left_hand'
        
        left_wrist_pose = r['left_wrist']

        q = rotations.quaternion_from_matrix(left_wrist_pose[:3, :3])
        print(q)


        t.transform.translation.x = 1.0
        t.transform.translation.y = 1.0
        t.transform.translation.z = 1.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        # 发布变换
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    tf_publisher = VisionNode("vision_node")
    rclpy.spin(tf_publisher)
    tf_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    print("qqq")
    main()