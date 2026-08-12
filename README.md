<img width="949" height="431" alt="image" src="https://github.com/user-attachments/assets/6b1a06b8-b665-44ea-87fe-26a7b54d1865" />
# ✉️ SmartMail AI

SmartMail AI is an AI-powered email assistant built with **Streamlit**. It uses **Mistral AI** to generate professional email content and **Gmail SMTP** to send emails with optional file and image attachments.

## 🚀 Features

- Generate professional emails using Mistral AI
- Enter recipient email address
- Enter email subject
- Describe the purpose of the email
- Add contact details to the email signature
- Preview and edit the generated email
- Send emails directly through Gmail SMTP
- Upload multiple files as attachments
- Upload multiple images as attachments
- Preview selected images before sending
- Securely load API keys and email credentials using `.env`
- Clean and responsive Streamlit UI

## 🛠️ Technologies Used

- Python
- Streamlit
- Mistral AI
- LangChain
- Gmail SMTP
- Python-dotenv

## 📁 Project Structure

```text
SmartMail-AI/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── services/
    ├── email_generator.py
    └── email_sender.py
🔄 Application Flow
User enters recipient email
        ↓
User enters subject
        ↓
User describes email purpose
        ↓
User adds contact details
        ↓
User uploads files/images (optional)
        ↓
Mistral AI generates professional email
        ↓
User previews and edits email
        ↓
Email + attachments are sent using Gmail SMTP
📋 Requirements

Make sure Python is installed on your system.

Recommended Python version:

Python 3.10+
📦 Installation
1. Clone the repository
git clone https://github.com/your-username/SmartMail-AI.git
2. Open the project folder
cd SmartMail-AI
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
5. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the root directory of the project.

Add the following variables:

MISTRAL_API_KEY=your_mistral_api_key
EMAIL_ADDRESS=your_gmail_address
EMAIL_APP_PASSWORD=your_gmail_app_password
Important

Do not upload your .env file to GitHub.

Add .env to your .gitignore file:

.env
venv/
__pycache__/
*.pyc
🔑 Gmail App Password

To send emails through Gmail SMTP, you need a Gmail App Password.

The application uses:

SMTP Server: smtp.gmail.com
SMTP Port: 587

The email service uses TLS and Gmail authentication before sending the email.

🤖 Mistral AI

SmartMail AI uses the Mistral model:

mistral-small-latest

The Mistral API key is loaded securely from the .env file.

The AI generates the email body using:

Email subject
Short description
Contact details

The generated email includes a professional greeting, properly structured body, closing phrase, and contact details when provided.

📎 Supported Attachments
Files

The application supports:

PDF
DOC
DOCX
TXT
CSV
XLSX
PPT
PPTX
Images

The application supports:

PNG
JPG
JPEG
WEBP

Multiple files and images can be selected and attached to the email.

▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

🖥️ How to Use
Step 1

Enter the recipient's email address.

Step 2

Enter the email subject.

Step 3

Describe what you want to write in the email.

Step 4

Add contact details if required.

Example:

Abhishek Nishad
+91 XXXXX XXXXX
your@email.com
Step 5

Upload files or images if required.

Step 6

Click:

✨ Generate Email
Step 7

Review and edit the generated email.

Step 8

Click:

🚀 Send Email

The email will be sent to the specified recipient.

🧩 Main Components
app.py

The main Streamlit application.

It handles:

User interface
Email input
Subject input
Description input
Contact details
File uploads
Image uploads
Email preview
Email sending
services/email_generator.py

Responsible for AI-based email generation using Mistral AI and LangChain.

Main function:

generate_email(
    subject,
    short_description,
    contact_details
)
services/email_sender.py

Responsible for sending emails using Gmail SMTP.

Main function:

send_email(
    sender_email,
    sender_app_password,
    recipient_email,
    subject,
    body,
    attachments
)
🔒 Security

Sensitive credentials should always be stored in .env.

Never commit the following information to GitHub:

MISTRAL_API_KEY
EMAIL_ADDRESS
EMAIL_APP_PASSWORD

Make sure .env is included in .gitignore.

📄 License

This project is created for learning and development purposes.

👨‍💻 Author

Abhishek Nishad

AI/ML | Python | Generative AI | NLP
