from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from tqdm import tqdm
import requests
import random

# categories
SSL = 'https://www.sslproxies.org/',
GOOGLE = 'https://www.google-proxy.net/',
ANANY = 'https://free-proxy-list.net/anonymous-proxy.html',
UK = 'https://free-proxy-list.net/uk-proxy.html',
US = 'https://www.us-proxy.org/',
NEW = 'https://free-proxy-list.net/',
SPYS_ME = 'http://spys.me/proxy.txt',
PROXYSCRAPE = 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
PROXYNOVA = 'https://www.proxynova.com/proxy-server-list/'
PROXYLIST_DOWNLOAD_HTTP = 'https://www.proxy-list.download/HTTP'
PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'
PROXYLIST_DOWNLOAD_SOCKS4 = 'https://www.proxy-list.download/SOCKS4'
PROXYLIST_DOWNLOAD_SOCKS5 = 'https://www.proxy-list.download/SOCKS5'
ALL = 'ALL'
PROXYLIST_DOWNLOAD_HTTPS = 'https://www.proxy-list.download/HTTPS'


def print_proxies(inf):
    print("Scrapped Proxies:")
    for item in inf.proxies:
        print('{}:{}'.format(item.ip, item.port))
    print("Total Proxies")
    print(inf.len)
    print("Category of the Proxy")
    print(inf.category)


def proxies_to_str_lst(inf):
    lst = []
    for item in tqdm(inf.proxies, 'convert proxies'):
        lst.append('{}{}:{}'.format('http://', item.ip, item.port))
    return lst


def get_session(proxies):
    session = requests.Session()
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session


if __name__ == "__main__":
    print("getting proxies...")
    scrapper = Scrapper(category=ALL, print_err_trace=False)
    data = scrapper.getProxies()
    print("got proxies!")
    proxies_lst = proxies_to_str_lst(data)
    print("getting session...")
    s = get_session(proxies_lst)
    print("session got")
#    try:
    url = input("enter url to access:\t")
    if url == '':
        url = 'http://mywebsite.com/example'
    print("Request page with IP:", s.get(
        "http://icanhazip.com", timeout=10).text.strip())
    """ ------ methods ------
        response = requests.get(url)
        response = requests.post(url, data={"a": 1, "b": 2})
        response = requests.put(url, data=put_body)
        response = requests.delete(url)
        response = requests.patch(url, data=patch_update)
        response = requests.head(url)
        response = requests.options(url)
        """

#            "http://icanhazip.com", timeout=1.5).text.strip())
#    except Exception as e:
#        print("problema...\n", e)
