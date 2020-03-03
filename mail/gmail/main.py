from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import auth
import pandas as pd
import subprocess
p = subprocess.Popen(['sudo','tcpdump', '-i', 'enp0s3', '-vvv' ,'-w', 'text_mail.pcap'],stdout=subprocess.PIPE)
def get_labels():
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = 'https://mail.google.com/'
authInst = auth.auth(SCOPES)
credentials = authInst.get_credentials()
service = build('gmail', 'v1', http=credentials.authorize(Http()))

import send_email
sendInst = send_email.send_email(service)


df=pd.read_csv("spam_mail.csv")
mail_ids=df["email_id"].tolist()

for mail in mail_ids:


	##message = sendInst.create_message_with_attachment('nmuthyala005@gmail.com', mail, 'test gmail api', 'hi Naveen!, test email', 'Capture.PNG')
	message = sendInst.create_message('nmuthyala005@gmail.com', mail, 'test gmail api', 'hi Naveen!')
	sendInst.send_message('me', message)
os.system("sudo killall tcpdump")
