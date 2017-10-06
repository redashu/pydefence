#!/usr/bin/python

import  socket
import	commands 

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("127.0.0.1",3333))


while  3 > 2 :

	data =  x.recvfrom(100)
	print  "______________________"
	print "Cmd rcvd:", data[0]
	print  "______________________"
	reply = commands.getstatusoutput(data[0])
	if reply[0] != 0:
	  x.sendto("Invalid Command",data[1])
	if not reply[1]:
	  x.sendto("Cmd executed successfully",data[1])
	x.sendto(reply[1],data[1])
