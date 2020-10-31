import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import current_app as app
from socket import gaierror

class EmailUtil:

    def __init__(self):
        self.host = app.config['SMTP_SERVER']
        self.port = app.config['SMTP_PORT']
        self.sender = app.config['EMAIL_ID']

        if "PASSWORD" in app.config and app.config['PASSWORD']:
            self.password = app.config['PASSWORD']
        else:
            self.password = None

    def message(self, msg_str, subject, receivers, cc, msg_type="plain"):
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = ", ".join(receivers)
        msg["Cc"] = ", ".join(cc)

        msg.attach(MIMEText(msg_str, msg_type))
        return msg.as_string()            

    def send_mail(self, message, receivers):
        try:
            if self.password:
                with smtplib.SMTP_SSL(self.host, self.port) as smtp:
                    smtp.login(self.sender, self.password)
                    smtp.sendmail(self.sender, receivers, message)

        except (gaierror, ConnectionRefusedError):
            app.logger.info('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            app.logger.info('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            app.logger.error(e)