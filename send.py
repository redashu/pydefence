#!/usr/bin/python

import  socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while  3 > 2 :
	msg=raw_input("enter your data  to send :  ")
	x.sendto(msg,("127.0.0.1",3333))
	print  "______________________"
	print  x.recvfrom(100)[0]
	print  "______________________"

