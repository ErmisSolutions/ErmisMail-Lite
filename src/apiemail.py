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

    def sendMail(self, to:str, name:str, fromEmail:str, subject:str, message:str):
        try:
            with smtplib.SMTP_SSL(self._server, self._port, ssl.create_default_context()) as smtp:
                smtp.login(self._username, self._password)

                emailMessage = MIMEMultipart("alternative")
                emailMessage["Subject"] = subject
                emailMessage["From"] = self._username
                emailMessage["To"] = to

                finalMessage: str = f"Name: {name}\nEmail: {fromEmail}\nSubject: {subject}\n\n{message}"

                emailMessage.attach(MIMEText(finalMessage, "plain"))

                smtp.sendmail(self._username, to, emailMessage.as_string())
                return True
        except Exception as ex:
            return ex