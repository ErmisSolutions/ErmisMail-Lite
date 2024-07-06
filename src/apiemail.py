import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Emailer():

    _port = None
    _server = None
    _username = None
    _password = None
    _context = None

    def __init__(self, server, port, username, password) -> None:
        self._server = server
        self._port = port
        self._username = username
        self._password = password

    def sendMail(self, to:str, frm:str, message:str):
        try:
            with smtplib.SMTP_SSL(self._server, self._port, ssl.create_default_context()) as smtp:
                smtp.login(self._username, self._password)

                emailMessage = MIMEMultipart("alternative")
                emailMessage["Subject"] = "Hello World"
                emailMessage["From"] = self._username
                emailMessage["To"] = to

                emailMessage.attach(MIMEText(message, "plain"))

                smtp.sendmail(self._username, to, emailMessage.as_string())
        except Exception as ex:
            return ex