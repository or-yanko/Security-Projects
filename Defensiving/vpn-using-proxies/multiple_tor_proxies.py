import requests
from stem.control import Controller
from stem import Signal


def get_tor_session():
    session = requests.Session()
    session.proxies = {"http": "socks5://localhost:9050",
                       "https": "socks5://localhost:9050"}
    return session


def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)


if __name__ == "__main__":
    s = get_tor_session()
    ip = s.get("http://icanhazip.com").text
    print("IP:", ip)
    renew_connection()
    s = get_tor_session()
    ip = s.get("http://icanhazip.com").text
    print("IP:", ip)
