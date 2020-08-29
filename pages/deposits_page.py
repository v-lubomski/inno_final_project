import logging
from time import sleep

import allure
from selenium.webdriver import ActionChains

from common.common_locators import CommonLocators
from locators.deposits_locators import DepositLocators

logger = logging.getLogger()


class DepositsPage:
    def __init__(self, app):
        self.app = app

    @allure.step("Opening the deposits page")
    def open_deposits_page(self):
        logger.info("Opening the deposits page")
        self.app.wd.find_element(*CommonLocators.DEPOSITS_TAB).click()

    @allure.step("Select deposit")
    def select_deposit(self, currency, time):
        logger.info('Click to "Open deposit" button')
        self.app.wd.find_element(*DepositLocators.OPEN_DEPOSIT).click()
        logger.info("Set deposits filter")
        self.app.wd.find_element(*DepositLocators.concrete_currency(currency)).click()
        self.app.wd.find_element(*DepositLocators.deposit_time(time)).click()
        logger.info('Click to "Open deposit" button for concrete deposit')
        self.app.wd.find_element(*DepositLocators.OPEN_CONCRETE_DEPOSIT).click()

    @allure.step("Fill new deposit form")
    def fill_new_deposit_form(self, account, due_date, amount):
        logger.info("Fill new deposit form")
        self.app.wd.find_element(*DepositLocators.ACCOUNT_FOR_DEPOSIT).send_keys(
            account
        )
        self.app.wd.find_element(*DepositLocators.END_DATE).send_keys(due_date)
        self.app.wd.find_element(*DepositLocators.END_DATE).clear()
        self.app.wd.find_element(*DepositLocators.END_DATE).send_keys(due_date)
        self.app.wd.find_element(*DepositLocators.AMOUNT).clear()
        self.app.wd.find_element(*DepositLocators.AMOUNT).send_keys(amount)

    @allure.step("Confirm the deposit opening")
    def confirm_deposit_opening(self):
        logger.info("Click to all confirmation buttons")
        sleep(1)
        self.app.wd.find_element(*DepositLocators.FORWARD_BUTTON).click()
        self.app.wd.find_element(*DepositLocators.CHECKBOX).click()
        self.app.wd.find_element(*DepositLocators.CONFIRM_BUTTON).click()

    @allure.step("Check is deposit opened")
    def is_deposit_opened(self):
        logger.info("Check is deposit opened")
        message = self.app.wd.find_element(*DepositLocators.SUCCESSFUL_MESSAGE).text
        success_message = "Deposit has been created"
        result = success_message in message
        return result

    @allure.step('Click "Show closed deposits"')
    def show_closed_deposits(self):
        logger.info('Click "Show closed deposits"')
        self.app.wd.find_element(*DepositLocators.SHOW_CLOSED_DEPOSITS).click()

    @allure.step("Get closed deposits title")
    def closed_deposits_title(self):
        logger.info("Get closed deposits title")
        return self.app.wd.find_element(*DepositLocators.TITLE).text

    @allure.step("Click to the deposit alias")
    def click_to_the_deposit_alias(self):
        logger.info("Click to the first deposit alias")
        self.app.wd.find_element(*DepositLocators.ONE_OF_DEPOSITS).click()

    @allure.step("Get deposit details title")
    def deposit_details_title(self):
        logger.info("Get deposit details title")
        return self.app.wd.find_element(*DepositLocators.TITLE).text

    @allure.step("Edit deposit alias")
    def edit_alias(self, alias):
        logger.info("Edit deposit alias")
        edit_button = self.app.wd.find_element(*DepositLocators.EDIT_ALIAS_BUTTON)
        ActionChains(self.app.wd).move_to_element(edit_button).perform()
        edit_button.click()
        self.app.wd.find_element(*DepositLocators.EDIT_INPUT).clear()
        self.app.wd.find_element(*DepositLocators.EDIT_INPUT).send_keys(alias)
        self.app.wd.find_element(*DepositLocators.OK_BUTTON).click()

    @allure.step("Get deposit alias")
    def deposit_alias(self):
        logger.info("Get deposit alias")
        sleep(0.5)
        return self.app.wd.find_element(*DepositLocators.ALIAS).text
