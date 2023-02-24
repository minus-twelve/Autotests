import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    out = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(out)
    browser.find_element(By.TAG_NAME, 'button').click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(3)
    browser.quit()
