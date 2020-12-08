import sys

import socket

def main():

    UDP_IP="169.254.233.201"
    UDP_PORT=9
    MESSAGE='Test'

    print ("UDP target IP:", UDP_IP)
    print ("UDP target port:", UDP_PORT)
    print ("message:", MESSAGE)
    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP
    sock.sendto( bytes(MESSAGE, 'UTF-8'), (bytes(UDP_IP, 'UTF-8'), UDP_PORT) )
