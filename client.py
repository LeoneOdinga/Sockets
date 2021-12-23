#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 56000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        print('Start a conversation:')
        data1 = input()
        if data1:
            s.send(data1.encode())
        else:
            break
        data = s.recv(1024)
        if data :
            print('Server Said:', repr(data))
        else:
            break