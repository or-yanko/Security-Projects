from aes import encrypt, decrypt
key = 'A?D(G+KaPdSgVkYp3s6v9y$B&E)H@McQ'
txt = input('enter text: ')
print("\nuse aes\n-------------")
c = encrypt(key, txt)
print("cypher text: ", c)
p = decrypt(key, c)
print("plain text: ", p)
