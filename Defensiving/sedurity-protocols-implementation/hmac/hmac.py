import hashlib
k = 'A?e(G+KaPdSgVkYp3s6v9y$B&E)H@McQ'
msg = "hello world!"


def generate_sha256_hmac(msg, key):
    hmac1 = hashlib.sha256(msg.encode()).hexdigest()
    hmac2 = [chr(ord(a) ^ ord(b)) for a, b in zip(hmac1, key)]
    hmac3 = "".join(hmac2)
    hmac = hashlib.sha256(hmac3.encode()).hexdigest()
    return hmac


print(generate_sha256_hmac(msg, k))
