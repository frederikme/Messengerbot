from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
# for our print statements and layout in terminal/command prompt
import pyfiglet
import os
import time

class MessengerBot:

    def __init__(self, email, password):
        self.logToScreen("Messengerbot", isBanner=True)
        self.logToScreen("-> Made by Frederikme")
        self.logToScreen("-----------------------------------\n\n")

        self.logToScreen("Getting ChromeDriver ...")
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        self.email = email
        self.password = password

    def loadPage(self, url):
        self.logToScreen("Loading page %s" % str(url))
        self.browser.get(url)
        # optionally add storage and readability of cookies with pickle

    def login(self):
        if self.isLoggedIn():
            self.logToScreen("You are already logged in")
            return

        while True:
            self.loadPage("http://messenger.com/login")

            # wait for elements to be loaded
            delay = 5
            try:
                WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.NAME, 'email')))
            except TimeoutException:
                self.logToScreen("Loading took too much time! Let's try again.")
                continue

            try:
                emailInput = self.browser.find_element_by_name('email')
                passwordInput = self.browser.find_element_by_name('pass')

                emailInput.send_keys(self.email)
                passwordInput.send_keys(self.password)
                passwordInput.send_keys(Keys.ENTER)

            except Exception as e:
                self.logToScreen(e)
                continue
            break

    def getChat(self, chatid):
        if not self.isLoggedIn():
            self.logToScreen("Need to login first before getting chat")
            self.login()

        # check if correct chat is already opened
        url = self.browser.current_url
        if "messenger.com/t/{}".format(chatid) in url:
            return

        while True:

            self.loadPage('https://www.messenger.com/t/' + chatid)

            # wait for elements to be loaded
            delay = 5
            try:
                WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, '_5rpb')))
            except TimeoutException:
                self.logToScreen("Loading took too much time! Let's try again.")
                continue

            break

    def getChatIDs(self):
        if not self.isLoggedIn():
            self.logToScreen("need to login first before getting chat")
            self.login()

        # gets chats that you see on your left
        while True:
            self.logToScreen("Fetching your chats and IDs ...")
            names = []
            ids = []

            delay = 5
            try:
                WebDriverWait(self.browser, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//div')))
            except TimeoutException:
                self.logToScreen("Loading took too much time! Let's try again.")
                continue

            attributes = self.browser.find_elements_by_xpath("//div")

            for attribute in attributes:

                try:
                    name = attribute.get_attribute("data-tooltip-content")
                except:
                    continue

                if not name: continue

                names.append(name)

            attributes = self.browser.find_elements_by_xpath("//a")

            for attribute in attributes:

                link = attribute.get_attribute("data-href")

                if not link: continue

                if "messenger.com/t/" in link:
                    if "#" in link:
                        link = link[:-1]
                    id = link.split("t/")[1]
                    if id not in ids:
                        ids.append(id)

            chat_ids = [("NAME", "CHATID")] + list(zip(names, ids))

            return chat_ids

        return None

    def sendChatMessage(self, chatid, message):
        self.getChat(chatid)
        while True:

            try:
                elements = self.browser.find_elements_by_class_name('_5rpu')

                # check if it is a groupchat
                if len(elements) > 1:
                    # isgroupchat
                    chatmessage_box = elements[1]
                else:
                    # is individual 1-to-1 chat
                    chatmessage_box = elements[0]

                chatmessage_box.send_keys(message)
                chatmessage_box.send_keys(Keys.ENTER)

                break

            except TimeoutException:
                self.logToScreen("Loading took too much time! Let's try again.")
                continue

        return

    def changeChatName(self, chatid, name):

        self.getChat(chatid=chatid)

        elements = self.browser.find_elements_by_class_name('_5rpu')

        chatname_box = elements[0]

        # clear current textname of the chat assuming it has less than 20 characters
        for _ in range(20):
            chatname_box.send_keys(Keys.BACK_SPACE)

        chatname_box.send_keys(name)
        chatname_box.send_keys(Keys.ENTER)

        return

    def isLoggedIn(self):
        # check if chat is already opened
        url = self.browser.current_url
        if "messenger.com/t/" in url:
            return True
        else:
            return False

    def logToScreen(self, text, isBanner=False):
        if isBanner:
            # clear the terminal
            os.system("clear")
            banner = pyfiglet.figlet_format(text)
        else:
            # provide one line space in between
            print("\n")
            banner = text

        print(banner)
        # give time to let the shown message in console sink in
        time.sleep(1)