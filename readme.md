
# 1 环境依赖

1. 基本依赖

~~~python
# 1 VisionProStreamer的依赖
pip install grpcio protobuf numpy
~~~

2. `vision pro`获取姿态

~~~python
from vision_pro import VisionProStreamer
avp_ip = "192.168.8.214"   # 改成vision pro上的IP
s = VisionProStreamer(ip = avp_ip, record = False)

while True:
    r = s.latest
    print(r['left_pinch_distance'] r['left_wrist_rpy']， r['left_wrist'], r['right_fingers'])
    time.sleep(0.2)
~~~~

3. 获取的姿态说明

~~~python
r['head'] r['right_wrist'], r['right_fingers']
head                  # 头部

left_pinch_distance   # 捏夹距离   r['left_pinch_distance']
left_wrist            # 腕部姿态   r['left_wrist'][0]
left_fingers          # 手指动作   r['right_fingers']       [25, 3, 3]
left_wrist_rpy        # 腕部角度   r['left_wrist_rpy']

right_wrist           #           r['right_wrist'][0]
right_fingers
right_wrist_rpy
right_pinch_distance
~~~


# 2 手指映射

`vision pro`获取的手部检测示意图
![](./assets/hand_skeleton_convention.png)

1. 计算`index[6,5,9]`食指的角度, 即计算向量 $V_{65}$ 与向量 $V_{69}$ 的夹角即可
+ 向量余弦定理计算夹角`->`角度上下位限制`->`角度映射到实际手范围

2. 计算大拇指： `bending_angle[1, 4, 6]`  `rotation_angle[6, 3, 21]`
3. 因时灵巧手底层顺序`little、ring、middle、index、thumb_bending、thumb_rotation`


# 3 手臂逆解

+ 带约束的最小二乘，二次规划