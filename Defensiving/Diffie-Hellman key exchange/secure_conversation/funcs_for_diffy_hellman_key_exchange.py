from math import sqrt
from os import execlp
from random import randint
import socket
from threading import Thread
import time


client_sockets = set()
separator_token = "<SEP>"


def xorDataWithKey(data='', key=0):
    """get data which is text and key which is number.
    xoring the data with the key and return the xored data."""
    xored_data = ''
    data_lst = list(data)
    for char in data_lst:
        xored_data += chr(ord(char) ^ key)
    return xored_data


def generate_random_number_in_range(min=10, max=15):
    return randint(min, max)


def calculate_capital_A_and_B(g, p, little_letter):
    return (pow(g, little_letter) % p)


def generate_big_prime_number(digits=3):
    if digits < 1:
        print('not valid input to random number')
        exit()
    min = 1
    max = int('9' * digits)
    first_rand = randint(min, max)
    counter = 1
    if is_prime(first_rand):
        return first_rand
    while True:
        if counter+first_rand <= max:
            if(is_prime(counter+first_rand)):
                return counter+first_rand
        if first_rand-counter >= max:
            if(is_prime(first_rand-counter)):
                return first_rand-counter
        counter += 1


def calculate_key(p, capital_letter, little_letter):
    return (pow(capital_letter, little_letter) % p)


def is_prime(n):
    """get a number.
    check if the number is prime and return a boolean value thats represent his prime."""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def primeRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------


def get_my_ip_address():
    return socket.gethostbyname(socket.gethostname())


def socket_after_connection_listen_as_a_server(SERVER_HOST="0.0.0.0", SERVER_PORT=1234):
    try:
        s = socket.socket()
        s.bind(('', SERVER_PORT))
        s.listen(5)
        while True:
            c, addr = s.accept()
            return c, addr
    except KeyboardInterrupt:
        print('socket was closed bye bye')


def connect_to_server_socket(SERVER_HOST="127.0.0.1", SERVER_PORT=1234):
    s = socket.socket()
    #print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    #print("[+] Connected.")
    return s


def recive_msg(sock):
    return sock.recv(1024).decode()


def send_msg(sock, msg):
    return sock.send(msg.encode())

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------


def send_msg_with_diffy_hellman_key_exchange(sock, msg):
    # crate elements
    p = generate_big_prime_number()
    pr = primeRoots(p)
    g = pr[randint(0, len(pr)-1)]
    a = generate_random_number_in_range()
    A = calculate_capital_A_and_B(g, p, a)

    # send g p A
    send_msg(sock, str(g))
    time.sleep(0.001)
    send_msg(sock, str(p))
    time.sleep(0.001)
    send_msg(sock, str(A))

    # recive B
    B = int(recive_msg(sock))

    # claculate the key
    key = calculate_key(p, B, a)

    # ecrypting with key
    encrypted_msg = xorDataWithKey(msg, key)

    # sending the encrypted msg
    send_msg(sock, encrypted_msg)


def recive_msg_with_diffy_hellman_key_exchange(sock):
    # recive g p A
    g = int(recive_msg(sock))
    p = int(recive_msg(sock))
    A = int(recive_msg(sock))

    # crate elements
    b = generate_random_number_in_range()
    B = calculate_capital_A_and_B(g, p, b)

    # claculate the key
    key = calculate_key(p, A, b)

    # send B
    send_msg(sock, str(B))

    # recive encrypted msg
    encrypted_msg = recive_msg(sock)

    # decripting_msg
    decrypted_msg = xorDataWithKey(encrypted_msg, key)

    return decrypted_msg


if __name__ == '__main__':
    pass
"""
    p1 = generate_big_prime_number()
    pr = primeRoots(p1)
    g1 = pr[randint(0, len(pr)-1)]
    a1 = generate_random_number_in_range()
    b1 = generate_random_number_in_range()
    A1 = calculate_capital_A_and_B(g1, p1, a1)
    B1 = calculate_capital_A_and_B(g1, p1, b1)
    ka = calculate_key(p1, B1, a1)
    kb = calculate_key(p1, A1, b1)
    print(f'p:{p1}, g:{g1}\na:{a1}, b:{b1}\nka:{ka} , kb:{kb}\n')"""
