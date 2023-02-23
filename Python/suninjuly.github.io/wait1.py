from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.XPATH, "//div[@id='verify_message']")
    print(message.text)
    assert "successful" in message.text
 
finally:
    time.sleep(2)
    browser.quit()
