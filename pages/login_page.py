from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def go_to_login_page(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_LINK)

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_warning_message(self):
        return self.get_text(self.WARNING_MESSAGE)
