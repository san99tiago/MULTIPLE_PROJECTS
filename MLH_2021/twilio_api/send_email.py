# SEND EMAILS USING TWILIO API IN PYTHON
# Santiago Garcia Arango

# --------------------------------------------
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# --------------------------------------------


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='santiago.garcia1999@hotmail.com',
    to_emails='jjj.1998@hotmail.com',
    subject='MY FIRST AUTOMATED EMAIL BY SAN99TIAGO!!',
    html_content='<strong>Twilio is amazing and the best part is that \
        I programmed it completely in Python!!! <br><br><br> \
        This is a daily challenge for the Major League Hacking 2021. <br> \
        Best regards, <br><br>\
        Santiago Garcia Arango</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print("ERROR:", e)
