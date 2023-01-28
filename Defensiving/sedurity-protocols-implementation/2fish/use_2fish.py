from twofish import *
__testkey = b'\xD4\x3B\xB7\x55\x6E\xA3\x2E\x46\xF2\xA2\x82\xB7\xD4\x5B\x4E\x0D\x57\xFF\x73\x9D\x4D\xC9\x2C\x1B\xD7\xFC\x01\x70\x0C\xC8\x21\x6F'
__testdat = input('enter data to encrtpt: ').encode("utf-8")
while len(__testdat) % 16 != 0:
    __testdat += b' '
tf = Twofish(__testkey)
print('plaintext: ', __testdat)
ct = tf.encrypt(__testdat)
print('cypher text: ', ct)
pt = tf.decrypt(ct).decode("utf-8")
print('plaintext: ', pt)

exit(0)
