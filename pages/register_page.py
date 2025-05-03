from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")

    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")

    def go_to_register_page(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.REGISTER_LINK)

    def fill_registration_form(self, fname, lname, email, phone, pwd):
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.EMAIL, email)
        self.type(self.TELEPHONE, phone)
        self.type(self.PASSWORD, pwd)
        self.type(self.CONFIRM_PASSWORD, pwd)
        self.click(self.AGREE_CHECKBOX)
        self.click(self.CONTINUE_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
