from dotenv import load_dotenv
load_dotenv()

import os
from services.email_generator import generate_email
from services.email_sender import send_email


def main():
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_app_password = os.getenv("EMAIL_APP_PASSWORD")

    if not sender_email or not sender_app_password:
        print("❌ EMAIL_ADDRESS or EMAIL_APP_PASSWORD missing in .env file")
        return

    recipient = input("Enter email where the email should be sent: ").strip()
    subject = input("Enter subject: ").strip()
    short_description = input("Enter short description about the email: ")
    contact_details = input("Enter contact details: ")

    body = generate_email(
        subject=subject,
        short_description=short_description,
        contact_details=contact_details
    )

    print("\n" + "=" * 60)
    print("EMAIL PREVIEW")
    print("=" * 60)
    print(f"To: {recipient}")
    print(f"Subject: {subject}\n")
    print(body)
    print("=" * 60)

    confirm = input("\nSend email? (yes/no): ").strip().lower()

    if confirm == "yes":
        try:
            send_email(sender_email, sender_app_password, recipient, subject, body)
            print(f"\n✅ Email sent successfully to {recipient}")
        except Exception as e:
            print(f"\n❌ Failed to send email: {e}")
    else:
        print("\n🚫 Email not sent.")


if __name__ == "__main__":
    main()
    