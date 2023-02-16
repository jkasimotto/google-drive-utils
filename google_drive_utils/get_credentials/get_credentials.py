
import io
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def get_credentials(client_secret_file_path, token_file_path, scopes):
    # Load or create credentials for the Google Drive API
    creds = None
    if os.path.exists(token_file_path):
        creds = Credentials.from_authorized_user_file(token_file_path, scopes)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secret_file_path, scopes)
        creds = flow.run_local_server(port=0)
        with open(token_file_path, 'w') as token:
            token.write(creds.to_json())
    return creds