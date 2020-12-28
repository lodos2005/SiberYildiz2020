from scapy.all import *

ip= IP(dst="85.111.95.19",ttl=64)
tcp = TCP(dport=5555, window=1212)

send(ip/tcp/"USOM")
