#!/usr/bin/python

import  thread
import  time

def  a():

	while  3 > 2 :

		print   "Helloo"
		time.sleep(1)


def   b():


	while  3  > 1  :
		print   "HIiiiiiiiiii"
		time.sleep(2)

thread.start_new_thread(a,())
thread.start_new_thread(b,())

while   4 >  2  :
	pass











