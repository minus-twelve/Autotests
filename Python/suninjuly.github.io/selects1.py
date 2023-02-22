from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link="http://suninjuly.github.io/selects1.html"

try:
   browser = webdriver.Chrome()
   browser.get(link)


   a=browser.find_element(By.CSS_SELECTOR, "#num1").text
   newa=int(a)
   b=browser.find_element(By.CSS_SELECTOR, "#num2").text
   newb=int(b)
   newres=newa+newb
   finalres=str(newres)
   select = Select(browser.find_element(By.TAG_NAME, "select"))
   select.select_by_value(value=str(finalres))
   browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
   time.sleep(1)
   alert = browser.switch_to.alert
   print(alert.text)
   alert.accept()
# После выполнения всех действий мы должны не забыть закрыть окно браузера
   browser.quit()