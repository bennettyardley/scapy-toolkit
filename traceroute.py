from scapy.all import *

hostname = input("Enter hostname or IP for traceroute: ")

for i in range(1, 30):
    packet = IP(dst=hostname, ttl=i) / UDP(dport=33434)
     = sr1(packet, verbose=0)
    if response is None:
        break
    elif response.type == 3:
        print ("Final Hop " + response.src)
        break
    else:
        print (str(i) + " " + response.src)
