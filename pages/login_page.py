import logging

import allure

from locators.auth_locators import AuthLocators

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def login_button(self):
        return self.app.wd.find_element(*AuthLocators.SUBMIT_LOGIN)

    def code_button(self):
        return self.app.wd.find_element(*AuthLocators.SUBMIT_CODE)

    @allure.step("Авторизация")
    def auth(self):
        logger.info("Default authorization")
        self.login_button().click()
        self.code_button().click()
