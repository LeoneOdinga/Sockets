#!/usr/bin/env python3
#this is the client file

import socket

HEADER =64
FORMAT = 'utf-8'
HOST = socket.gethostbyname(socket.gethostname())
PORT = 56000
ADDR = (HOST,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def sendMessage(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    connection = True
    while connection:
       print("Please type a message you want to send to the server: ")
       userInput = input()
       sendMessage(userInput)

sendMessage("Disconnected!")
