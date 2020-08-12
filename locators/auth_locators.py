from selenium.webdriver.common.by import By


class AuthLocators:
    SUBMIT_LOGIN = (By.ID, "login-button")
    SUBMIT_CODE = (By.ID, "login-otp-button")
