from scapy.all import *
import logging


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

addr_const = "192.168.1."

for addr in range(1,255):
    ans = sr1(IP(dst=addr_const+str(addr))/ICMP(), timeout=1, verbose=0)
    if ans:
        print ("Host: " + ans.src)
