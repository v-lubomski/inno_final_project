from selenium.webdriver.common.by import By


class CommonLocators:
    EXIT = (By.XPATH, '//a[@id="logout-button"]')
    CARDS_TAB = (By.ID, "cards-overview-index")
    ACCOUNTS_TAB = (By.ID, "accounts-index")
    ACCOUNTING_TAB = (By.ID, "statements-statement")
    CONFIRM_SMS_BUTTON = (By.XPATH, '//button[@id="confirm"]')
    CONFIRMATION_IFRAME = (By.ID, "confirmation-frame")
