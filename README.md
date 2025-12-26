# word_every_day

Send a curated word (with definition/example) to your email every day.

## Table of contents
- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## About
word_every_day is a small utility that delivers a word-of-the-day email to one or more recipients. It’s intended to help users learn new vocabulary by receiving a short, readable email once per day.

## Features
- Sends a daily email with a word, definition, and example sentence.
- Configurable SMTP settings and recipient address.
- Can be scheduled with system cron or run inside a container.

## Requirements
- Python 3.8+ (or the runtime used by the project)
- Access to an SMTP server (Gmail, SendGrid, Mailgun, etc.)
- Internet connection for sending emails

## Configuration
Set the following environment variables (example names — adapt to your codebase):

- SMTP_HOST — SMTP server host (e.g., `smtp.gmail.com`)
- SMTP_PORT — SMTP port (e.g., `587` for TLS)
- SMTP_USER — SMTP username / sender email
- SMTP_PASS — SMTP password or app-specific password
- SENDER_EMAIL — From address shown in the email
- RECIPIENT_EMAIL — Comma-separated recipient addresses
- WORD_SOURCE — (optional) path or API to fetch words
- CRON_SCHEDULE — (optional) cron expression if your runner reads it)

Store these in a `.env` file or configure them in your deployment environment.

## Installation
1. Clone the repository:
   git clone https://github.com/freakyLuffy/word_every_day.git
2. Install dependencies:
   - If Python: pip install -r requirements.txt
   - If Node or other, follow the language-specific steps in the repo

## Usage
- Test sending a single email:
  - Run the main script directly (example):
    python send_word.py
- Schedule daily runs:
  - Using cron (example to run at 08:00 daily):
    0 8 * * * /path/to/venv/bin/python /path/to/word_every_day/send_word.py
  - Or use a cloud scheduler / GitHub Actions / systemd timer

## Docker (optional)
Add a Dockerfile or use an existing one. Example run:
- Build: docker build -t word_every_day .
- Run: docker run -e SMTP_HOST=... -e SMTP_USER=... -e SMTP_PASS=... word_every_day

## Testing
- Provide a test mode or staging SMTP to avoid spamming real users.
- Run unit tests if included:
  pytest

## Contributing
Contributions, issues and feature requests are welcome. Please open an issue first to discuss major changes.

## License
Add your license here (e.g., MIT). If you don't want a license, note that the project is proprietary.
