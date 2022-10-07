from math import sqrt
from random import randint


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


if __name__ == '__main__':
    pass
    """p1 = generate_big_prime_number()
    pr = primeRoots(23)
    for g1 in pr:
        a1 = generate_random_number_in_range()
        b1 = generate_random_number_in_range()
        A1 = calculate_capital_A_and_B(g1, p1, a1)
        B1 = calculate_capital_A_and_B(g1, p1, b1)
        ka = calculate_key(p1, B1, a1)
        kb = calculate_key(p1, A1, b1)
        print(f'p:{p1}, g:{g1}\na:{a1}, b:{b1}\nka:{ka} , kb:{kb}\n')"""