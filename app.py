import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date, datetime
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, recipients):
    email = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEMultipart()
    msg["From"] = email
    # No "To" header for BCC privacy
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipients, msg.as_string())

def main():
    df = pd.read_csv("words.csv")
    print(f"CSV loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"First row: {df.iloc[0].to_dict()}")

    start_date_str = os.environ.get("START_DATE", "2025-12-25")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    today = date.today()
    day_number = (today - start_date).days + 1
    day_number = max(1, day_number)  # Ensure non-negative
    len_df = len(df)
    day_number = ((day_number - 1) % len_df) + 1

    print(f"Today: {today}, Start date: {start_date}, Raw day number: {(today - start_date).days + 1}, Final day number: {day_number}")

    row = df[df["day"] == day_number]

    if row.empty:
        print("No word found for today")
        return

    word = row.iloc[0]

    subject = f"🗣️ Word of the Day – {word['word']}"

    body = f"""
Word: {word['word']}

Meaning:
{word['meaning']}

Example:
"{word['example']}"

Try using this word today 🙂
"""

    # Read recipients from emails.txt
    with open("emails.txt", "r") as f:
        recipients = [line.strip() for line in f if line.strip()]

    if not recipients:
        print("No recipients found in emails.txt")
        return

    send_email(subject, body, recipients)
    print("Email sent successfully")

if __name__ == "__main__":
    main()
