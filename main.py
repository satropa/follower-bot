from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

WHERE_FOLLOWERS = # Account from where you want to follow followers
USERNAME = # Instagram username
PASSWORD = # Password


class InstaFollower:

    def __init__(self):
        """Instagram Follower Bot Class"""
        self.s = Service('C:\Development\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)

    def login(self):
        """Login to Instagram"""
        self.driver.get("https://www.instagram.com/")
        time.sleep(random.uniform(3.5, 4.5))
        # Allow cookies
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/'
                                                'div[1]/div/div[2]/div/div/div/'
                                                'div/div[2]/div/button[1]').click()
        time.sleep(random.uniform(3.5, 4.5))
        # Login with Facebook
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button').click()
        time.sleep(random.uniform(3.5, 4.5))
        # Allow Cookies
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[1]').click()
        time.sleep(random.uniform(3.5, 4.5))
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(USERNAME)
        time.sleep(random.uniform(2.5, 3.5))
        self.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(PASSWORD + Keys.ENTER)
        # Wait for Instagram to load up
        time.sleep(20)

        # Notifications off
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]'
                                           '/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    def find_followers(self):
        """Find the account from where you going to follow followers"""
        # Search button
        time.sleep(random.uniform(2.5, 3.5))
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]'
                                           '/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a').click()
        time.sleep(random.uniform(2.5, 3.5))
        # Search the account
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]'
                                           '/div[1]/div/div/div[2]/div/div/'
                                           'div[2]/div[1]/div/input').send_keys(WHERE_FOLLOWERS + Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/'
                                           'div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]'
                                           '/div[2]/div/div[1]/div/a').click()

        time.sleep(random.uniform(3.5, 4.5))
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/'
                                           'div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(random.uniform(3.5, 4.5))

    def follow(self):
        """Start following followers"""
        followers = self.driver.find_element(by="css selector", value='div._aano')
        for num in range(1, 10000):
            time.sleep(random.uniform(2.5, 3.5))
            follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/'
                                                         f'div[2]/div/div/div/div/div[2]/div/div/'
                                                           f'div[2]/div[1]/div/div[{num}]/div[3]/button')
            if follow_button.text == "Follow":
                follow_button.click()
                time.sleep(random.uniform(1.5, 2.5))
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            else:
                pass




bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

