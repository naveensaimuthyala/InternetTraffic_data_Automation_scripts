import dropbox
import os
import subprocess
INTERFACE = 'enp0s3'
access_token = 'REPLACE WITH ACCESS TOKEN'
dbx = dropbox.Dropbox(access_token)
response = dbx.files_list_folder("/inputs")
print(list(response.entries))
print("Number of files is : ",len(list(response.entries)))
for file in response.entries:

    print(file.name)
    x=file.name
    p = subprocess.Popen(['sudo','tcpdump', '-i', INTERFACE, '-vvv' , '-s 450',
                    '-w', 'dropbox_download_capture/'+x+'_db_downlink.pcap'], stdout=subprocess.PIPE)

    with open('db'+x, "wb") as f:
        metadata, res = dbx.files_download(path="/inputs/"+x)
        f.write(res.content)

    print('downloaded :',x)
    cmd = "sudo killall  tcpdump"
    os.system(cmd)

