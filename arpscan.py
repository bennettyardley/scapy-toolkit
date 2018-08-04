from scapy.all import *
iprange = "192.168.1.1/24"
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=iprange),
              timeout=2)

for snd,rcv in ans:
    print rcv.sprintf(r"%ARP.psrc%,%Ether.src%")
