from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


class InstaBot:
    def __init__(self):
        self.chrome_driver_path = "C:/Users/robertp/Development/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_path)
        self.url = "https://www.instagram.com/"
        self.email = "YOUR_EMAIL"
        self.password = "YOUR_PASSWORD"
        self.username = "YOUR_USERNAME"
        self.similar_account = "https://www.instagram.com/cookingwithayeh/"

    def login(self):
        # stuck - cannot find element - It changes depending on if clicked or not
        # both login and password inputs do this!
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element(By.NAME, 'username').send_keys(self.email)
        time.sleep(1)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'button[class ="sqdOP  L3NKy   y3zKF     "]').click()
        time.sleep(3)
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CSS_SELECTOR, '.mt3GC .HoLwm').click()
        except NoSuchElementException:
            print("No notifications popup today")

    def find_followers(self):
        time.sleep(3)
        self.driver.get(self.similar_account)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href = "/cookingwithayeh/following/"]').click()

    def follow(self):
        time.sleep(3)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

