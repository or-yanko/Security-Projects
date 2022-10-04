import requests
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


if __name__ == "__main__":
    slowprint("[?] welcome to or yankos subdomain scanner.\n[?] please ter domain name (example 'google.com', 'netflix.com'):")
    domain = input().replace(' ', '')
    file = open("sub-domains copy.txt")
    content = file.read()
    subdomains = content.splitlines()
    discovered_subdomains = []
    slowprint('[+] start scanning all domains...\n')
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=4)
        except requests.ConnectionError:
            pass
        else:
            slowprint("[+] Discovered subdomain: " + url)
            discovered_subdomains.append(url)
    slowprint('\n[+] scan has been finished successfully')

    slowprint('[+] start saving all subdomain to '+domain+'-subdomain.txt')
    fname = domain+'-subdomain.txt'
    with open(fname, "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
    slowprint('[+] saved successfully to '+domain+'-subdomain.txt')
