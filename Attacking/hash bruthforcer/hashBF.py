#the code find the password thats fit to the has is given
#crack hashes



# 5f4dcc3b5aa765d61d8327deb882cf99 => password || md5
# 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 => password || sha1
import hashlib

typeOfHash = str(input('Which type of hash you want to bruteforce?\t'))
filePath = str(input('Enter path to the file to bruteforce:\t'))
hashToDecrypt = str(input('Enter the hash Value To Bruteforce:\t'))

with open(filePath, 'r') as file:
    for line in file.readlines():
        if typeOfHash.lower() == 'md5':
            hashObject = hashlib.md5(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashToDecrypt:
                print('Found MD5 Password: ', line.strip())
                exit(0)
        if typeOfHash.lower() == 'sha1':
            hashObject = hashlib.sha1(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashToDecrypt:
                print('Found sha1 Password: ', line.strip())
                exit(0)
    print('Password not in file.')
