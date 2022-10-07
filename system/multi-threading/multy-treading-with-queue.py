import requests
from threading import Thread
from queue import Queue
import os
from time import perf_counter

q = Queue()
n_threads = 5
buffer_size = 1024


def download():
    global q
    while True:
        url = q.get()
        response = requests.get(url, stream=True)
        filename = './multy-t-with-q/'+url.split("/")[-1]
        if not os.path.exists('./multy-t-with-q/'):
            os.mkdir('./multy-t-with-q/')

        with open(filename, "wb") as f:
            for data in response.iter_content(buffer_size):
                # write data read to the file
                f.write(data)
        # we're done downloading the file
        q.task_done()


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
        q.put(url)
    for t in range(n_threads):
        worker = Thread(target=download)
        worker.daemon = True
        worker.start()
    q.join()
    print(f"Time took: {perf_counter() - t:.2f}s")
