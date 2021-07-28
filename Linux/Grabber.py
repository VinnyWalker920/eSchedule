import time

import selenium
from selenium import webdriver


class scheduleGrabber:
    def __init__(self, user, pwd, headless=False):
        '''
        :param user: K username (String)
        :param pwd: K password (String)
        :param headless: If TRUE chrome window will not open otherwise it will (Boolean)
        Gathers schedule details and aggregates website source
        '''

        chromeDriver = DRIVEREXEPATH
        self.chromeOptions = webdriver.ChromeOptions()
        if headless is True:
            self.chromeOptions.add_argument("--window-size=1920,1080")
            self.chromeOptions.add_argument("--disable-extensions")
            self.chromeOptions.add_argument("--proxy-server='direct://'")
            self.chromeOptions.add_argument("--proxy-bypass-list=*")
            self.chromeOptions.add_argument("--start-maximized")
            self.chromeOptions.add_argument('--headless')
            self.chromeOptions.add_argument('--disable-gpu')
            self.chromeOptions.add_argument('--disable-dev-shm-usage')
            self.chromeOptions.add_argument('--no-sandbox')
            self.chromeOptions.add_argument('--ignore-certificate-errors')
            self.chromeOptions.add_argument('--allow-running-insecure-content')

        self.schedule = {'Sunday': None, 'Monday': None, 'Tuesday': None, 'Wednesday': None, 'Thursday': None,
                         'Friday': None, 'Saturday': None, }
        self.browser = webdriver.Chrome(executable_path=chromeDriver, chrome_options=self.chromeOptions)
        self.username = user
        self.password = pwd
        self.schedulePortalLink = PUTLINKHERE
    def grabber(self):
        '''Logins in and scrapes schedule + Parses schedule source'''

        self.browser.get(self.schedulePortalLink)
        time.sleep(1)
        usernameElement = self.browser.find_element_by_id("KSWUSER")
        passwordElement = self.browser.find_element_by_id("PWD")
        usernameElement.send_keys(self.username)
        passwordElement.send_keys(self.password)

        self.browser.find_element_by_class_name("actionButtons").find_element_by_xpath("//div/input[1]").click()
        try:
            time.sleep(1)
            self.browser.find_element_by_id("btnContinue").click()
        except(selenium.common.exceptions.NoSuchElementException):
            pass

        for x, i in enumerate(self.schedule):
            time.sleep(1)
            parsedInfo = (self.browser.find_element_by_class_name("child" + str(x + 1)).text).split("\n")
            self.schedule[i] = parsedInfo
        print('Successful')

    def getSchedule(self):
        """
        Return schedule if empty grabs schedule and returns it
        :return: Schedule hashmap(Dictionary)
        """
        if self.schedule['Sunday'] is None:
            self.grabber()
            return self.schedule
        else:
            return self.schedule

    def closeWindow(self):
        """
        Closes browser
        """
        self.browser.quit()
