import time
from selenium import webdriver
import selenium
import subprocess
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH = 'C:\\Users\\Juhandre\\Downloads\\geckodriver\\geckodriver.exe'
EMAIL = ""
PASSWORD = ""
CONTACT_NAME = ''
CALL_DURATION = 60
PCAP_DIR = 'pcaps'
TCPDUMP_COMMAND = ['sudo', 'tcpdump', '-i', 'enp0s3', '-q', '-w', '', '-n', '-C', '30', '-W', '10', '-U', '-s', '0']
TCPDUMP_COMMAND_NAME_INDEX = 6

def make_call(driver, call_duration):
    driver.get("http://web.skype.com/en")
    driver.maximize_window()
    
    driver.find_element_by_name("loginfmt").clear()
    driver.find_element_by_name("loginfmt").send_keys(EMAIL)
    driver.find_element_by_name("passwd").clear()
    driver.find_element_by_name("passwd").send_keys(PASSWORD)
    driver.find_element_by_css_selector(".btn").submit()
    driver.find_element_by_name("passwd").send_keys(PASSWORD)
    driver.find_element_by_css_selector(".btn").submit()

    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Contacts']")))
    element.is_displayed()
    element.click()

    xpath = "//div[contains(@aria-label, \'{}\')]".format(CONTACT_NAME)
    element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, xpath)))
    ActionChains(driver).move_to_element(element).click().perform()
    # element.click()
    
    audio_call = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Audio Call']")))
    audio_call.click()

    # video_call = WebDriverWait(driver, 25).until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Video call']")))
    # video_call.click()
    
    time.sleep(call_duration)
    ActionChains(driver).move_by_offset(200,200).perform()
    end_call_btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@title='End Call']")))
    end_call_btn.click()
    
    time.sleep(2)
    
    #video_call.send_keys(Keys.ENTER)

def set_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument('--use-fake-device-for-media-stream')
    # chrome_options.add_argument('--use-fake-ui-for-media-stream')

    chrome_options.add_experimental_option("prefs", { \

        "profile.default_content_setting_values.media_stream_mic": 1,

        "profile.default_content_setting_values.media_stream_camera": 1,

        "profile.default_content_setting_values.geolocation": 1,

        "profile.default_content_setting_values.notifications": 1
    })

    return chrome_options

if not os.path.isdir(PCAP_DIR):
    os.mkdir(PCAP_DIR)

chrome_options = set_chrome_options()

for i in range(0,4):
    pcap_name = 'skype-voip-{}.pcap'.format(i)
    pcap_path = os.path.join(PCAP_DIR, pcap_name)
    TCPDUMP_COMMAND[TCPDUMP_COMMAND_NAME_INDEX] = pcap_path
    
    driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
    process = None
    try:
        # process = subprocess.Popen(TCPDUMP_COMMAND, stdout=subprocess.PIPE)
        make_call(driver, CALL_DURATION)
    except:
        e = sys.exc_info()[0]
        print(e)
    finally:
        driver.close()
        if process:
            os.system("sudo killall tcpdump")

