import socket
import sys
import os
from os import path
s=socket.socket()

app_dir = str(os.environ['APP_DIR'])

host="193.2.205.19"  #IP address of the server
port=50000

print("Connect to server")
try:
	s.connect((host,port))

except socket.gaierror as err:
	print("Address-related error connecting to server: ", err)
	sys.exit(1)

except socket.error as err:
	print("Connection error: ", err)
	sys.exit(1)

filename= path.relpath("/root/logatec-experiment/applications/" + app_dir + "/node_results.txt")

f=open(filename, "rb")

line=f.read(1024)
while(line):
	s.send(line)
	#print('sent' , repr(line))
	line=f.read(1024)
f.close()

print("Done sending file to server.")

s.close()
