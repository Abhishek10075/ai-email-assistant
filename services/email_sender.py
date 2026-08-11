"""Email sending service for SmartMail AI."""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def send_email(
    sender_email: str,
    sender_app_password: str,
    recipient_email: str,
    subject: str,
    body: str
) -> None:
    """
    Send an email via Gmail SMTP using credentials provided at runtime.

    Args:
        sender_email: The Gmail address to send from.
        sender_app_password: That account's 16-char Gmail App Password.
        recipient_email: The address to send to.
        subject: Email subject line.
        body: Email body text.

    Raises:
        smtplib.SMTPException: If sending fails.
    """
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(sender_email, sender_app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())