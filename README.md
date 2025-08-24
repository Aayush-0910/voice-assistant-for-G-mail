Voice Assistant for Gmail
This project integrates with the Gmail API to fetch and send emails, with a focus on voicemail-related features like automated email handling and notifications.
🚀 Features

Secure Authentication: Google OAuth2 integration for safe access to Gmail.
Inbox Management: Fetch messages from your Gmail inbox with filtering options.
Automated Emails: Send automated responses or voicemail notifications.
Developer Testing: Restricted access mode for development and testing.

🛠️ Setup Instructions

Clone the Repository
git clone https://github.com/yourusername/voicemail.git
cd voicemail


Create a Google Cloud Project

Go to the Google Cloud Console.
Create a new project or select an existing one.
Enable the Gmail API:
Visit Enable Gmail API.
Select your project and click Enable.




Configure OAuth Consent Screen

In Google Cloud Console, navigate to APIs & Services > OAuth consent screen.
Select External (for testing with your account).
Add your email as a Test User.
Save changes.


Create OAuth Credentials

Go to APIs & Services > Credentials.
Click Create Credentials > OAuth Client ID.
Choose Desktop app (or Web application if hosting).
Download the JSON file and rename it to credentials.json.
Place this file in the project root directory.


Install Dependencies

Ensure you have Python 3.8+ installed.
Run:pip install -r requirements.txt




Run the App

Run:python main.py


On the first run:
A browser window will open for Google login.
Grant the required permissions.
A token.json file will be generated for future logins.





📌 Important Notes

Testing Mode: The app is in testing mode, so only developer-approved users can log in until Google verification is completed.
Common Error: If you see "Access blocked: This app hasn't completed the Google verification process":
Ensure your email is added as a Test User in the OAuth consent screen.
Wait a few minutes after adding test users for changes to propagate.



📜 License
MIT License – feel free to use, modify, and distribute.
