from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {
    i: {'time': time.text, 'name': name.text}
    for i, (time, name) in enumerate(zip(event_times, event_names))
}

print(events)


# product_name = driver.find_element(By.ID, value="productTitle").text
# print(product_name)
# # By.css_selector also exists
# careers_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[1]/div/div[1]/ul/li[1]/a')
# print(careers_link.text)
# driver.close() closes one tab
driver.quit() # closes entire browser
