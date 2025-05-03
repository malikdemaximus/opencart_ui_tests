import unittest
from selenium import webdriver
from pages.register_page import RegisterPage

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_register_valid(self):
        register_page = RegisterPage(self.driver)
        register_page.open("http://yourwebsite.com")
        register_page.go_to_register_page()
        register_page.fill_registration_form("John", "Doe", "john.doe@example.com", "1234567890", "password123")
        success_message = register_page.get_success_message()
        self.assertEqual(success_message, "Your Account Has Been Created!")

    def test_register_invalid(self):
        register_page = RegisterPage(self.driver)
        register_page.open("http://yourwebsite.com")
        register_page.go_to_register_page()
        register_page.fill_registration_form("John", "Doe", "invalid_email", "1234567890", "password123")
        # Здесь можно проверить наличие сообщения об ошибке

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
