from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import json
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
   "--disable-notifications"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://facebook.com')
email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
email_input.send_keys("abdeldroid1@gmail.com")

password_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
password_input.send_keys("Simou2007")

login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
login_button.click()
time.sleep(3)
driver.get('https://www.facebook.com/search/pages/?q=clothes')
time.sleep(1)
for i in range(8):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.save_screenshot('t.png')
pages = driver.find_elements(By.CSS_SELECTOR, "a[role='presentation']")
values = []
for anchor in pages:
    href_value = anchor.get_attribute("href")
    values.append(href_value)
json = json.dumps(values) 
with open('link2.json', "w", encoding="utf-8") as f:
    f.write(json)

