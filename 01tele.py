#!/home/lin/software/miniconda3/envs/yolo/bin/python3
# coding=utf-8
from vision_pro import VisionProStreamer
import time
from pytransform3d import rotations
import numpy as np


deg2rad = 3.14 / 180
rad2deg = 180 / 3.14

avp_ip = "192.168.8.214"   # example IP
s = VisionProStreamer(ip = avp_ip, record = False)

while True:
    r = s.latest
    print(r['left_pinch_distance'])
    print(r['right_pinch_distance'] )
    print(np.array(r['left_wrist_rpy']) * rad2deg)
    
    
    left_wrist = np.array(r['left_wrist'][0])
    # print(left_wrist)
    rpy = rotations.euler_from_matrix(left_wrist[:3,:3], 0, 1, 2, True)
    print(rpy * rad2deg)
    print(left_wrist[:3, 3])
    print('\n')
    time.sleep(0.2)