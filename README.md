📧 Voice Assistant for Gmail



A Python-based voice assistant that integrates with the Gmail API to streamline email management, with features like fetching emails, sending automated responses, and voicemail notifications.

Table of Contents

Features
Prerequisites
Setup Instructions
Usage
Troubleshooting
Contributing
License

Features

Secure Authentication: Integrates Google OAuth2 for safe Gmail access.
Inbox Management: Fetch and filter emails from your Gmail inbox.
Automated Emails: Send automated responses or voicemail notifications.
Developer Testing: Restricted access mode for development and testing.

Prerequisites

Python 3.8 or higher
A Google account
Access to Google Cloud Console for API setup
pip for installing dependencies

Setup Instructions

Clone the Repository
git clone https://github.com/yourusername/voicemail.git
cd voicemail


Set Up Google Cloud Project

Visit the Google Cloud Console.
Create a new project or select an existing one.
Enable the Gmail API:
Go to APIs & Services > Library.
Search for "Gmail API" and click Enable.




Configure OAuth Consent Screen

Navigate to APIs & Services > OAuth consent screen.
Select External for testing.
Add your email as a Test User in the "Test users" section.
Save changes.


Create OAuth Credentials

Go to APIs & Services > Credentials.
Click Create Credentials > OAuth Client ID.
Select Desktop app (or Web application if hosting).
Download the JSON file, rename it to credentials.json, and place it in the project root.


Install Dependencies
pip install -r requirements.txt


Run the Application
python main.py


On first run, a browser window will prompt Google login.
Grant permissions to generate a token.json for future logins.



Usage

Fetch Emails: Use the app to retrieve and filter inbox messages.
Send Automated Emails: Configure automated responses for voicemail notifications.
Testing Mode: Only approved test users can log in until Google verification is complete.

Troubleshooting

Error: "Access blocked: This app hasn't completed the Google verification process"
Ensure your email is added as a Test User in the OAuth consent screen.
Wait a few minutes for changes to propagate.


Dependency Issues: Verify Python 3.8+ and run pip install -r requirements.txt again.
Token Issues: Delete token.json and rerun python main.py to re-authenticate.

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/awesome-feature).
Commit changes (git commit -m 'Add awesome feature').
Push to the branch (git push origin feature/awesome-feature).
Open a pull request.

License
This project is licensed under the MIT License.
