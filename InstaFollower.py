from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class InstaFollower():
    def __init__(self,path):
        self.driver = webdriver.Chrome(path)

    def login(self, username, password, url):
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)

    def findusers(self, account):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(account)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        self.pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
        time.sleep(3)

    def follow(self):
        while True:
            buttons = self.driver.find_elements_by_css_selector("li button")
            for n in buttons:
                try:
                    n.click()
                    time.sleep(1)
                except:
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                else:
                    time.sleep(1)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', self.pop_up_window)
            time.sleep(1)