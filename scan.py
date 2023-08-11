#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

host = input("Adresse ip à scanner : ")
port = int(input("Port à scanner : "))


def portScanner(port):
	if s.connect_ex((host, port)):
		print("Port non-ouvert")
	else:
		print("Port ouvert")
		
portScanner(port)
