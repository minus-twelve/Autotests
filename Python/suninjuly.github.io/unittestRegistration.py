import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
