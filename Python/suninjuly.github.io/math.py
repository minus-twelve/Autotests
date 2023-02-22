import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    #print(x_element)
    x = x_element.text
    #print(x)
    y = calc(x)
    #print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Robots rule')]").click()
    input4 = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()









