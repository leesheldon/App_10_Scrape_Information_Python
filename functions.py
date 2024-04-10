import requests
import selectorlib
import smtplib
import ssl
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(raw_message):
    host = "smtp.gmail.com"
    port = 465

    username = "lhanco@gmail.com"
    password = os.getenv("Python_App_Send_Email")

    receiver = "lhanco@gmail.com"
    context = ssl.create_default_context()

    message = f"""\
Subject: New event

From: lhanco@gmail.com

    {raw_message}
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent!")
