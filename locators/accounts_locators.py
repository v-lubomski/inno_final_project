from selenium.webdriver.common.by import By


class AccountsLocators:
    OPEN_ACCOUNT_BUTTON = (By.XPATH, '//a[text()="New account"]')
    CURRENCY = (By.ID, "currencySelect")
    DIVISION_OF_BANK = (By.XPATH, '//select[@id="account-branch"]')
    AGREEMENT = (By.NAME, "condition.newAccountConditions")
    OPEN_ACCOUNT = (By.ID, "submit")
    CONFIRM_SMS = (By.ID, "confirm")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

    ACCOUNT_OPERATIONS = (
        By.XPATH,
        '//table[@id="accounts"]//button[@class="btn btn-mini dropdown-toggle"]',
    )
    CLOSE_ACCOUNT = (By.XPATH, '(//a[@class="close-account-link"])[last()]')
    ACCOUNT_FOR_TRANSFER = (By.ID, "beneficiaryId")
    FORWARD_BUTTON = (By.ID, "#forward")
    REQUISITES = (By.XPATH, '//a[text()="Details"]')
    REQUISITES_TITLE = (By.XPATH, '//h3[text()="Account details for payments"]')
    CLOSE_REQUISITES = (
        By.XPATH,
        '//div[@id="requisites-popup"]//button[@class="close"]',
    )
    # = (By., '')
    # = (By., '')
    # = (By., '')
    # = (By., '')
    # = (By., '')
    #
    #


#     CREATE_VIRTUAL_CARD_BUTTON = (By.ID, "submit-button")
#     VIRTUAL_CARD_CHECKBOX = (By.XPATH, '//input[@name="condition.virtualConditions"]')
