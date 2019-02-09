#!/usr/bin/python
import socket,sys

if len(sys.argv) < 2:
	print "------------------------------------------------------------'-"
	print "------------------| Whois -- By Foo0T |-----------------------"
	print "------------| Uso padrao: python  "+sys.argv[0]+" www.alvo.com |----------"
	print "-------------------------------------------------------------'"
	sys.exit()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("200.160.2.3",43))
socket.send(sys.argv[1]+"\r\n")

resp = socket.recv(1024)
print resp
