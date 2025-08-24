📧 Voice Assistant for Gmail
A Python-based voice assistant that integrates with the Gmail API to manage emails, with features like fetching messages, sending automated responses, and voicemail notifications.

✨ Features

Secure Authentication: Uses Google OAuth2 for safe and secure Gmail access.
Inbox Management: Retrieve and filter emails from your Gmail inbox.
Automated Emails: Send automated responses or voicemail-related notifications.
Developer-Friendly Testing: Supports restricted access for development and testing.


🛠️ Setup Instructions
Prerequisites

Python 3.8 or higher
A Google account
A Google Cloud project with Gmail API enabled

Step-by-Step Setup

Clone the Repository
git clone https://github.com/yourusername/voicemail.git
cd voicemail


Set Up a Google Cloud Project

Navigate to the Google Cloud Console.
Create a new project or select an existing one.
Enable the Gmail API:
Go to APIs & Services > Library.
Search for "Gmail API" and click Enable.




Configure OAuth Consent Screen

In the Google Cloud Console, go to APIs & Services > OAuth consent screen.
Select External for testing purposes.
Add your email address as a Test User under the "Test users" section.
Save your changes.


Create OAuth Credentials

Navigate to APIs & Services > Credentials.
Click Create Credentials > OAuth Client ID.
Select Desktop app (or Web application if hosting online).
Download the JSON file, rename it to credentials.json, and place it in the project root directory.


Install Dependencies

Ensure Python 3.8+ is installed.
Install required packages:pip install -r requirements.txt




Run the Application

Execute the main script:python main.py


On first run:
A browser window will prompt you to log in to your Google account.
Grant the necessary permissions.
A token.json file will be created for subsequent logins.






⚠️ Important Notes

Testing Mode: The app operates in testing mode, limiting access to developer-approved test users until Google verification is complete.
Common Issue: If you encounter "Access blocked: This app hasn't completed the Google verification process":
Verify your email is listed as a Test User in the OAuth consent screen.
Allow a few minutes for changes to propagate after adding test users.




📜 License
This project is licensed under the MIT License – feel free to use, modify, and distribute.

💡 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
