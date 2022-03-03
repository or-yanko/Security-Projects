from random import randint
# Both the persons will be agreed on the
# public keys G and P

# A prime number P is taken
# A primitive  root for P, G is taken
P = 283
G = 47

class Alice:
    def __init__(self):
        self.a = randint(1, P)
    def publish(self):
        return int(pow(G, self.a, P))
    def compute_secret(self, gb):
        return int(pow(gb, self.a, P))

class Bob:

    def __init__(self):
        self.b = randint(1, P)

    def publish(self):
        return int(pow(G, self.b, P))

    def compute_secret(self, ga):
        return int(pow(ga, self.b, P))


def main():
    alice = Alice()
    bob = Bob()
    print('Alice selected: %s' % alice.a)
    print('Bob selected: %s' % bob.b)
    ga = alice.publish()
    gb = bob.publish()
    print('Alice published: %s' % ga)
    print('Bob published: %s' % gb)
    sa = alice.compute_secret(gb)
    sb = bob.compute_secret(ga)
    print('Alice computed: %s' % sa)
    print('Bob computed: %s' % sb)
if __name__ == '__main__':
    main()
