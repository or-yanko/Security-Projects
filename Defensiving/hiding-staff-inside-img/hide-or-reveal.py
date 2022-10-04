from email.mime import image
from logging import exception
import cv2
import numpy as np
import sys
import time
from random import uniform
from termcolor import colored
import imageio as iio
from os import listdir, system


def slowprint(s, col='green', slow=1./20, isChangeSpeed=False):
    """Print slower"""
    if isChangeSpeed == False:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            time.sleep(slow)
    else:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            a = uniform(1./25, 0.6)
            time.sleep(a)


def to_bin(data):
    """Convert data to binary format as string"""
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes):
        return ''.join([format(i, "08b") for i in data])
    elif isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


def encode(image_name, secret_data):
    # read the image
    #image = cv2.imread(image_name)
    image = iio.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    slowprint("[*] Maximum bytes to encode:", n_bytes)
    if len(secret_data) > n_bytes:
        raise ValueError(
            "[!] Insufficient bytes, need bigger image or less data.")
    slowprint("[*] Encoding data...")
    # add stopping criteria
    secret_data += "====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_bin(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    for row in image:
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = to_bin(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image


def decode(image_name):
    slowprint("[+] Decoding...")
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]


if __name__ == "__main__":
    slowprint("[?] hello, whuold you like to encode or decode image? e/d")
    ans = input()
    slowprint(
        "[?] please enter filename (it has to be in your current directory!:\n[?] files in your curren folder:")
    try:
        system("ls")
    except:
        system("dir")
    file = input()

    if ans == "e":
        output_image = "encoded_image.PNG"
        slowprint("what massage you want to hide inhere?")
        secret_data = input()
        encoded_image = encode(image_name=file, secret_data=secret_data)
        cv2.imwrite(output_image, encoded_image)
        slowprint("[+] Data encoded successfuly.")
    elif ans == "d":
        decoded_data = decode(file)
        slowprint("[+] Decoded data: '" + decoded_data+"'")

    else:
        slowprint('[-] invalid input!', 'red')
