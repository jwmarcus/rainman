import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load environment variables
load_dotenv()


def send_email_via_gmail(subject, message, to_email):
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASS")  # relay-user-python-dev (app password)

    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, to_email, text)
    server.quit()


def main():
    subject = ""
    message = "Take two! Call me in the morning."
    to_email = os.environ.get("TO_EMAIL")

    send_email_via_gmail(subject, message, to_email)


if __name__ == "__main__":
    main()
