# This file is to base my project on. It also was used to test the SMTP connection and send_email test.

import smtplib
import ssl


def send_email(message):
    port = 465  # for ssl
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # email sent from
    receiver_email = ""  # email received to
    password = ""  # email password or app password

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print("Email sent")
            return res
        except Exception as e:
            print("Email could not be sent")
            print(e)


if __name__ == '__main__':
    res = send_email("Testing AutomatedEmailApp")
    print(res)
