import logging

import allure

from common.common_locators import CommonLocators
from common.common_pages import confirm_sms_code
from locators.accounts_locators import AccountsLocators

logger = logging.getLogger()


class AccountsPage:
    def __init__(self, app):
        self.app = app

    @allure.step("Opening the accounts page")
    def open_accounts_page(self):
        logger.info("Opening the accounts page")
        self.app.wd.find_element(*CommonLocators.ACCOUNTS_TAB).click()

    @allure.step("Click open account button")
    def click_open_account_button(self):
        logger.info("Click open account button")
        self.app.wd.find_element(*AccountsLocators.OPEN_ACCOUNT_BUTTON).click()

    @allure.step("Fill form for new account")
    def fill_form_for_new_account(self, currency, division, agreement):
        logger.info("Fill form for new account")
        self.app.wd.find_element(*AccountsLocators.CURRENCY).send_keys(currency)
        self.app.wd.find_element(*AccountsLocators.DIVISION_OF_BANK).send_keys(division)
        if agreement:
            self.app.wd.find_element(*AccountsLocators.AGREEMENT).click()

    @allure.step("Confirm opening")
    def confirm_opening(self):
        logger.info("Confirm opening")
        self.app.wd.find_element(*AccountsLocators.OPEN_ACCOUNT).click()
        confirm_sms_code(self.app)

    @allure.step("Check is account opened")
    def is_account_opened(self):
        logger.info("Check is account opened")
        message = self.app.wd.find_element(*AccountsLocators.SUCCESS_MESSAGE).text
        success_message = "New account open for operations"
        result = success_message in message
        return result

    @allure.step("Click close account button")
    def click_close_account_button(self):
        logger.info("Click close account button")
        account_operations = self.app.wd.find_elements(
            *AccountsLocators.ACCOUNT_OPERATIONS
        )[-1]
        account_operations.click()
        account_operations.find_element(*AccountsLocators.CLOSE_ACCOUNT).click()

    @allure.step("Pick account for transfer")
    def pick_account_for_transfer(self, account):
        logger.info("Pick account for transfer")
        self.app.wd.find_element(*AccountsLocators.ACCOUNT_FOR_TRANSFER).send_keys(
            account
        )

    @allure.step("Confirm closing account")
    def confirm_closing_account(self):
        logger.info("Confirm closing account")
        self.app.wd.find_element(*AccountsLocators.FORWARD_BUTTON).click()
        confirm_sms_code(self.app)

    @allure.step("Check is account closed")
    def is_account_closed(self):
        logger.info("Check is account closed")
        message = self.app.wd.find_element(*AccountsLocators.SUCCESS_MESSAGE).text
        success_message = "closed"
        result = success_message in message
        return result

    @allure.step("Go to account requisites")
    def go_to_requisites(self):
        logger.info("Go to account requisites")
        account_operations = self.app.wd.find_element(
            *AccountsLocators.ACCOUNT_OPERATIONS
        )
        account_operations.click()
        account_operations.find_element(*AccountsLocators.REQUISITES).click()

    @allure.step("Check requisites title")
    def requisites_title(self):
        logger.info("Check requisites title")
        if self.app.wd.find_elements(*AccountsLocators.REQUISITES_TITLE):
            return True
        else:
            return False

    @allure.step("Close requisites popup")
    def close_requisites(self):
        logger.info("Close requisites popup")
        self.app.wd.find_element(*AccountsLocators.CLOSE_REQUISITES).click()

    #
    # @allure.step('')
    # def(self):
    #     logger.info('')
    #
    # @allure.step('')
    # def(self):
    #     logger.info('')
    #    # @allure.step('')
    # def(self):
    #     logger.info('')
    #
    # @allure.step('')
    # def(self):
    #     logger.info('')
    #
    # @allure.step('')
    # def(self):
    #     logger.info('')
    #
    # @allure.step('')
    # def(self):
    #     logger.info('')
    #


#     def card_element(self, card_name):
#         cards_block = self.app.wd.find_element(*CardsLocators.CARDS_BLOCK)
#         card = cards_block.find_element_by_xpath(f'//div[@data-tag="{card_name}"]')
#         return card
#
#     @allure.step("Opening the cards page")
#     def open_cards_page(self):
#         logger.info("Opening the cards page")
#         self.app.wd.find_element(*CommonLocators.CARDS_TAB).click()
#
#     @allure.step('Click to the "Order new card" button')
#     def click_order_new_card_button(self):
#         logger.info('Click to the "Order new card" button')
#         self.app.wd.find_element(*CardsLocators.ORDER_NEW_CARD_BUTTON).click()
