import os
import subprocess
import time
import random

BOT_NAME = '' # Should start with an @ and the name will end with Bot, for example @TestBot
INTERFACE = ''

def send_message(receiver, message):
	p = subprocess.Popen(['telegram-cli', '-W', '-k', 'server.pub',  '-e','msg '+ receiver +' '+message],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	s = p.communicate()
	# time.sleep(3)
	if s[1]: return "not sent \n "
	return "sent \n"

q = subprocess.Popen(['sudo','tcpdump', '-i', INTERFACE, '-vvv' , '-s 450','-w','telegrambot'+'.pcap'],stdout=subprocess.PIPE)
for i in range(0,1000):
	nouns=["Naveen","BIS","solana","Networks","Moodie drive","cybersecurity","Network Topology","nabil","nis","serge","colin","yonglin"]
	verbs=["Runs","HITS","Jumps","barks","drink","sleep","sit","stand","read","write","talk","break"]
	adj=["Threat","meeting","dropbox","telegram","gmail","yahoo","ftb","guru","om","browsing","tor","traffic"]
	num=random.randrange(0,12)
	message=nouns[num]+"  "+nouns[num]+verbs[num]+verbs[num]+"  "+adj[num]+adj[num]
	print(message)
	#message = "your message"
	print(send_message(BOT_NAME, message))

os.system("sudo killall tcpdump")
	


