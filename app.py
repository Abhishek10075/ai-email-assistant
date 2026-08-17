import os
import streamlit as st
from dotenv import load_dotenv
import re

from services.email_generator import generate_email
from services.email_sender import send_email

load_dotenv()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

def is_valid_email(email: str) -> bool:
    """Basic email format validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


st.set_page_config(
    page_title="SmartMail AI",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
        }

        .header {
            text-align: center;
            padding: 10px 0 25px 0;
        }

        .header h1 {
            font-size: 42px;
            margin-bottom: 5px;
        }

        .header p {
            font-size: 17px;
            color: #666;
        }

        .section-title {
            font-size: 22px;
            font-weight: 600;
            margin-top: 15px;
            margin-bottom: 10px;
        }

        .preview-box {
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 12px;
            background-color: #fafafa;
        }

        .stButton > button {
            width: 100%;
            border-radius: 8px;
            height: 45px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    """
    <div class="header">
        <h1>✉️ SmartMail AI</h1>
        <p>Create professional emails quickly with AI</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Check Email Credentials
# --------------------------------------------------

sender_email = os.getenv("EMAIL_ADDRESS")
sender_app_password = os.getenv("EMAIL_APP_PASSWORD")

if not sender_email or not sender_app_password:
    st.error(
        "EMAIL_ADDRESS or EMAIL_APP_PASSWORD is missing in your .env file."
    )
    st.stop()

# --------------------------------------------------
# Main Layout
# --------------------------------------------------

left, right = st.columns([1, 1], gap="large")

# ==================================================
# LEFT SIDE - EMAIL FORM
# ==================================================

with left:

    st.markdown(
        '<div class="section-title">📨 Email Details</div>',
        unsafe_allow_html=True
    )

    recipient = st.text_input(
        "Recipient Email",
        placeholder="example@gmail.com"
    )

    if recipient:
        if is_valid_email(recipient):
            st.success("Valid email address ✅")
        else:
            st.error("Please enter a valid email address ❌")

    

    subject = st.text_input(
        "Subject",
        placeholder="Enter email subject"
    )

    short_description = st.text_area(
        "Short Description",
        placeholder="Describe what you want to write in the email...",
        height=130
    )

    contact_details = st.text_area(
        "Contact Details",
        placeholder="Name\nPhone\nEmail\nCompany",
        height=120
    )

    st.markdown(
        '<div class="section-title">📎 Attachments</div>',
        unsafe_allow_html=True
    )

    uploaded_files = st.file_uploader(
        "Upload files",
        accept_multiple_files=True,
        type=[
            "pdf",
            "doc",
            "docx",
            "txt",
            "csv",
            "xlsx",
            "ppt",
            "pptx"
        ]
    )

    uploaded_images = st.file_uploader(
        "Upload images",
        accept_multiple_files=True,
        type=[
            "png",
            "jpg",
            "jpeg",
            "webp"
        ]
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) selected.")

    if uploaded_images:
        st.success(f"{len(uploaded_images)} image(s) selected.")

    if uploaded_images:
        with st.expander("View selected images"):
            image_columns = st.columns(3)

            for index, image in enumerate(uploaded_images):
                with image_columns[index % 3]:
                    st.image(
                        image,
                        caption=image.name,
                        use_container_width=True
                    )

# ==================================================
# RIGHT SIDE - GENERATION & PREVIEW
# ==================================================

with right:

    st.markdown(
        '<div class="section-title">🤖 AI Email Generator</div>',
        unsafe_allow_html=True
    )

    generate_button = st.button(
        "✨ Generate Email",
        type="primary"
    )

    if generate_button:

        if not recipient:
            st.warning("Please enter recipient email.")

        elif not subject:
            st.warning("Please enter email subject.")

        elif not short_description:
            st.warning("Please enter a short description.")

        else:

            with st.spinner("Generating professional email..."):

                try:
                    body = generate_email(
                        subject=subject,
                        short_description=short_description,
                        contact_details=contact_details
                    )

                    st.session_state["email_body"] = body

                except Exception as e:
                    st.error(f"Failed to generate email: {e}")

    # --------------------------------------------------
    # Email Preview
    # --------------------------------------------------

    if "email_body" in st.session_state:

        st.markdown(
            '<div class="section-title">👀 Email Preview</div>',
            unsafe_allow_html=True
        )

        st.text_input(
            "To",
            value=recipient,
            disabled=True
        )

        st.text_input(
            "Subject",
            value=subject,
            disabled=True
        )

        edited_body = st.text_area(
            "Email Body",
            value=st.session_state["email_body"],
            height=350
        )

        st.session_state["email_body"] = edited_body

        # --------------------------------------------------
        # Send Email
        # --------------------------------------------------

        send_button = st.button(
            "🚀 Send Email",
            type="primary"
        )

        if send_button:

            if not recipient:
                st.warning("Please enter recipient email.")

            else:

                try:

                    all_attachments = (
                        (uploaded_files or []) + (uploaded_images or [])
                    )

                    send_email(
                        sender_email,
                        sender_app_password,
                        recipient,
                        subject,
                        st.session_state["email_body"],
                        attachments=all_attachments
                    )

                    st.success(
                        f"Email sent successfully to {recipient}"
                    )

                except Exception as e:

                    st.error(
                        f"Failed to send email: {e}"
                    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "SmartMail AI • AI-powered professional email generation"
)