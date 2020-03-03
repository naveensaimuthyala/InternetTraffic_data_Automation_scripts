import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
import subprocess

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
EMAIL = "mnir@solananetworks.com"
PASSWORD = "solana5g"
INTERFACE = 'enp0s3'
CALL_DURATION = 7
CALL_RECEIVER = 'https://www.messenger.com/t/msingh.paul'
NUMBER_OF_CALLS = 3

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--use-fake-device-for-media-stream')
chrome_options.add_argument('--use-fake-ui-for-media-stream')

# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", { \

    "profile.default_content_setting_values.media_stream_mic": 1,

    "profile.default_content_setting_values.media_stream_camera": 1,

    "profile.default_content_setting_values.geolocation": 1,

    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)  # Optional argument, if not specified will search path.
driver.maximize_window()

driver.get("http://www.messenger.com")
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(EMAIL)
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys(PASSWORD)
driver.find_element_by_id("loginbutton").click()

driver.implicitly_wait(10)
#friend = input("Enter your friend's fb id: ")
driver.get("http://www.messenger.com/t/"+CALL_RECEIVER)
print(driver.window_handles)
try:
	#ch = int(input("enter 1 for audio or 2 for video: "))
	ch= 1
except Exception as e:
	print("enter only number")
	exit()

def  make_call(i,s):
	mits=(s/60)
	p = subprocess.Popen(['sudo','tcpdump', '-i', INTERFACE, '-vvv' , '-s 650','-w','facebook_audio_'+str(round(mits, 2))+'min_'+str(i)+'.pcap']
		,stdout=subprocess.PIPE)
	if ch == 1:
		phone = driver.find_element_by_css_selector("[title*='Start a voice call']").find_element_by_xpath("..")
	elif ch == 2:
		phone = driver.find_element_by_css_selector("[title*='Start a video chat']").find_element_by_xpath("..")
	else:
		print("wrong choice")
		exit()
	phone.click()
	phone.send_keys(Keys.TAB)
	phone.send_keys(Keys.ENTER)
	hls=driver.window_handles
	print(hls[1])
	
	driver.switch_to.window(hls[1])
	driver.implicitly_wait(20)
	time.sleep(s)
	endbtn = driver.find_element_by_xpath('//button[contains(@class,"endCall")]')
	WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[contains(@class,"endCall")]')))
	endbtn.click()
	
	if driver.window_handles[1] is not driver.window_handles[0]:
		driver.close()
	os.system("sudo killall tcpdump")
	driver.switch_to_window(hls[0])

for i in range(NUMBER_OF_CALLS):
	make_call(i,CALL_DURATION)

driver.close()
	


