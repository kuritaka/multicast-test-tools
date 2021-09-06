#!/usr/bin/python36

import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
LOCAL_IP = '192.168.0.22'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
#mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_ADD_MEMBERSHIP,
                socket.inet_aton(MCAST_GRP) + socket.inet_aton(LOCAL_IP))

while True:
  # For Python 3, change next line to "print(sock.recv(10240))"
  #Python3
  print(sock.recv(10240))
  #Python2
  #print sock.recv(10240)
