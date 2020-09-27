import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def send_email(author, mail, subject, message):
    email = EmailMessage()
    email['from'] = author
    email['to'] = 'ferreirasebastian@gmail.com'
    email['subject'] = subject

    email.set_content(f'{author} ({mail}) dice: {message}')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(email)
        print('all good done')