import requests
from tqdm.auto import tqdm


def download_online_file_with_loadingbar(url):
    filename = url.split('/')[-1]
    resp = requests.get(url, stream=True)
    pbar = tqdm(desc=filename, total=int(resp.headers.get('content-length', 0)),
                unit='B', unit_scale=True, unit_divisor=1024,)
    with open(filename, 'wb') as fi:
        for data in resp.iter_content(chunk_size=1024):
            fi.write(data)
            pbar.update(len(data))
    pbar.close()


if __name__ == '__main__':
    url = 'https://wordnetcode.princeton.edu/2.1/WNsnsmap-2.1.tar.gz'
    download_online_file_with_loadingbar(url)
