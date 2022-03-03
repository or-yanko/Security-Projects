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
primelist = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677]
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

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


##--------------------dont work yet----------------------

def send(data, s):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def reliable_send(data, s):
    #p and g generated in array
    length = len(data)//10
    pglst = []
    for i in range (0,length):
        p1 = primelist[random.randint(0,len(primelist)-1)]
        glist = primRoots(p1)
        g1 = glist[random.randint(0,len(glist)-1)]
        pglst.append([p1,g1])

    #generate private num
    a = random.randint(0,200)
    send(, s)



def safe_sent(data, s):
    pass

def safe_recv(data, s):
    pass

reliable_send("hello bro how are you", 1)

    



def main():
    port = input("enter port: ")
    ip = input("enter ip: ")
    print('starting chat with\nip:',ip)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection(s)
