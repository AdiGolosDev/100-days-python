from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first = driver.find_element(By.NAME, value="fName")
first.send_keys("someFirstName", Keys.TAB, "someLastName", Keys.TAB, "some@Email.com", Keys.TAB, Keys.ENTER)

# num_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(num_of_articles)
# num_of_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Lord of Mysteries", Keys.ENTER)

input("press enter to quit")

driver.quit()
