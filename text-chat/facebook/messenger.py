
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import random
import subprocess

#p = subprocess.Popen(['sudo','tcpdump', '-i', 'enp0s3', '-vvv' , '-s 800',
 #                '-w', '_db.pcap'], stdout=subprocess.PIPE)
DRIVER_PATH = ''
INTERFACE = ''
USERNAME = ''
PASSWORD = ''
CHAT_PATH = ''

_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
#webdriver.Firefox(firefox_profile=_browser_profile)

# driver = webdriver.Firefox(firefox_profile=_browser_profile)
driver = webdriver.Chrome(DRIVER_PATH)

p = subprocess.Popen(['sudo','tcpdump', '-i', INTERFACE, '-vvv' , '-s 400','-w','facebook'+'.pcap'],stdout=subprocess.PIPE)
driver.get(CHAT_PATH)  ##Tells the driver to go to facebook.com
driver.find_element_by_css_selector("#email").send_keys(USERNAME)
driver.find_element_by_css_selector("#pass").send_keys(PASSWORD)


login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

#driver.get("https://www.facebook.com/messages/t/2037591349694082")  ##facebook link of your friend



msg = driver.find_element_by_xpath('//div[@role="combobox"]')
x=['a','b','c','d','d','e','f','g','h','i','j','k','l','m','n']
for i in range(1000):
	nouns=["Naveen","BIS","solana","Networks","Moodie drive","cybersecurity","Network Topology","nabil","nis","serge","colin","yonglin"]
	verbs=["Runs","HITS","Jumps","barks","drink","sleep","sit","stand","read","write","talk","break"]
	adj=["Threat","meeting","dropbox","telegram","gmail","yahoo","ftb","guru","om","browsing","tor","traffic"]
	num=random.randrange(0,12)
	messagei=nouns[num]+"  "+nouns[num]+verbs[num]+verbs[num]+"  "+adj[num]+adj[num]
	
	msg.send_keys(messagei) #message to be sent
	msg.send_keys(Keys.ENTER)
	time.sleep(3)

for i in x:
	
	msg.send_keys(i) #message to be sent
	msg.send_keys(Keys.ENTER)
	time.sleep(3)

driver.close()

os.system("sudo killall tcpdump")


