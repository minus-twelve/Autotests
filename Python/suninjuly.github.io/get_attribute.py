import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    new=x_element.get_attribute("valuex")
    print(new)

    willbesend=calc(new)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(willbesend)
    input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    input4 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()

