import smtplib
import ssl


class AutomatedEmailServer:
    def __init__(self, port, smtp_server):
        self.context = ssl.create_default_context()

        self.sender_email = None
        self.sender_password = None
        self.receiver_email = None

        self.port = port
        self.smtp_server = smtp_server

    def set_sender_profile(self, email, password):
        self.sender_email = email
        self.sender_password = password
        return 0

    def set_receiver_profile(self, email):
        self.receiver_email = email
        return 0

    def send_email(self, title, message):
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
            try:
                server.login(self.sender_email, self.sender_password)
                res = server.sendmail(self.sender_email, self.receiver_email, message)
                return 0
            except Exception as e:
                return 1, e
