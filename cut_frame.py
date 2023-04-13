# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/16 18:06
# @File    : cut_frame.py
# @Author  : zyy
# @Comment : 提取视频帧
"""
import cv2

# 读入视频文件
cap = cv2.VideoCapture(r'D:\天健\防溺水系统\测试视频\8.mp4')

c = 1
if cap.isOpenend():
    # 判断是否正常打开
    ret, frame = cap.read
else:
    ret = False

# 视频帧计数间隔频率
timeF = 100

while ret:
    ret, frame = cap.read()
    if (c % timeF == 0):
        print('开始截取视频第：' + str(c) + '帧')
        # 每隔timeF帧进行提取图像，地址必须是英文的，不能包含中文或中文字符
        cv2.imwrite(r'D:\Datasets\summing\2' + '\\' + str(c // timeF) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
cap.release()