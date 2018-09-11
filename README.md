# scapy-toolkit
A collection of Scapy scripts for network discovery and pen-testing

## pingscan.py
Sends ICMP (ping) packets to 255 addresses and waits for a response to test if a host is online. This is much slower than the ARP scan.

## arpscan.py
Broadcasts an ARP packet to the network and monitors for responses to test if a host is online. Then looks up the MAC addresses to find the vendor of each device.

## traceroute.py
Runs a traceroute on desired hostname or ip to see what hops the packet takes to get to its destination.
