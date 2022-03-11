web_url = "http://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/hudayis/Documents/Development/chromedriver.exe"

ser = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(web_url)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("manu")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("sakura")

email = driver.find_element(By.NAME,"email")
email.send_keys("mmanusx@gmail.com")

sing_up_button = driver.find_element(By.CSS_SELECTOR, "form button.btn")
sing_up_button.click()
# sing_up_button.send_keys(Keys.ENTER)

driver.quit()


