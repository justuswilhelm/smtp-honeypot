from asyncore import loop
from smtpd import DebuggingServer


if __name__ == "__main__":
    smtp_server = DebuggingServer(('localhost', 25), None)
    try:
        loop()
    except KeyboardInterrupt:
        smtp_server.close()
