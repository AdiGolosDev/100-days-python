from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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



input("Press enter to quit")
driver.quit()
