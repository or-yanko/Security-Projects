from scapy.all import *
from threading import Thread
from faker import Faker
import sys
import time
from random import uniform
from termcolor import colored


def slowprint(s, col='green', slow=1./20, isChangeSpeed=False):
    """Print slower"""
    if isChangeSpeed == False:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            time.sleep(slow)
    else:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            a = uniform(1./25, 0.6)
            time.sleep(a)


"""


if __name__ == "__main__":

    n_ap = args.n_ap
    iface = args.interface

    faker = Faker()

    ssids_macs = [(faker.name(), faker.mac_address()) for i in range(n_ap)]
    for ssid, mac in ssids_macs:
        Thread(target=send_beacon, args=(ssid, mac)).start()
"""


def send_beacon(ssid, mac, infinite=True):
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff",
                  addr2=mac, addr3=mac)
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)


if __name__ == "__main__":
    slowprint('[?] how many access points do you want to upload?')
    n_ap = input()
    iface = "wlan0mon"
    # generate random SSIDs and MACs
    faker = Faker()
    ssids_macs = [(faker.name(), faker.mac_address()) for i in range(n_ap)]
    for ssid, mac in ssids_macs:
        Thread(target=send_beacon, args=(ssid, mac)).start()
