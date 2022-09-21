import os
import smtplib
from email.message import EmailMessage   

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#list of multiple receivers
candidates = []

msg = EmailMessage()
msg['Subject'] = 'Short-listed for role of ABC'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(candidates)   #or candidates(list of multiple receivers)
msg.set_content(""" 
We are pleased to inform you that 
our team has short-listed you for the next round of this recruiting process.
Please click below for a short coding test.

http://localhost:5000/
""")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)