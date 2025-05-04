import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.open(f"{BASE_URL})
        login_page.go_to_login_page()
        login_page.login("valid_user@example.com", "valid_password")

    def test_login_invalid(self):
        login_page = LoginPage(self.driver)
        login_page.open(f"{BASE_URL})
        login_page.go_to_login_page()
        login_page.login("invalid_user@example.com", "invalid_password")
        error_message = login_page.get_warning_message()
        self.assertEqual(error_message, "Warning: No match for E-Mail Address and/or Password.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
