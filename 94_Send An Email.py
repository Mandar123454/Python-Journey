import os
import smtplib
from email.message import EmailMessage

"""
Safe email sending example.

Usage steps:
1. Create an app password (Gmail: Account -> Security -> App passwords) or use a test SMTP server.
2. Set environment variables before running (PowerShell):
    $env:EMAIL_SENDER="your_email@gmail.com"
    $env:EMAIL_PASSWORD="your_app_password"
    $env:EMAIL_RECEIVER="receiver_email@gmail.com"
3. Run: python 94_Send An Email.py   (after activating the virtual environment)
    (Or: ./.venv/Scripts/python.exe 94_Send An Email.py)

If required variables are missing, a dry-run preview is shown instead (no email sent).
"""

sender = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")

subject = "Python email test"
body = "I wrote an email! :D"

missing = [name for name, val in {"EMAIL_SENDER": sender, "EMAIL_PASSWORD": password, "EMAIL_RECEIVER": receiver}.items() if not val]
if missing:
    print("=" * 50)
    print(" Email Script Dry Run ")
    print("=" * 50)
    print("Status : MISSING REQUIRED ENVIRONMENT VARIABLES")
    print(f"Missing: {', '.join(missing)}")
    print()
    print("Set them (PowerShell examples):")
    print('  $env:EMAIL_SENDER="your_email@gmail.com"')
    print('  $env:EMAIL_PASSWORD="your_app_password"')
    print('  $env:EMAIL_RECEIVER="receiver_email@gmail.com"')
    print()
    print("Would send:")
    print(f"  From   : {sender or '<unset>'}")
    print(f"  To     : {receiver or '<unset>'}")
    print(f"  Subject: {subject}")
    print("  Body   :")
    for line in body.splitlines():
        print(f"    {line}")
    print()
    print("(No email sent. Populate variables and re-run to send.)")
    print("=" * 50)
else:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
            server.starttls()
            server.login(sender, password)
            print("Logged in...")
            server.send_message(msg)
            print("Email has been sent!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check credentials/app password.")
    except Exception as e:
        print(f"Send failed: {e}")
