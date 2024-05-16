from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

## This instagram was created to scrape follower's profile data

class IntagramBotFollowerScrpaer:
    def __init__(self, email, username, password):
        
        self.email = email
        self.username = username
        self.password = password
        
        
        # Initialize WebDriver
        self.driver = webdriver.Firefox() 
        # self.driver.get(url)
        # self.driver.implicitly_wait(3)
        # time.sleep(3)  
        
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login')
        time.sleep(5)
        
        username = self.driver.find_element(By.NAME,'username')
        password = self.driver.find_element(By.NAME,'password')
        
        username.send_keys(self.email)
        password.send_keys(self.password)
        
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        
        
    def find_user(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{self.username}')
        time.sleep(5)
        
        followers = self.driver.find_element(By.CSS_SELECTOR,'li a ._ac2a')
        followers.click()
        
    def follow(self, number):
        time.sleep(5)
        follow_buttons = []
        for i in range(1, number + 1):
            btn = self.driver.find_element(By.XPATH,f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button')
            follow_buttons.append(btn)
            
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                print("Click has been intercepted by a modal")
    
        


    def scrapeCurrentUserInfos(self):
        try:
            
            followers = self.driver.find_element(By.CSS_SELECTOR, ".x2pgyrj:nth-child(2) ._ap30")
            
            print(followers.text)
            
            posts= self.driver.find_element(By.CSS_SELECTOR, ".x2pgyrj:nth-child(1) ._ap30").text
            print(posts)
            
            following= self.driver.find_element(By.CSS_SELECTOR, ".x2pgyrj~ .x2pgyrj+ .x2pgyrj ._ap30").text
            print(following)
        
        except Exception as e:
            print("An error occurred:", e)
        
        finally:
            pass
        
        
    def getFollowersListAndScrapeProfileInfos(self):
        pass
    
    
    def close_driver(self):
        # Close the driver
        self.driver.quit()

email = "xxxxxxxxxxxx"
username = "xxxxxxxxxxxxx"
password = "xxxxxxxxx"

# bot1 
bot1 = IntagramBotFollowerScrpaer(email,username,password)

bot1.login()
bot1.find_user()
bot1.follow(3)
bot1.close_driver()
