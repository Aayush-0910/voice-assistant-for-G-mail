from __future__ import print_function
import datetime
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import date

# If modifying these scopes, delete the file token.pickle
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Check if running in CI mode
CI_MODE = "--ci" in sys.argv

if not CI_MODE:
    import pyttsx3
    import speech_recognition as sr


def speak(text):
    if CI_MODE:
        print("[Speak disabled in CI] ->", text)
    else:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 20)
        engine.say(text)
        engine.runAndWait()


def get_audio():
    if CI_MODE:
        print("[Audio input disabled in CI]")
        return ""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            said = r.recognize_google(audio)
            print(said)
            return said.lower()
    except Exception as e:
        speak("Didn't get that")
        return ""


def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def check_mails(service):
    today = date.today()
    today_main = today.strftime('%Y/%m/%d')

    results = service.users().messages().list(
        userId='me',
        labelIds=["INBOX", "UNREAD"],
        q=f"after:{today_main} and category:Primary"
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
        speak('No messages found.')
    else:
        speak(f"{len(messages)} new emails found")
        for message in messages:
            msg = service.users().messages().get(
                userId='me',
                id=message['id'],
                format='metadata'
            ).execute()

            for add in msg['payload']['headers']:
                if add['name'] == "From":
                    sender = str(add['value'].split("<")[0])
                    print("Email from:", sender)
                    speak("email from " + sender)

                    if CI_MODE:
                        print("Snippet:", msg['snippet'])
                    else:
                        text = input("Type 'read' to hear it, anything else to skip: ")
                        if text.strip().lower() == "read":
                            print(msg['snippet'])
                            speak(msg['snippet'])
                        else:
                            speak("email skipped")


if __name__ == "__main__":
    speak("Welcome to Gmail Assistant")
    service = authenticate_gmail()
    check_mails(service)
