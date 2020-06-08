from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

if len(sys.argv) != 3:
  raise Exception("need 2 arguments")

Username = sys.argv[1]
Password = sys.argv[2]

# Start headless Chrome without display
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.headless = True
command_executor = "http://localhost:4444/wd/hub"
driver = webdriver.Remote(command_executor, desired_capabilities=options.to_capabilities())

# driver = webdriver.Chrome(executable_path = "/Users/sachiniyer/docs/coding/Python/env/projects/web_automation/chromedriver")
driver.get('https://sameday.costco.com/')

# Enter zip code
zip_code = driver.find_element_by_id('signup-zipcode')
zip_code.send_keys('95125')

# Submit button
continue_box = driver.find_element_by_class_name('rcp-form-submit-button')
driver.implicitly_wait(2)
continue_box.click()

# Enter email
driver.implicitly_wait(2)
email_box = driver.find_element_by_id('logonId')
email_box.send_keys(Username)

# Enter password
pass_box = driver.find_element_by_id('logonPassword')
pass_box.send_keys(Password)

# Continue box
continue_box = driver.find_elements(By.CLASS_NAME, "primary")
driver.implicitly_wait(1)
continue_box[1].click()

# Open deliveries
driver.implicitly_wait(5)
button = driver.find_element_by_xpath("//*[@id='header']/div/div/div[5]/div[2]/span/a")
button.click()

# Open deliveries 2
driver.implicitly_wait(5)
button = driver.find_element_by_xpath("//*[@id='react-tabs-2']")
button.click()

driver.implicitly_wait(5)
try:
  value = driver.find_element_by_xpath("//*[@id='react-tabs-1']/div/div/div/div/div/div/h1")
  time = value.text
except:
  try:
    driver.implicitly_wait(5)
    value = driver.find_element_by_xpath("//*[@id='react-tabs-3']/div/div/div/div/div[1]/div/div/div")
    time = value.text
  except:
    time = "Delivery Available"
finally:
  driver.quit()
  print(time)
