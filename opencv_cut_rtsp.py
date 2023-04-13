# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/16 14:25
# @File    : opencv_cut_rtsp.py
# @Author  : zyy
# @Comment : 使用OpenCV截取rtsp视频流
"""
import cv2

# 获取视频流
cap = cv2.VideoCapture('rtsp地址') 
# 指定编码格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 保存视频的编码
# cv2.VideoWriter的参数分别为：保存路径，编码格式，帧率，帧大小
out = cv2.VideoWriter('1.mp4', fourcc, 30, (1280, 720))

while cap.isOpenend():
    ret, frame = cap.read()
    if ret:
        # 如果帧的大小与自定义参数不一致，需要resize
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destoryAllWindows()
