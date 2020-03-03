from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import subprocess
import os

DRIVER_PATH = ''
INTERFACE = ''
USERNAME = ''
PASSWORD = ''
RECEIVER_EMAIL = ''

browser = webdriver.Chrome(DRIVER_PATH)
browser.maximize_window()

p = subprocess.Popen(['sudo','tcpdump', '-i', INTERFACE, '-vvv' ,'-w', 'yahoo_mail.pcap'],stdout=subprocess.PIPE)
browser.get('https://login.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(USERNAME)
emailElem.submit()


passwordElem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "login-passwd"))
)
passwordElem.send_keys(PASSWORD)
passwordElem.send_keys(Keys.ENTER)

mailElem = browser.find_element_by_id('uh-mail-link')
print(mailElem.get_attribute('id'))
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='uh-mail-link']")))
ActionChains(browser).move_to_element(mailElem).click().perform()

WebDriverWait(browser, 100).until(EC.title_contains('Yahoo Mail'))

composeElem = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/nav/div/div[1]/a')
composeElem.click()

toelem=browser.find_element_by_id('message-to-field')
toelem.send_keys(RECEIVER_EMAIL)


subelem=browser.find_element_by_xpath("//div[@class='p_R']//input[contains(@data-test-id,'compose-subject')]")
subelem.send_keys("Test_mail")


bdyelem=browser.find_element_by_xpath("//div[@id='editor-container']//div[contains(@role,'textbox')]")


bdyelem.send_keys("Test_mail")

# UNCOMMENT FOR SENDING ATTACHMENTS
# atchelem = browser.find_element_by_xpath("//input[@title='Attach files']")
# atchelem.click()
# atchelem.send_keys('')

sendElem = browser.find_element_by_class_name('q_Z2aVTcY')
sendElem.click()
time.sleep(3)
browser.close()
os.system("sudo killall tcpdump")




