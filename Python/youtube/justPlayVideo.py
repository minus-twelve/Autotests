from selenium import webdriver

from selenium.webdriver.common.by import By

import time

link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

try:
   browser = webdriver.Chrome()
   browser.get(link)
   button = browser.find_element(By.ID, "movie_player")
   button.click()
   time.sleep(240)



finally:
   time.sleep(10)
   browser.quit()