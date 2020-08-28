import logging
from time import sleep

import allure

from common.common_locators import CommonLocators

logger = logging.getLogger()


@allure.step("Confirm the sms code")
def confirm_sms_code(app):
    logger.info("Confirm the sms code")
    if app.wd.find_elements(*CommonLocators.CONFIRMATION_IFRAME):
        iframe = app.wd.find_element(*CommonLocators.CONFIRMATION_IFRAME)
        app.wd.switch_to.frame(iframe)
    sleep(1)
    app.wd.find_element(*CommonLocators.CONFIRM_SMS_BUTTON).click()
