import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from locators.cards_locators import CardsLocators
from locators.header_locators import HeaderLocators

logger = logging.getLogger()


class CardsPage:
    def __init__(self, app):
        self.app = app

    def card_element(self, card_name):
        cards_block = self.app.wd.find_element(*CardsLocators.CARDS_BLOCK)
        card = cards_block.find_element_by_xpath(f'//div[@data-tag="{card_name}"]')
        return card

    @allure.step("Opening the cards page")
    def open_cards_page(self):
        logger.info("Opening the cards page")
        self.app.wd.find_element(*HeaderLocators.CARDS_TAB).click()

    @allure.step('Click to the "Order new card" button')
    def click_order_new_card_button(self):
        logger.info('Click to the "Order new card" button')
        self.app.wd.find_element(*CardsLocators.ORDER_NEW_CARD_BUTTON).click()

    @allure.step('Switch of the "Connect credit limit" button')
    def click_credit_limit_radiobutton(self, card_name, credit_limit):
        if not credit_limit:
            logger.info('Switch of the "Connect credit limit" button')
            self.card_element(card_name).find_element(
                *CardsLocators.RELATIVE_CREDIT_LIMIT_RADIOBUTTON
            ).click()

    @allure.step('Click to the "Order" button under the card block')
    def click_order_button(self):
        logger.info('Click to the "Order" button under the card block')
        self.app.wd.find_element(*CardsLocators.ORDER_BUTTON).click()

    @allure.step("Pick the division of bank")
    def pick_division_of_bank(self, division):
        logger.info("Pick the division of bank")
        self.app.wd.find_element(*CardsLocators.DIVISION_OF_BANK).send_keys(division)

    @allure.step("Submit application")
    def submit_application(self):
        logger.info("Submit application")
        self.app.wd.find_element(*CardsLocators.SUBMIT_APPLICATION).click()

    @allure.step("Confirm the sms code")
    def confirm_sms_code(self):
        logger.info("Confirm the sms code")
        iframe = self.app.wd.find_element(By.ID, "confirmation-frame")
        self.app.wd.switch_to.frame(iframe)
        sleep(1)
        self.app.wd.find_element(*CardsLocators.CONFIRM_SMS_BUTTON).click()

    @allure.step("Check is order card successful")
    def successful_message(self):
        logger.info("Check is order card successful")
        return self.app.wd.find_element(*CardsLocators.SUCCESSFUL_MESSAGE).text

    @allure.step('Click to the "Add other bank card" button')
    def click_add_other_bank_button(self):
        logger.info('Click to the "Add other bank card" button')
        self.app.wd.find_element(*CardsLocators.ADD_OTHER_BANK_CARD_BUTTON).click()

    @allure.step("Fill other bank card fields")
    def fill_other_bank_card_fields(self, card_number, card_month, card_year, cvv):
        logger.info("Fill other bank card fields")
        self.app.wd.find_element(*CardsLocators.CARD_NUMBER).send_keys(card_number)
        self.app.wd.find_element(*CardsLocators.CARD_MONTH).send_keys(card_month)
        self.app.wd.find_element(*CardsLocators.CARD_YEAR).send_keys(card_year)
        self.app.wd.find_element(*CardsLocators.CARD_CVV).send_keys(cvv)

    @allure.step("Submit adding other bank card")
    def submit_adding_other_bank_card(self):
        logger.info("Submit adding other bank card")
        self.app.wd.find_element(*CardsLocators.SAVE_OTHER_BANK_CARD_BUTTON).click()

    # def add_other_bank_card(self, card_data):
    #     pass
    #
    # def is_adding_other_bank_card_successful(self):
    #     pass
    #
    # def block_card(self):
    #     pass
    #
    # def is_card_blocked(self):
    #     pass
    #
    #
    #
    # # =============================
    # def sign_in_page_button(self):
    #     return self.app.wd.find_element(*RegistrationLocators.SIGN_IN_BUTTON)
    #
    # def email_for_create_input(self):
    #     return self.app.wd.find_element(*RegistrationLocators.EMAIL)
    #
    # @allure.step("Нажатие кнопки sign in на главной странице")
    # @allure.step("Ввод email")
    # @allure.step("Нажатие кнопки create an account")
    # def start_registration_process(self, user_data: RegistrationUserData):
    #     self.sign_in_page_button().click()
    #     self.email_for_create_input().send_keys(user_data.email)
    #     self.submit_create_button().click()
    #
    # @allure.step("Заполнение обязательных полей для регистрации")
    # def fill_requireds(self, user_data):
    #     fill_input(self.first_name_input, user_data.first_name)
    #     fill_input(self.last_name_input, user_data.last_name)
    #     fill_input(self.password_input, user_data.password)
    #     fill_input(self.address_input, user_data.address)
    #     fill_input(self.city_input, user_data.city)
    #     fill_select(self.state_list, user_data.state)
    #     fill_input(self.postal_code_input, user_data.postal_code)
    #     fill_input(self.mobile_phone_input, user_data.mobile_phone)
    #     self.register_button_input().click()
    #
    # def check_my_account(self):
    #     if len(self.my_account()) == 0:
    #         return False
    #     return True
