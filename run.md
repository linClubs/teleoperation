~~~python
pip install grpcio protobuf numpy
~~~


~~~python
r['head'] r['right_wrist'], r['right_fingers']


head                  # 头部

left_pinch_distance   # 捏夹距离
left_wrist            # 腕部姿态
left_fingers          # 手指动作 [25, 3, 3]
left_wrist_rpy        # 腕部角度

right_wrist
right_fingers
right_wrist_rpy
right_pinch_distance
~~~

![](./assets/hand_skeleton_convention.png)

1. 计算`index[6,5,9]`食指的角度, 即计算向量$V_{65}$与向量$V_{69}$的夹角即可
2. 计算大拇指： `bending_angle[1, 4, 6]`  `rotation_angle[6, 3, 21]`
3. 因时底层顺序`little、ring、middle、index、thumb_bending, thumb_rotation`