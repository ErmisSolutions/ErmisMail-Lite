import smtplib, ssl

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

    def sendMail(self):
        with smtplib.SMTP_SSL(self._server, self._port, ssl.create_default_context()) as smtp:
            smtp.login(self._username, self._password)
