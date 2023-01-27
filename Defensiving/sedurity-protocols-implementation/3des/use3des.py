from des3 import *
data = input("Please encrypt my data: ")

print('\ndes encription:\n---------------')
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print("Encrypted: %s" % d)
print("Decrypted: %s" % k.decrypt(d))

print('\n3des encription:\n----------------')
k = triple_des('DESCRYPTFKBIPEDN', 'ECB', "\0\0\0\0\0\0\0\0",
               pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print("Encrypted: %s" % d)
print("Decrypted: ", k.decrypt(d))
