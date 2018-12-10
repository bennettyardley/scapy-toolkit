from scapy.all import *
import urllib.request as urllib2
import json
import codecs

#Initalize some variables
macList = []
 = []
i = 0

#Send an ARP request to every device on the IP Range
iprange = "192.168.1.1/24"
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=iprange),
              timeout=2)

#Get a list of all the MAC address for lookup
for snd,rcv in ans:
    macList.append(rcv.sprintf(r"%Ether.src%"))

#Lookup the MAC address to find a vendor
def macLookup(macAddr):
    site = "http://macvendors.co/api/"
    request = urllib2.Request(site+macAddr, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen(request)
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))
    vendorList.append((obj['result']['company']))

#Pass each MAC address into the API
for item in macList:
    macLookup(item)

#Print the data
for snd,rcv in ans:
    print("IP Address: " + rcv.sprintf(r"%ARP.psrc%") + " MAC Address: " + rcv.sprintf(r"%Ether.src%") + " " + vendorList[i])
    i = i + 1
