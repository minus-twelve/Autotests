from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first = browser.find_element(By.XPATH, "//button[contains(text(),'I want to go on a magical journey!')]").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    input2 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    alert = browser.switch_to.alert
    print(alert.text)
    #print(browser.switch_to.alert.text.split(': ')[-1])
    alert.accept()

    # закрываем браузер после всех манипуляций
    browser.quit()
