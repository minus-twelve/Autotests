from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
time.sleep(1)
alert = browser.switch_to.alert
print(alert.text)
alert.accept()
browser.quit()