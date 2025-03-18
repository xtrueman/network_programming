#!/usr/bin/env python3

from pprint import pprint
import socket

hostname = "example.com"
ip_address = socket.gethostbyname(hostname)
#print(ip_address) # 142.250.74.78

addresses = socket.gethostbyname_ex(hostname)
# -> (name, aliaslist, addresslist)
# print(addresses)
# ('example.com', [], ['23.192.228.84', '23.215.0.136', '23.215.0.138', '96.7.128.175', '96.7.128.198', '23.192.228.80'])

# getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
addr_info = socket.getaddrinfo('google.com', None, socket.AF_INET6)
# [(family, type, proto, canonname, sockaddr)]
pprint(addr_info)
# [(<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_DGRAM: 2>, 17 (socket.IPPROTO_TCP), '', ('::ffff:142.250.74.78', 0, 0, 0)),
#  (<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_STREAM: 1>, 6 (socket.IPPROTO_UDP), '', ('::ffff:142.250.74.78', 0, 0, 0))]
