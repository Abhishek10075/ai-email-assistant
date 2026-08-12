✉️ SmartMail AI

SmartMail AI is an AI-powered email assistant built with Streamlit. It helps users generate professional email content using Mistral AI and send the generated email through Gmail SMTP.

🚀 Features

Generate professional email content using Mistral AI.

Enter recipient email address.

Enter email subject.

Describe the purpose of the email using a short description.

Add contact details that are automatically included in the email signature.

Edit the generated email before sending.

Attach multiple files.

Attach multiple images.

Preview selected images before sending.

Send emails through Gmail SMTP.

Store API and email credentials in a .env file.

🛠️ Technologies Used

Python

Streamlit

Mistral AI

LangChain

Gmail SMTP

python-dotenv

📁 Project Structure

SmartMail AI/
│
├── app.py
│
├── services/
│   ├── email_generator.py
│   └── email_sender.py
│
├── .env
└── README.md

File Description

File

Purpose

app.py

Streamlit user interface, email form, file/image upload, preview, generation and sending flow

services/email_generator.py

Generates the professional email body using Mistral AI

services/email_sender.py

Sends emails through Gmail SMTP and handles attachments

.env

Stores Mistral API key and Gmail email credentials

README.md

Project documentation

🔄 Application Flow

User
  │
  ├── Recipient Email
  ├── Subject
  ├── Short Description
  ├── Contact Details
  ├── Files
  └── Images
          │
          ▼
     Streamlit UI
          │
          ▼
   Mistral AI + LangChain
          │
          ▼
    Generated Email
          │
          ▼
     Email Preview
          │
          ▼
       Send Email
          │
          ▼
      Gmail SMTP
          │
          ▼
      Recipient

🔑 Environment Variables

Create a .env file in the project root.

MISTRAL_API_KEY=your_mistral_api_key
EMAIL_ADDRESS=your_gmail_address
EMAIL_APP_PASSWORD=your_gmail_app_password

The application loads these values using python-dotenv.

Important: Never commit your .env file or expose your API key and Gmail App Password publicly.

📦 Installation

Create and activate your Python environment, then install the required packages:

pip install streamlit python-dotenv langchain-mistralai langchain-core

▶️ Run the Application

From the project root, run:

streamlit run app.py

The application will open in your browser.

📝 How to Use

Enter the recipient's email address.

Enter the email subject.

Enter a short description of what the email should contain.

Enter contact details if required.

Upload files or images if needed.

Click Generate Email.

Review and edit the generated email.

Click Send Email.

The email is sent through Gmail SMTP.

📎 Attachments

The application supports multiple file and image uploads.

Supported Files

PDF

DOC

DOCX

TXT

CSV

XLSX

PPT

PPTX

Supported Images

PNG

JPG

JPEG

WEBP

Uploaded files and images are combined and passed to the email sending service as attachments.

🤖 AI Email Generation

The email generation service uses the Mistral model:

mistral-small-latest

The generated email is based on:

Subject

Short Description / Purpose

Contact Details

The generated output contains only the email body and does not generate a separate subject line.

📧 Email Sending

The application uses Gmail SMTP:

SMTP Server: smtp.gmail.com
SMTP Port: 587

The email is sent as a multipart email so that the message body and uploaded attachments can be included together.

🔐 Security

Keep the following values private:

MISTRAL_API_KEY

EMAIL_ADDRESS

EMAIL_APP_PASSWORD

Add .env to .gitignore before pushing the project to GitHub.

Example:

.env
__pycache__/
*.pyc

🎯 Project Purpose

SmartMail AI is designed to make professional email writing and sending faster by combining AI-powered email generation with a simple Streamlit interface and Gmail SMTP.

👨‍💻 Author

Abhishek Nishad
