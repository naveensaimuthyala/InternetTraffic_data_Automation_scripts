# InternetTraffic_data_Automation_scripts


1. Install python depencies:
    - run 'pip install -r requirements.txt'

2. Enable the Google APIs for both Gmail and Google Drive.
    - An app has to be created to be able to access the Gmail and Google Drive APIs.
    
    Google Drive:
        - Go to the link: https://developers.google.com/drive/api/v3/quickstart/python
        - select the "Enable the Drive API"
        - If you are not signed into a Google Account, sign in or create an account
            - This is the account that will be use for sending emails
        - Follow the instructions to create the app
        - Download the credentials file and save it in the file-transfer/google-drive directory
    
    Gmail:
        - Go to the link: https://developers.google.com/gmail/api/quickstart/python
        - select the "Enable the Drive API"
        - If you are not signed into a Google Account, sign in or create an account
            - This is the account that will be use for sending emails
        - Follow the instructions to create the app
        - Download the credentials file and save it in the mail/gmail/ directory with the python scripts for sending gmail emails

3. Enable the Dropbox API
    - An app has to be created to give the scripts access to your dropbox account
    
    - Create a Dropbox account or sign into dropbox.
    - Go to the link: https://www.dropbox.com/developers/apps
    - Select the "Create app" button and follow the instructions to make an app.
    - In the app settings under the OAuth 2 section, select the "Generate" button under "Generate access token"
    - Copy this token into the source files "dbdownload.py" and "dropboxupload.py" where it says "REPLACE WITH ACCESS TOKEN"
    - Go to your account home and go into the directory "Apps > <Your App Name>" and create the inputs directory.

4. Set your interface for packet captures.
    - The scripts will automatically start tcpdump on the system, however the interface may need to be changed in the scripts from the current interface of "enp0s3"
      to the desired interface.
    - Scripts "main.py" in "mail/gmail/", "dbdownload.py" and "dropboxupload.py" in "file-transfer/dropbox",
      and "drive_down.py" and "drive_up.py" in "file-transfer/google-drive"

5. Starting the scripts:
    Gmail:
        - enter the directory email/gmail
        - Edit the file spam_mail.csv and add all receiving email addresses in the file, with each address being its own line
        - First time run:
            - run 'sudo python main.py --noauth_local_webserver"
            - Visit the link displayed and select a google account to use
            - Copy the access code
        - Subsequent Runs:
            - run 'sudo python main.py --noauth_local_webserver"
    
    Google Drive:
        - enter the directory file-transfer/google-drive
            - Create the directory inputs
            - add files to be uploaded into inputs

        - Upload:
            - First time run (for either upload or download):
                - run 'sudo python drive_up.py --noauth_local_webserver"
                - Visit the link displayed and select a google account to use
                - Copy the access code
            - Subsequent runs:
                - run 'sudo python drive_up.py'

        - Download:
            - ensure there are files uploaded to the Google Drive account
            - First time run (for either upload or download):
                - run 'sudo python drive_down.py --noauth_local_webserver"
                - Visit the link displayed and select a google account to use
                - Copy the access code
            - Subsequent runs:
                - run 'sudo python drive_down.py'

    Dropbox:
        - enter the directory "file-transfer/dropbox"
            - Create the directory inputs
            - add files to be uploaded into inputs
        
        - Upload:
            - run 'sudo python dropboxupload.py'

        - Download:
            - ensure there are files in the Apps' inputs directory
            - run 'sudo python dbdownload.py'


VoIP:
=====
- The following automation is done with the use of selenium and a browser's webdriver
- The Selenium python library should have been installed with the other packages from the requirements
    - If not, then run 'pip install selenium'

1. Install your browser's webdriver
    - Chrome webdriver can be found here: https://chromedriver.chromium.org/downloads
        - Make note of which version of Chrome you are using. Each chrome version has its own webdriver
    - Firefox's webdriver can be found here: https://github.com/mozilla/geckodriver/releases/tag/v0.24.0
    - extract the webdriver executable and make note of its file path. 
        - It does not have to be in a specific location

