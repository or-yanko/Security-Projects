import socket
from IPy import IP


###nsloookup <url of website (www...)>  => gives you the ip of the website

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port', port, ':', banner)
        except:
            print('[+] Open Port', port)
    except:
        pass


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target]', str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)


if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan(split targets with comma :\",\") : ')
    if ',' in targets:
        for ipAdd in targets.split(','):
            scan(ipAdd.strip(' '))
    else:
        scan(targets)
