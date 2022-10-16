from termcolor import colored
from random import uniform
import time
import sys
import scapy.all as scapy
import re
import socket
import nmap
from urllib.request import urlopen


def scan(ip):
    arp_req_frame = scapy.ARP(pdst=ip)
    broadcast_ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
    answered_list = scapy.srp(
        broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
    result = []
    for i in range(0, len(answered_list)):
        client_dict = {
            "ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
        result.append(client_dict)
    return result


def display_result(result):
    print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
    for i in result:
        print("{}\t{}".format(i["ip"], i["mac"]))


def slowprint(s, col='green', slow=1./100, isChangeSpeed=False):
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
            a = uniform(0, 0.6)
            time.sleep(a)


def main():
    slowprint("hey you!!!\nyha yha youuu....", slow=1./5)
    time.sleep(1)
    slowprint("welcome to or yanko's wifi's clients scanner", slow=1./10)

    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    # Get the address range to ARP
    while True:
        slowprint("yo man enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24),24 means all network.\n or if you are goat and want it automaticly, enter 'auto':")
        ip_add_range_entered = input()
        if ip_add_range_entered.replace(' ', '') == 'auto':
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            s = 'you, ' + str(socket.gethostname()) + \
                ' have the adress ' + str(sock.getsockname()[0])
            slowprint(s)
            net = str(sock.getsockname()[0])
            l1 = net.split('.')
            l1[3] = '0'
            net = '.'.join(l1)
            net += '/24'
            ip_add_range_entered = net
            slowprint("network "+ip_add_range_entered +
                      " is valid.\nstart scanning...")
            break

        elif ip_add_range_pattern.search(ip_add_range_entered):
            slowprint("network "+ip_add_range_entered +
                      " is valid.\nstart scanning...")
            break

    slowprint("""choose the format to show the address: 
1. press 'a' to the formatt: <ip> <mac>
2. press 'b' to the formatt: <ip> <status>
3. press 'c' to the formatt: <mac> <name> <ip>
""")
    c = input()
    if c == 'a':
        scanned_output = scan(ip_add_range_entered)
        display_result(scanned_output)

    if c == 'b':
        nm = nmap.PortScanner()
        nm.scan(hosts=ip_add_range_entered, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for ip, status in hosts_list:
            slowprint('hots\t '+ip+'\t'+status)

    if c == 'c':
        arp_result = scapy.arping(ip_add_range_entered)


if __name__ == '__main__':
    main()
