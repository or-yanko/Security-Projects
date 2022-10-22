from time import sleep
import hmac
import base64
import struct
import hashlib
import time
import os
from twilio.rest import Client

secret = 'MNUGC2DBGBZQ===='
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

"""-------------------------------------random generator-------------------------------------------"""


def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h


def get_totp_token(secret):
    x = str(get_hotp_token(secret, intervals_no=int(time.time())//60))
    while len(x) != 6:
        x += '0'
    return x


"""-------------------------------------phone authenticatio----------------------------------------"""


def send_phone_authenticatio(from_phone='+12059418767', to_phone='+972586302004'):
    account_sid = os.environ[TWILIO_ACCOUNT_SID]
    auth_token = os.environ[TWILIO_AUTH_TOKEN]
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"temprerial code is:\t{get_totp_token(secret)}.",
                        from_=from_phone,
                        to=to_phone
                    )


def phone_auth():
    send_phone_authenticatio()
    pss = input('Enter code:\t')
    if pss == get_totp_token(secret):
        print('succesfully sns authenticated')
        return True


"""-------------------------------------email authenticatio----------------------------------------"""


def email_auth(gmail_user='you@gmail.com', gmail_password='P@ssword!'):
    import smtplib

    sent_from = gmail_user
    to = ['me@gmail.com', 'bill@gmail.com']
    subject = 'authentication massage'
    body = f"temprerial code is:\t{get_totp_token(secret)}."

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')


"""--------------------------------------------main------------------------------------------------"""

if __name__ == '__main__':
    phone_auth()
    email_auth()
