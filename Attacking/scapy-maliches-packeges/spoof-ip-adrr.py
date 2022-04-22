##### python a.py 01:02:03:04:05:06



import scapy.all
import sys
from termcolor import colored

layer2 = scapy.all.Ether()
#layer2.show()
layer3 = scapy.all.IP()
#layer3.show()
ipv6 = scapy.all.IPv6()
#ipv6.show()
layer4 = scapy.all.TCP()
#layer4.show()

try:
    mac = str(sys.argv[1])
    ip = str(sys.argv[2])

except:
    print(colored("\n\npython a.py <source mac address> <destination ip address>\npython a.py 01:02:03:04:05:06 192.168.1.59",'red'))
    exit()



layer2 = scapy.all.Ether(src=mac)
#layer2 = scapy.all.Ether(src="01:02:03:04:05:06")
layer3 = scapy.all.Ether(dst=ip)
#layer3 = scapy.all.Ether(dst="192.168.1.59")

send = scapy.all.sendp(layer2/layer3)

scapy.all.load_contrib('mpls')
#myMpls = scapy.all.MPLS()

#send = scapy.all.sendp(layer2/myMpls/layer3/myMpls/layer4)
