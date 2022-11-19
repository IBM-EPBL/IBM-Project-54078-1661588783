# export SENDGRID_API_KEY = "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"
# setx SENDGRID_API_KEY "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"


import os

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import Mail


# 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


message = Mail(

    from_email='from_email@example.com',

    to_emails='somanathdas.r@gmail.com',

    subject='Sending with Twilio SendGrid is Fun',

    html_content='<strong>and easy to do anywhere, even with Python</strong>')


sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
print((sg.send(message)).status_code, (sg.send(message)).body, (sg.send(message)).headers)


