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

    ACCOUNTING_ACCOUNT = (By.NAME, "accountId")
    ACCOUNTING_DATE_FROM = (By.NAME, "from")
    ACCOUNTING_DATE_TO = (By.NAME, "until")
    GET_ACCOUNTING = (By.ID, "query-button")
    ACCOUNTING_DATES_RESULT = (
        By.XPATH,
        '(//div[@class="statement-header clearfix"]/div)[last()]',
    )
    ACCOUNTING_ACCOUNT_RESULT = (By.XPATH, '//span[@class="print-hidden"]')
