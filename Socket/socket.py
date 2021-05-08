# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:53:41 2021

@author: Jan Binkowski
"""


import socket

host = "info.cern.ch" 
port = 80  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
client.connect((host, port))  
 
print("Connecting successful!\n")

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % (host)

print(request)

client.sendall(request.encode())  
response = client.recv(4096)  
client.close
outFile = open("message.txt", "w")
outFile.write(response.decode('utf-8'))
outFile.close()

