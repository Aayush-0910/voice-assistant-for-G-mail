📩 Voicemail – Gmail API Integration

This project connects to Gmail API to fetch/send emails and handle voicemail-related features.

🚀 Features

Secure Google OAuth2 authentication

Fetch messages from Gmail inbox

Send automated emails/voicemails

Developer mode testing with restricted access

🛠️ Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/voicemail.git
cd voicemail

2. Create a Google Cloud Project

Go to Google Cloud Console
.

Create a new project or select an existing one.

Enable the Gmail API for the project:

Visit Enable Gmail API
.

Select your project and click Enable.

3. Configure OAuth Consent Screen

In Google Cloud Console, go to APIs & Services > OAuth consent screen.

Select External (for testing with your account).

Add your email as a Test User.

Save changes.

4. Create OAuth Credentials

Navigate to APIs & Services > Credentials.

Click Create Credentials > OAuth Client ID.

Choose Desktop app (or Web if you’re hosting it).

Download the JSON file and rename it to:

credentials.json


Place this file in the project root directory.

5. Install Dependencies

Make sure you have Python 3.8+ installed.

pip install -r requirements.txt

6. Run the App
python main.py


On the first run:

A browser window will open asking you to log in with your Google account.

Grant permissions.

A token.json file will be generated automatically for future logins.

📌 Notes

This app is in testing mode, so only developer-approved users can log in until verification is completed.

If you get an error like:

Access blocked: This app hasn’t completed the Google verification process


→ Make sure your email is added as a Test User in the OAuth consent screen.

📜 License

MIT License – feel free to use and modify.
