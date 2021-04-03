#-------receiver.py---------#

#!/usr/bin/env python

from socket import *
import sys
import select
#import time
#import json

host = "0.0.0.0"
port = 9999  # int(sys.argv[1])
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

# Change package size if the thing breaks (Goal:1400 bytes )
buf = 1024
addr = (host,port)
#addr = (port)

#f = open("received.txt",'wb')

#s.settimeout(2)

#total_data = 0
data,addr = s.recvfrom(buf)
# f = open("received.txt",'wb')

try:
	while(data):

		sys.stdout.write(data.decode())
		s.settimeout(2)
		data,addr = s.recvfrom(buf)


except timeout:
       #exit(2)
	sys.stderr.write("File received, exiting. ")
	s.close()
