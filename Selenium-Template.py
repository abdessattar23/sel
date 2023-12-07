import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import json
display = Display(visible=0, size=(800, 800))  
display.start()

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--disable-notifications",
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

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://facebook.com')
email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
email_input.send_keys("abdeldroid1@gmail.com")

password_input = driver.find_element(By.CSS_SELECTOR, "input#pass")
password_input.send_keys("Abdessattar@2007@")

login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
login_button.click()
time.sleep(3)
driver.save_screenshot('screenshot2.png')
driver.get('https://www.facebook.com/search/pages/?q=clothes')
time.sleep(1)
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.save_screenshot('t0.png')
#pages = r(driver.page_source)
values = []


def r(pg):
    sp = BeautifulSoup(pg, 'html.parser')
    ps = []
    #rsp = BeautifulSoup(page_source, 'html.parser')
   # reslts = sp.find_all(string=re.compile(r'(?<=<)[^<>]*@[^<>]*(?=)'))
    page_results = sp.find_all('div', {'class': 'search-result'})    
    for result in page_results:
       page_name = result.find('div', {'class': 'clearfix'}).text.strip()

       page_info = {
        'Page Name': page_name,
        'Page Link': page_link
}
       ps.append(in)
       print(f'Page Name: {page_name}')
       print(f'Page Link: {page_link}')
       print('---')



    # Print the results
  #  for result in reslts:
   #     print(result)
    #    print('hello')


def get_data(driver, id):
    driver.get('https://mbasic.facebook.com/' + id)
    res = driver.page_source
    soup = BeautifulSoup(res, "html.parser")
    info = soup.find(id="contact-info")
    return info


#for anchor in pages:
#    href_value = anchor.get_attribute("href")
#    id = href_value.replace("https://www.facebook.com/", "")
 #   contact = get_data(driver, id)
  #  values.append(contact)

#json_data = json.dumps(values)
with open('links5.json', 'w') as file:
    json.dump(ps, file)

print(f'Data saved to links5.json successfully.')

r(driver.page_source)
