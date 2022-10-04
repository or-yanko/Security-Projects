import requests
from threading import Thread, Lock
from queue import Queue
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


q = Queue()
list_lock = Lock()
discovered_domains = []


def scan_subdomains(domain):
    global q
    while True:
        subdomain = q.get()
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            slowprint("[+] Discovered subdomain: " + url, slow=0)
            with list_lock:
                discovered_domains.append(url)
        q.task_done()


def main(domain, n_threads, subdomains):
    global q

    for subdomain in subdomains:
        q.put(subdomain)

    for t in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()


if __name__ == "__main__":
    slowprint("[?] welcome to or yankos fastttt subdomain scanner.\n[?] please ter domain name (example 'google.com', 'netflix.com'):")
    domain = input().replace(' ', '')
    wordlist = "sub-domains.txt"
    slowprint("[?] please enter num of threads to work on:")
    num_threads = int(input().replace(' ', ''))
    output_file = domain+'-subdomain.txt'

    main(domain=domain, n_threads=num_threads,
         subdomains=open(wordlist).read().splitlines())
    q.join()

    # save the file
    with open(output_file, "w") as f:
        for url in discovered_domains:
            print(url, file=f)
