import tarfile
from tqdm import tqdm
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


def compress(tar_file, members):
    tar = tarfile.open(tar_file, mode="w:gz")
    progress = tqdm(members)
    for member in progress:
        tar.add(member)
        progress.set_description(f"Compressing {member}")
    tar.close()


def decompress(tar_file, path, members=None):
    tar = tarfile.open(tar_file, mode="r:gz")
    if members is None:
        members = tar.getmembers()
    progress = tqdm(members)
    for member in progress:
        tar.extract(member, path=path)
        progress.set_description(f"Extracting {member.name}")
    tar.close()


if __name__ == "__main__":
    slowprint(
        "welcome to my compresser.\nwhould you like to compress or decompress? c\d")
    action = input().lower()
    slowprint("enter filename, make sure it is on your current directory")
    path = input()
    if action == 'c':
        slowprint("enter name of file after compress.")
        nextfilename = input()
        compress(f"{nextfilename}.tar.gz", [path])
    elif action == 'd':
        decompress(path, "decompressed")
