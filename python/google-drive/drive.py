from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile(os.path.expanduser("~/.drive.credentials"))
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.CommandLineAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile(os.path.expanduser("~/.drive.credentials"))

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'
file1.SetContentFile('test.py') # Set content of the file from given string
file1.Upload()
