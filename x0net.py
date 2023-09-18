# --------------------------- X0Reda ----------------------------
from scapy.all import ARP , Ether , srp
import sys
exist = []
def scan(ip):
          while True:
                     try:
                         arp_reg = ARP(pdst=ip)
                         brodcast = Ether(dst="ff:ff:ff:ff:ff:ff")
                         arp_brodcast = brodcast/arp_reg
                         result = srp(arp_brodcast,timeout=3,verbose=False)[0]
                         print(result)
                         lst = []
                         for element in result:
                                          clients = {"ip":element[1].psrc,"mac":element[1].hwsrc}
                                          lst.append(clients)
                         for i in lst:
                                     if i["mac"] not in exist:
                                      print ("{} /t/t/t/t {} /n".format(i['ip'],i['mac']))
                                     exist.append(i['mac'])
                     except:
                             print("/exit..!")
                             sys.exit()
ip = str(input("enter ip:"))
scan(ip)  
