from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   browser = webdriver.Chrome()
   browser.get("http://suninjuly.github.io/explicit_wait2.html")
   button=browser.find_element(By.CSS_SELECTOR, "#book")
   WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")

   )
   button.click()
   x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
   x = x_element.text
   y = calc(x)
   input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
   input1.send_keys(y)
   submit = browser.find_element(By.CSS_SELECTOR, "#solve").click()

finally:
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()
