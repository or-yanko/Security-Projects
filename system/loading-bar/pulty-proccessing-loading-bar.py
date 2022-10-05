import time
from tqdm.auto import tqdm
from concurrent.futures import ThreadPoolExecutor


def worker(thread_number):
    for i in tqdm(range(100), desc=f'thread {thread_number}'):
        time.sleep(0.05*thread_number)


if __name__ == '__main__':
    thread_list = list(range(1, 4))
    with ThreadPoolExecutor() as p:
        p.map(worker, thread_list)
