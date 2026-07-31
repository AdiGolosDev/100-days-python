from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep, time
import os

ACCOUNT_USER = "abcdefgh"
ACCOUNT_EMAIL = "somename@test.com"
ACCOUNT_PASS = "somepass12345678"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 2)

login_button = driver.find_element(by=By.ID, value="login-button")
login_button.click()

login = driver.find_element(by=By.ID, value="email-input")
login.send_keys(ACCOUNT_EMAIL, Keys.TAB, ACCOUNT_PASS, Keys.TAB, Keys.ENTER)

wait.until(ec.presence_of_all_elements_located((By.ID, "schedule-page")))

days = driver.find_elements(By.CLASS_NAME, value="Schedule_dayGroup__y79__")

for day in days:
    if "Tue" in day.text:
        classes = day.find_elements(By.CLASS_NAME, value="ClassCard_card__KpCx5")
        for c in classes:
            if "6:00 PM" in c.text:
                button = c.find_element(By.CSS_SELECTOR, value="button")
                button.click()
                break
        break

input("enter to quit")
driver.quit()
