# ----- sender.py ------
# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import select
import time


s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]

port = 9999 #int(sys.argv[])

#probably gonna have to change
buf =1024
addr = (host,port)
#s.bind((host,port))
data = sys.stdin.read(buf).encode()
# f=open("a.txt","rb")


data,addr = s.recvfrom(buf)
time_start = time()
kb_total = 0
timeSec = 0

while (data):

        if(s.sendto(data,addr)):

                print("sending ...")
                data = sys.stdin.read(buf).encode()
                time_curr = time.time()
                time_total = time_curr - time_start

                kb_total = kb_total + 1
s.close()

time_total = float("%0.3f" % (time_total))
bytes = kb_total * 1024
kb_seconds = kb_total/time_total
kb_seconds = float("%0.3f" % (kb_secconds))
print("Sent" + str(bytes) + " bytes in " + str(time_total) + " seconds: " + str(kb_seconds) + " kb/s")

