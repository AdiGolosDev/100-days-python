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

classes_booked = 0
waitlists_joined = 0
days = driver.find_elements(By.CLASS_NAME, value="Schedule_dayGroup__y79__")
appointments = []

def print_class(day, card, bw):
    appointments.append(card)
    date = day.find_element(By.CSS_SELECTOR, value="h2[id^='day-title-']")
    time = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']")
    details = card.find_elements(By.CSS_SELECTOR, value="p[class^='ClassCard_classDetail']")
    details_string = f""
    for d in details:
        details_string += d.text + "\n"
    print(f"Class on {date.text}, at {time.text} {bw}\nDetails:\n{details_string}")



for day in days:
    if "Tue" in day.text or "Thu" in day.text:
        classes = day.find_elements(By.CLASS_NAME, value="ClassCard_card__KpCx5")
        for c in classes:
            if "6:00 PM" in c.text:
                try:
                    button = c.find_element(By.CSS_SELECTOR, value="button")
                    if button.text.lower() == "booked":
                        print("Already Booked!")
                        break
                    elif button.text.lower() == "waitlisted":
                        print("Already Waitlisted!")
                        break
                    elif button.text.lower() == "book class":
                        button.click()
                        print_class(day, c, "booked")
                        classes_booked += 1
                    elif button.text.lower() == "join waitlist":
                        button.click()
                        print_class(day, c, "wait-listed")
                        waitlists_joined += 1
                except NoSuchElementException:
                    print("found the class, but couldn't book for some reason...")
                break

booked_waitlisted = len(appointments)
print(f"--- BOOKING SUMMARY ---\nClasses booked: {classes_booked}\nWaiting lists joined: {waitlists_joined}\nAlready Booked/Wait-listed: {booked_waitlisted}")

input("enter to quit")
driver.quit()
