import requests
from time import perf_counter
import os

buffer_size = 1024


def download(url):
    response = requests.get(url, stream=True)
    path = './one-t/'+url.split("/")[-1]
    if not os.path.exists('./one-t/'):
        os.mkdir('./one-t/')
    with open(path, "wb") as f:
        for data in response.iter_content(buffer_size):
            f.write(data)


if __name__ == "__main__":
    urls = [
        "https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832__340.jpg",
        "https://cdn.pixabay.com/photo/2013/10/02/23/03/dawn-190055__340.jpg",
        "https://cdn.pixabay.com/photo/2016/10/21/14/50/plouzane-1758197__340.jpg",
        "https://cdn.pixabay.com/photo/2016/11/29/05/45/astronomy-1867616__340.jpg",
        "https://cdn.pixabay.com/photo/2014/07/28/20/39/landscape-404072__340.jpg",
    ] * 5

    t = perf_counter()
    for url in urls:
        download(url)
    print(f"Time took: {perf_counter() - t:.2f}s")
