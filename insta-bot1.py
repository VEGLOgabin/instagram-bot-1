from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.instagram.com/wsj/"

def instagram_profile_scraper():
    # Initialize WebDriver
    driver = webdriver.Firefox() 
    
    # Open the URL
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(2)  
    
    try:
        
        followers = driver.find_element(By.CSS_SELECTOR, ".x2pgyrj:nth-child(2) ._ap30")
        
        print(followers.text)
        
        posts= driver.find_element(By.CSS_SELECTOR, ".x2pgyrj:nth-child(1) ._ap30").text
        print(posts)
        
        following= driver.find_element(By.CSS_SELECTOR, ".x2pgyrj~ .x2pgyrj+ .x2pgyrj ._ap30").text
        print(following)
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close the driver
        driver.quit()

# Call the function to start scraping
instagram_profile_scraper()