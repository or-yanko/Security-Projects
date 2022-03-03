import json
import socket
import os
import sys
import time
import hash1
from termcolor import colored
import random

ip = ''
port = 0

#--------------------------work--------------------------
def xorData(data, key):
    data.replace('\n','. ')
    enc = ''
    k = int(key) % 127
    for letter in data:
        enc += chr(k ^ ord(letter))
    return enc

def encyptOrDecrypt(data, keyList):
    split_strings = []
    x = 0
    for index in range(0, len(data), 10):
        split_strings.append( xorData(data[index : index + 10], keyList[x]))

        x+=1
    return ''.join(split_strings)



##--------------------dont work yet----------------------

def reliable_recv(s):
    data = ''
    b = 0
    gplist =[]
    while True:
        try:

            b = random.randint(0,200)
        except ValueError:
            continue


def recv(s):
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
