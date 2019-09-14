#! /bin/python/python3

import socket
import sys
import os
import time
import random

lHost = "127.0.0.1"                    #Server IP
port = 1333                     #Connection Port
def Server():
	#Functions
	print("Starting server on port 1333")

	def send(msg):
	    s.send(msg.encode("UTF-8"))
   
	def getInstructions():
	    print(">")
	    while True:
	        msg = s.recv(4096)
	        inst = msg.decode("UTF-8")
       
        #Instructions
       
	if inst == "test":
            try:
                send("Working!")
            except:
                pass
 
#Connection
 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	connected = False
	while connected == False:
	    try:
	        s.connect((host, port))
	        connected = True
	    except:
	        sleepTime = random.randint(20, 30)
	        time.sleep(sleepTime)
	getInstructions()



