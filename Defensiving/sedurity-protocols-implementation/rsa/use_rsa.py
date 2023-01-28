from rsa_ import *

public = 0
private = 0
ans = input("generate keys? y/n")
if ans.lower() == 'y':
    bit_length = int(input("Enter bit_length: "))
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2**bit_length)
    print("Public Key: ", public)
    print("Private Key: ", private)

elif ans.lower() == 'n':
    p = input('enter public key like "24863, 60653":\t').replace(
        ' ', '').split(',')
    public = tuple([int(i) for i in p])
    p = input('enter private key like "587,60653":\t').replace(
        ' ', '').split(',')
    private = tuple([int(i) for i in p])

msg = input("Write msg: ")

print("Running RSA...")
encrypted_msg = encrypt(msg, public)
print("\nEncrypted msg:\n-------------")
print(''.join(map(lambda x: str(x), encrypted_msg)))
print("\nDecrypted msg:\n-------------")
print(decrypt(encrypted_msg, private))
