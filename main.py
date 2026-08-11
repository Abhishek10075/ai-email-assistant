from dotenv import load_dotenv
load_dotenv()

from getpass import getpass
from services.email_generator import generate_email
from services.email_sender import send_email


def split_subject_and_body(email_text: str):
    """Split generated text into subject and body."""
    lines = email_text.strip().split("\n")
    subject = "No Subject"
    body_lines = lines

    if lines and lines[0].lower().startswith("subject:"):
        subject = lines[0].split(":", 1)[1].strip()
        body_lines = lines[1:]

    body = "\n".join(body_lines).strip()
    return subject, body


def main():
    sender_email = input("Enter your Gmail address: ")
    sender_app_password = getpass("Enter your Gmail App Password: ")

    short_description = input("Enter short description about the email: ")
    email_length = input("Enter email length (Short/Long): ")
    contact_details = input("Enter your contact details: ")

    email_text = generate_email(
        sender_email=sender_email,
        short_description=short_description,
        email_length=email_length,
        contact_details=contact_details
    )

    print("\n" + "=" * 60)
    print("GENERATED EMAIL")
    print("=" * 60)
    print(email_text)

    recipient = input("\nEnter recipient's email to send this: ").strip()
    subject, body = split_subject_and_body(email_text)

    try:
        send_email(sender_email, sender_app_password, recipient, subject, body)
        print(f"\n✅ Email sent successfully to {recipient}")
    except Exception as e:
        print(f"\n❌ Failed to send email: {e}")


if __name__ == "__main__":
    main()