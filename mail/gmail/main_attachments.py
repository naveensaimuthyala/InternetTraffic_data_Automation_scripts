from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import auth
import subprocess
import pandas as pd
p = subprocess.Popen(['sudo','tcpdump', '-i', 'enp0s3', '-vvv' ,'-w', 'mail_attchments.pcap'],stdout=subprocess.PIPE)
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

receivers_list=df["email_id"].tolist()

message = sendInst.create_message_with_attachment('alex6139819267@gmail.com', 'muthyalanaveensai@gmail.com', 'test gmail api', 'hi there!, test email','netflix.pcap')
sendInst.send_message('me', message)




'''

for receiver in receivers_list:
	
	message = sendInst.create_message_with_attachment('alex6139819267@gmail.com', receiver, 'test gmail api', 'hi there!, test email','attach.pcap')
	#message = sendInst.create_message('nmuthyala005@gmail.com', 'nmuthyala005@gmail.com', 'test gmail api', 'hi there!')
	sendInst.send_message('me', message)

'''


os.system("sudo killall tcpdump")
