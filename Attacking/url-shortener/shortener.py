import pyshorteners as short
import sys
from termcolor import colored

title = """ _   _ ____  _         ____  _                _                       
| | | |  _ \| |       / ___|| |__   ___  _ __| |_ ___ _ __   ___ _ __ 
| | | | |_) | |       \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
| |_| |  _ <| |___     ___) | | | | (_) | |  | ||  __/ | | |  __/ |   
 \___/|_| \_\_____|   |____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|"""
link = ''


def url_shortener(url='', print_title=False):
    if print_title == True:
        print(title)
    shortener = short.Shortener()
    return shortener.tinyurl.short(link)


try:
    link = sys.argv[1]
except:
    print(colored('please enter enter it in this format:\tpython file.py <url>', 'red'))
    exit()

print(colored(url_shortener(link, True), 'green'))
