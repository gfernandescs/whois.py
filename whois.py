#!/usr/bin/python
import socket,sys

# ==============================================================================
# Variaveis
# ==============================================================================

sock = False
whois_from_iana = ""

# ==============================================================================
# Constantes
# ==============================================================================

IANA_HOST = "whois.iana.org"


def banner():
	print "--------------------------------------------------------------------------"
	print "------------------| Whois -- By Foo0T |-----------------------------------"
	print "------------| Uso padrao: python  "+sys.argv[0]+" www.alvo.com |----------"
	print "--------------------------------------------------------------------------"

def basicCheck():
	if len(sys.argv) < 2:
		banner()
		sys.exit()

def get_whois_from_iana():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((IANA_HOST,43))
	sock.send(sys.argv[1]+"\r\n")

	resp = sock.recv(1024).split()

	return resp[19]

def get_whois_from_specific_location(whois_from_iana):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((whois_from_iana,43))
	sock.send(sys.argv[1]+"\r\n")

	resp = sock.recv(1024)

	return resp
	
def main():
	basicCheck()

	whois_from_iana = get_whois_from_iana()

	whois_from_specific_location = get_whois_from_specific_location(whois_from_iana)
	
	print whois_from_specific_location

main()