Skype:
    - Two accounts will be required for performing Skype VoIP automation
    - The account that will be making the calls, enter in the information into the python scripts as outline below
    - Install the Skype desktop application
        - Does not have to be the same machine running the scripts
    - Login to the desktop application with the second account
    - At the top left corner, beside the search bar click the dial pad button
    - Click the settings gear icon at the top right > Advanced > Answer incoming calls automatically
        - This will cause the receiver to automatically answer calls so the only user input required is starting the script

    Configure the Scripts
        - in voip/skype/skype.py, there are a list of variables required to be filled out
            - DRIVER_PATH   ==> absolute path to the webdriver donwloaded earlier
            - EMAIL         ==> email address for the Skype account that will perform the calls
            - PASSWORD      ==> password for the Skype account that will perform the calls
            - CONTACT_NAME  ==> contact name that is displayed in the contacts list of the call receiver
            - CALL_DURATION ==> duration of the Skype calls
            - PCAP_DIR      ==> directory holding all the pcaps from capturing the VoIP calls
                                The PCAPs are named skype-voip-<Number>.pcap. If the script is run a second time, it will overwrite the pcaps in the PCAP_DIR

        - in voip/skype/skype.py, set the values in the for loop at line 109 to set how many calls will be created and captured
            - Because PCAP names are based on the interation number they occur, unless the PCAP_DIR is changed or the start of the loop is increased,
                PCAPs will be overwritten if the script is run again

    Run the Scripts
        - enter directory voip/skype
        - run 'sudo -v'
        - run 'python skype.py'

Facebook Messenger:
    - An iPhone is required to automate Facebook Messenger VoIP. It has the ability to auto answer calls.
    - Create two facebook accounts: 1 for making the call and one for receiving it.
    - Setup the receiving account on the iPhone
    - Set the variables at line 13 of voip/messenger/messenger.py to their correct values for your setup
        - the 'CALL_RECEIVER' is a value found in the URL.
            - Login to "messenger.com" and select the receiver from your friends list. The URL will look like "messenger.com/t/<friend id>
            - 'CALL_RECEIVER' should be equal to <friend id>
            - It is probably in the form of "firstname.lastname.<some number>'

    Running the Scripts:
        - run 'sudo -v'
        - run 'python messenger.py'
            - the PCAPs may be overwritten if you rerun the script without renaming the PCAPs first


Text Chat:
==========
Telegram:
    Install the following packages:
        - pip install python-telegram-bot
        - If an issue is encountered for installed in the cryptography package, install the following packages
            - sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
            - If not using Ubuntu, visit: https://cryptography.io/en/latest/installation/#building-cryptography-on-linux
        - snap install telegram-cli
            - If you do not have snap, built telegram-cli from source: https://github.com/vysheng/tg

    1. Create a Telegram account through downloading the app on either Android or iPhone
    2. Create a bot
        - Through the Web:
            - Log into telegram in the browser: https://web.telegram.org/#/login
            - Start a conversation with @BotFather with the following link: https://web.telegram.org/#/im?p=@BotFather
        - Through the App:
            - Search for @BotFather and start a conversation
        - Type '/newbot' and follow the instructions
    3. Copy the API token and set it as the value for the variable BOT_TOKEN at line 4 in text-chat/telegram/telegram-bot.py
    4. Set BOT_NAME at line 6 in text-chat/telegram/telegram-bot.py to the username assigned to the bot
        - Should be in the form of @<Entered Name>Bot, where <Entered Name> is the name you gave your bot
    5. Set INTERFACE at line 7 in text-chat/telegram/telegram-bot.py to the interface that will be monitored
    6. The loop at line 17 sets how many messages will be sent to the bot in the PCAP. Feel free to adjust that value
    7. Run telegram-cli and login with the Telegram account created

    Run the Scripts:
        - enter the directory text-chat/telegram/
        - Telegram Bot:
            - run 'python telegram-bot.py'
            - Using the telegram app, start a conversation with bot to confirm it is running
            - Any message sent to the bot should be sent back to you but all letters will be capitalized
        - Sender:
            - run 'sudo -v'
            - run 'python telegram-sender.py'
            - the pcap will be stored in the file 'telegrambot.pcap'
                - rename the file before running the script again or else the file will be overwritten

Facebook Messenger:
    Setup:
        - set the value to DRIVER_PATH and INTERFACE in text-chat/facebook/messenger.py at line 14 and 15 to the path of chrome browser driver and monitored interface
        - No further setup should be needed, all login credentials needed are present in text-chat/facebook/messenger.py

        - If the automation does not work and the bot does not respond, follow the instructions at the following link to set up a bot:
            https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start
            - I recommend setting up the webhook with Glitch. The file text-chat/facebook/webhook/app.js contains all the code to make the bot functional
        - Assign the correct values to the variables at line 15 of text-chat/facebook/messenger.py if a new account was created

   
    Running Scripts:
        1. run 'sudo -v'
        2. run 'python messenger.py'
            - The pcap will be saved just as "facebook.pcap". Restarting the script without renaming the PCAP will cause the PCAP to be overwritten


Email:
======
Yahoo:
    Setup:
        - Create a yahoo email account and a second account for receiving the emails
        - Set the variables at line 11 in mail/yahoo-mail/yahoo-mail.py to the appropriate values

    Running Scripts:
        1. run 'sudo -v'
        2. run 'python yahoo-mail.py'
            - The PCAP is saved as "yahoo_mail.pcap". Rerunning the script without changing the PCAP name will overwrite the PCAP
