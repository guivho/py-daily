# Time-stamp: <2026-02-23 07:56:10 sendnrs.py Guivho>

import datetime, smtplib, ssl, picknrs
from constants import \
    sender_email,\
    sender_password,\
    picked_numbers_email,\
    smtp_server,\
    smtp_port

iso = datetime.datetime.now().isoweekday()
if iso in [2, 3, 6, 7]:
    # only pick on monday and friday
    exit(0)

picked_nrs = picknrs.gofor(0,2)
sender_email = sender_email
password = sender_password
receiver_email = picked_numbers_email
message = f"""\
From: {sender_email}
To: {picked_numbers_email}
Subject: [Nrs] Your picked nrs

{picked_nrs}
https://www.nationale-loterij.be/onze-spelen/euromillions/speel#!single/board
"""

# send message
context = ssl.create_default_context()
with smtplib.SMTP(host=smtp_server, port=smtp_port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
