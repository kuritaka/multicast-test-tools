#!/usr/bin/python3

import socket
import time

LOCAL_IP = '192.168.0.30'
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not 
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
sock.bind((LOCAL_IP,MCAST_PORT))

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP, 0)
#sock.setsockopt(socket.IPPROTO_IP,
#                socket.IP_MULTICAST_TTL,
#                MULTICAST_TTL,
#                socket.inet_aton(LOCAL_IP))

count = 0
while True:
    message = 'test:{0}'.format(count).encode('utf-8')
    print(message)
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))
    count +=1
    time.sleep(0.5)


# For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
# "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)
# Python 3
#sock.sendto(b"robot", (MCAST_GRP, MCAST_PORT))
# Python 2
#sock.sendto("robot", (MCAST_GRP, MCAST_PORT))
