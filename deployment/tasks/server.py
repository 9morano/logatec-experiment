import sys
import socket
import os
import threading
import re
import sys
import glob

port = 50000
host = ""

numnodes = int(os.environ['NODES_NUM'])
timeout = int(os.environ['APP_DURATION_MIN'])

# Added 15 min as a reserve considering: 
#  -- 5 min: Docker building and running (in case of the first time build)
#  -- 6 min: Vesna compiling and flashing
#  -- 4 min: in case Vesna resets couple of times during app
timeout = timeout * 60 + (60 * 15)	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.settimeout(timeout)
s.listen(5)

i = 0

def client_thread(conn, addr):

    ip = addr[0]
    filename = '%s.txt' % ip

    with open(os.path.join("results/", filename), "wb") as f:
        print('File opened')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
    print('Done receiving')

    conn.close()
    

if os.path.exists("results/") is False:
	os.system("mkdir -m777 results/")

threads = []
totalthreads = 0

while True:
	if totalthreads == numnodes:
		break
	# print(_thread._count())
	conn, addr = s.accept()
	print('Got connection from', addr)
	totalthreads+=1
	t=threading.Thread(target=client_thread, args=(conn,addr))
	threads.append(t)
	t.start()
    # start_new(client_thread, (conn, addr))

for t in threads:
	t.join()
	
sys.exit()
