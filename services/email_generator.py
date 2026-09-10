"""AI email generation service for SmartMail AI."""

import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()


def get_client():
    """Create and return the Gemini API client."""
    return genai.Client(api_key=os.getenv("GEMINIAI_API_KEY"))


# --------------------------------------------------
# Prompt Template
# --------------------------------------------------

EMAIL_PROMPT_TEMPLATE = """
You are a professional email writing assistant.

Your task is to write a professional and natural email body
based on the information provided by the user.

Subject:
{subject}

Short Description / Purpose of Email:
{short_description}

Contact Details:
{contact_details}

Instructions:

1. Understand the purpose of the email from the short description.
2. Decide the appropriate length yourself based on the description -
   if the description is short, keep the email short but still
   complete and meaningful. If the description has more detail,
   write a longer, properly structured email.
3. The subject line is already fixed above - do NOT generate or
   repeat a subject line in your output.
4. Use a professional greeting.
5. Write the main body based on the short description.
6. End with an appropriate closing phrase (e.g. "Best regards," /
   "Sincerely,") followed by a new line.
7. MANDATORY: After the closing phrase, add every item listed under
   "Contact Details" above, each on its own line, exactly as a
   signature block. Do not skip this even if the description already
   mentions similar information. Do not paraphrase or reword the
   contact details - reproduce them exactly as given.
8. If Contact Details is empty, skip the signature block entirely -
   do not invent any contact information.
9. Do not explain how you generated the email.
10. Return only the email body text - no "Subject:" line, no extra labels.

Example of the expected ending format:

Best regards,
<contact detail line 1>
<contact detail line 2>
<contact detail line 3>
"""


# --------------------------------------------------
# Generate Email Function
# --------------------------------------------------

def generate_email(
    subject: str,
    short_description: str,
    contact_details: str
) -> str:
    """
    Generate a professional email body using Gemini AI.

    Args:
        subject: The email subject line, provided by the user.
        short_description: Purpose or topic of the email.
        contact_details: Additional user/contact information.

    Returns:
        Generated email body as a string.
    """

    client = get_client()

    prompt = EMAIL_PROMPT_TEMPLATE.format(
        subject=subject,
        short_description=short_description,
        contact_details=contact_details
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        raise RuntimeError(f"Gemini email generation failed: {e}")