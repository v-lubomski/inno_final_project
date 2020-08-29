from selenium.webdriver.common.by import By


class DepositLocators:
    OPEN_DEPOSIT = (By.ID, "btn-show-rates")
    OPEN_CONCRETE_DEPOSIT = (By.XPATH, '//a[contains(text(), "Place deposit")]')
    ACCOUNT_FOR_DEPOSIT = (By.XPATH, '//select[@name="fromAccountId"]')
    END_DATE = (By.ID, "endDate")
    AMOUNT = (By.ID, "amount")
    FORWARD_BUTTON = (By.ID, "submit-button")
    CHECKBOX = (By.CLASS_NAME, "checkbox")
    CONFIRM_BUTTON = (By.ID, "confirm")
    SUCCESSFUL_MESSAGE = (By.CLASS_NAME, "alert-success")
    SHOW_CLOSED_DEPOSITS = (By.XPATH, '//div[@id="show-closed-deposits"]/a')
    TITLE = (By.XPATH, "//h1")
    ONE_OF_DEPOSITS = (By.XPATH, "//td/a")
    EDIT_ALIAS_BUTTON = (By.XPATH, '//i[@title="Name"]')
    EDIT_INPUT = (By.XPATH, '//input[@class="input-medium"]')
    OK_BUTTON = (By.XPATH, '//button[@class="btn btn-primary no-loading"]')
    ALIAS = (By.XPATH, '(//a[@class="alias"])[1]')

    @staticmethod
    def concrete_currency(value):
        return By.XPATH, f'//input[@value="{value}"]'

    @staticmethod
    def deposit_time(time):
        return By.XPATH, f'//input[@value="{time}"]'
