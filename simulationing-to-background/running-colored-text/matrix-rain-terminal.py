from termcolor import colored
import time
import os
import random
import sys
from sys import argv


chars_to_print = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                  'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sleepingt = 0.04
try:
    sleepingt = int(argv[1])
except:
    pass
while True:
    rows, columns = os.popen('stty size', 'r').read().split()
    line_width = int(columns)

    str1 = ''
    for i in range(line_width):
        if random.getrandbits(1) == 0:
            str1 += str(random.choice(chars_to_print))
        else:
            str1 += ' '
    print(colored(str1, 'green'))
    time.sleep(sleepingt)
