 scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

addr = "192.168.1."

for ending in range(1,255):
    anwser = sr1(IP(dst=addr+str(ending))/ICMP(), timeout=1, verbose=0)
    if anwser:
        print ("Host: " + anwser.src)
