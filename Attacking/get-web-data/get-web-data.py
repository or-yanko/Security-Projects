import requests
from urllib.parse import urljoin
import os
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from tqdm import tqdm

total_urls_visited = 0

internal_urls = set()
external_urls = set()


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url, d):
    urls = set()
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in tqdm(soup.findAll("a"), desc=f'scan url in defth:{d}'):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                external_urls.add(href)
            continue
        urls.add(href)
        internal_urls.add(href)
    return urls


def crawl(url, d=3):
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url, d)
    for link in links:
        if d == 1:
            break
        crawl(link, d-1)


def get_all_images(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=20)
    soup = BeautifulSoup(response.html.html, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src") or img.attrs.get(
            "data-src") or img.attrs.get("data-original")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    session.close()
    return urls


def downloadall(urls, pathname):
    total_size_in_bytes = 0
    for url in urls:
        total_size_in_bytes += int(requests.get(url,
                                   stream=True).headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes,
                        desc='downloading imgs', unit='iB', unit_scale=True)
    for url in urls:
        response = requests.get(url, stream=True)
        filename = os.path.join(pathname, url.split("/")[-1])
        block_size = 1024  # 1 Kibibyte
        with open(filename, 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
    progress_bar.close()


url = input(" please enter urls\n ex: 'http://books.toscrape.com'\n")
if url == '':
    url = 'http://books.toscrape.com'
path = './' + url.split('://')[1] + '/'

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

html = session.get(url).content

soup = BeautifulSoup(html, "html.parser")

script_files = []


for script in tqdm(soup.find_all("script"), desc='getting scripts'):
    if script.attrs.get("src"):
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

css_files = []

for css in tqdm(soup.find_all("link"), desc='getting links'):
    if css.attrs.get("href"):
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)


pa = requests.get(url).text.split('\n')
pb = []
for x in tqdm(pa, desc='getting html'):
    if x.replace(' ', '').replace('\t', '') != '':
        pb.append(x)

page = '\n'.join(pb)

if not os.path.exists(path):
    os.mkdir(path)


imagesurls = get_all_images(url)
y = input('whould you like to download all the images? y/n:\t')
if y == 'y':
    pp = path+'images/'
    if not os.path.exists(pp):
        os.mkdir(pp)
    downloadall(imagesurls, pp)


domain_name = urlparse(url).netloc
crawl(url)


print("\n\nTotal script files in the page:", len(script_files))
print("Total CSS files in the page:", len(css_files))
print("Total Internal links:", len(internal_urls))
print("Total External links:", len(external_urls))
print("Total URLs:", len(external_urls) + len(internal_urls))
print("Total images:", len(imagesurls))


with open(f"{path}images.txt", "w") as f:
    for img in imagesurls:
        print(img, file=f)

with open(f"{path}javascript_files.txt", "w") as f:
    for js_file in script_files:
        print(js_file, file=f)

with open(f"{path}css_files.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)

with open(f"{path}page.html", "w") as f:
    print(page, file=f)

with open(f"{path}internal_links.txt", "w") as f:
    for internal_link in internal_urls:
        print(internal_link.strip(), file=f)

with open(f"{path}external_links.txt", "w") as f:
    for external_link in external_urls:
        print(external_link.strip(), file=f)
