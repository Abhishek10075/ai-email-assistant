"""AI email generation service for SmartMail AI."""

import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load environment variables
load_dotenv()


def get_llm():
    """Create and return the Mistral AI model."""
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv("MISTRAL_API_KEY")
    )


# --------------------------------------------------
# Prompt Template
# --------------------------------------------------

email_prompt = ChatPromptTemplate.from_template(
    """
You are a professional email writing assistant.

Your task is to write a professional and natural email
based on the information provided by the user.

Sender Email:
{sender_email}

Short Description / Purpose of Email:
{short_description}

Email Length:
{email_length}

Contact Details:
{contact_details}

Instructions:

1. Understand the purpose of the email from the short description.
2. Use the contact details naturally wherever relevant.
3. Do not invent any personal information that is not provided.
4. Keep the email professional, clear and natural.
5. If the requested length is "Short", write a concise email.
6. If the requested length is "Long", write a detailed but professional email.
7. Include an appropriate subject line.
8. Use a professional greeting.
9. End with an appropriate closing.
10. Do not explain how you generated the email.
11. Return only the final email.

Format:

Subject: <subject>

<email body>
"""
)


# --------------------------------------------------
# Output Parser
# --------------------------------------------------

output_parser = StrOutputParser()


# --------------------------------------------------
# Create Chain
# --------------------------------------------------

email_chain = email_prompt | get_llm() | output_parser


# --------------------------------------------------
# Generate Email Function
# --------------------------------------------------

def generate_email(
    sender_email: str,
    short_description: str,
    email_length: str,
    contact_details: str
) -> str:
    """
    Generate a professional email using Mistral AI.

    Args:
        sender_email: Sender's email address.
        short_description: Purpose or topic of the email.
        email_length: Short or Long.
        contact_details: Additional user/contact information.

    Returns:
        Generated email as a string.
    """

    result = email_chain.invoke(
        {
            "sender_email": sender_email,
            "short_description": short_description,
            "email_length": email_length,
            "contact_details": contact_details
        }
    )

    return result

