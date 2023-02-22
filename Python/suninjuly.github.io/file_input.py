from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//body/div[1]/form[1]/div[1]/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//body/div[1]/form[1]/div[1]/input[2]")
    input2.send_keys("Lapin")
    input3 = browser.find_element(By.XPATH, "//body/div[1]/form[1]/div[1]/input[3]")
    input3.send_keys("ivan.lapin@ivanlapin.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element(By.XPATH, "// input[ @ id = 'file']").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы




except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    # закрываем браузер после всех манипуляций
    browser.quit()