from termcolor import colored
from random import randint
from random import randint, shuffle, uniform
import time
import sys
#import keyboard

global errlist 
global corlist
global alrtlist

loadingList = [
[11,1,0.2,'cracking your comuter'],
[15,1,0.2,'cracking fgdv comuter'],
[14,1,0.2,'cracking dg comuter'],
[22,1,0.2,'cracking 100.23.435.7 comuter'],
[24,1,0.2,'cracking 7.23.435.7 comuter'],
[26,1,0.2,'cracking 100.23.5.7 comuter'],
[30,1,0.2,'cracking 100.23.435.32 comuter'],
[11,1,0.2,'cracking 100.4.435.7 comuter'],
[11,1,0.2,'sshing 56.4.35.7 comuter'],
[32,1,0.2,'sshing 100.4.5.7 comuter'],
[16,1,0.2,'sshing 10.4.435.7 comuter'],
[11,1,0.2,'sshing 100.4.46.7 comuter'],
[81,1,0.2,'sshing 46.4.46.7 comuter'],
[11,1,0.2,'sshing 100.4.68.7 comuter'],
[41,1,0.2,'sshing 46.4.79.6 comuter'],
[1,1,0.2,'sshing 100.4.64.7 comuter']
]
downloadingRuningList = [
    [23, 'importing data','r',False],
    [23, 'refactoring data','d',False],
    [23, 'importing mate','r',False],
    [23, 'sending data','d',False],
    [23, 'importing data','d',False],
    [23, 'blabalbla data','d',False],
    [23, 'fucking data','d',False],
    [23, 'suck my dick','d',False],
    [23, 'importing img134rge4324','r',True],
    [23, 'importing imgterw24324','d',True],
    [23, 'importing img13453524','r',True],
    [23, 'importing img1h54324','d',True],
    [23, 'importing img1343g5rt424','r',True]
]

# ----------------------------work f-------------------------------
def slowprint(s, col='green', slow=1./200,isChangeSpeed=False):
    if isChangeSpeed ==False:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            time.sleep(slow)
    else:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            a = uniform(0, 0.6)
            time.sleep(a)

def dotmove(n,stime=0.5):
    dot = "."*n
    loading = (f"Loading {dot}")
    print(loading + "   ", end = '\r')
    time.sleep(stime)

def simLoadingDisapear(dots=5, times=1,stime=0.5,subj=''):
    slowprint('start loading '+subj,'cyan')
    for x in range(times):
        for y in range(dots+1):
            dotmove(y,stime)
        for z in range(dots-1,  0, -1):
            dotmove(z,stime)
    slowprint('loading '+subj+' has been finnished successfuly !!!!!!','cyan')
    
def retRandomEmoji():
    i = randint(0,3)
    if i == 0:
        # grinning face
        return "\U0001f600" 
    elif i == 2:
        # grinning squinting face
        return "\U0001F606"
    else:
        # rolling on the floor laughing
        return "\U0001F923"

def loadErrors():
    global errlist
    errlist = open("elist.txt", "r").read().replace('|\n', '|').split('|')
    shuffle(errlist)

def loadCorrects():
    global corlist
    corlist = open("glist.txt", "r").read().replace('|\n', '|').split('|')
    shuffle(corlist)

def loadWarnings():
    global alrtlist
    alrtlist = open("wlist.txt", "r").read().replace('|\n', '|').split('|')
    shuffle(alrtlist)

def loadDataToLists():
    loadCorrects()
    loadErrors()
    loadWarnings()
    
def simulateDownoading(dotNum=20,subject = 'data from desktop', downloadingOrRuning = 'd', isEmoji=False):
    if downloadingOrRuning == 'r':
        print(colored('Start running ' + subject , 'blue'))
    elif downloadingOrRuning == 'd':
        print(colored('Start dowmloading ' + subject , 'blue'))
    
    txt = ''
    if isEmoji == True:
        slowprint(retRandomEmoji()*dotNum,col='magenta',isChangeSpeed=True)
    else:
        slowprint('#'*dotNum,col='magenta',isChangeSpeed=True)

    if downloadingOrRuning == 'd':
        print(colored( '\n' + subject + ' has been downloaded successfuly', 'blue'))
    elif downloadingOrRuning == 'r':
        print(colored( '\n' + subject + ' has been runned successfuly', 'blue'))
# ----------------------------work f-------------------------------



# -------------------------in progres f----------------------------
def main():
    #handle data
    global errlist 
    global corlist
    global alrtlist 
    errlist = []
    corlist = []
    alrtlist = []
    loadDataToLists()
    
    #while loop
    while True:
        '''#stop by pressing a
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break'''

        r = randint(1,100)
        if 0<r<50:
            if len(corlist) == 0:
                loadCorrects()
            slowprint(corlist[0])
            corlist.remove(corlist[0])
        elif 50 <= r <68:
            if len(alrtlist) == 0:
                loadWarnings()
            slowprint(alrtlist[0],'yellow')
            alrtlist.remove(alrtlist[0])
        elif 68 <= r <86:
            if len(errlist) == 0:
                loadErrors()
            slowprint(errlist[0],'red')
            errlist.remove(errlist[0])
        elif 86 <= r <92:
            e = randint(0,len(downloadingRuningList))
            simulateDownoading(downloadingRuningList[e][0],downloadingRuningList[e][1],downloadingRuningList[e][2],downloadingRuningList[e][3])
        elif 92 <= r <=100:
            e = randint(0,len(loadingList))
            simLoadingDisapear(loadingList[e][0],loadingList[e][1],loadingList[e][2],loadingList[e][3])
        else:
            slowprint('...........................................','red')





# -------------------------in progres f----------------------------



main()