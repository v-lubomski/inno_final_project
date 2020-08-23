from selenium.webdriver.common.by import By


class CardsLocators:
    ORDER_NEW_CARD_BUTTON = (By.ID, "order-new-card-link")
    CARDS_BLOCK = (By.XPATH, '//div[@class="cards-group-selection-content span9"]')
    RELATIVE_CREDIT_LIMIT_RADIOBUTTON = (
        By.XPATH,
        '//label[@class="credit-card-toggle span7"]',
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[@class='btn btn-primary span5 btn-huge start-order-btn']",
    )
    DIVISION_OF_BANK = (By.XPATH, '//select[@id="card-branch"]')
    SUBMIT_APPLICATION = (By.XPATH, '//button[@id="forward"]')
    CONFIRM_SMS_BUTTON = (By.XPATH, '//button[@id="confirm"]')
    SUCCESSFUL_MESSAGE = (By.CLASS_NAME, "alert-success")
    ADD_OTHER_BANK_CARD_BUTTON = (By.ID, "other-bank-card-bind")
    CARD_NUMBER = (By.XPATH, '//input[@name="card.number"]')
    CARD_MONTH = (By.XPATH, '//input[@name="card.validityMonth"]')
    CARD_YEAR = (By.XPATH, '//input[@name="card.validityYear"]')
    CARD_CVV = (By.XPATH, '//input[@name="card.cvv"]')
    SAVE_OTHER_BANK_CARD_BUTTON = (By.ID, "bind-card")
    BANK_ACCOUNT_FOR_VIRTUAL_CARD = (By.XPATH, '//select[@name="accountId"]')
    VIRTUAL_CARD_LIMIT = (By.XPATH, '//input[@name="cardOrder.limit"]')
    VIRTUAL_CARD_HOLDER_NAME = (By.XPATH, '//input[@name="cardOrder.holderName"]')
    VIRTUAL_CARD_DURATION = (By.XPATH, '//select[@cardOrder.validityDurationMonths"]')
    CREATE_VIRTUAL_CARD_BUTTON = (By.ID, "submit-button")
    VIRTUAL_CARD_CHECKBOX = (By.XPATH, '//input[@name="condition.virtualConditions"]')
    VIRTUAL_CARD_CREATED_MESSAGE = (By.XPATH, "//div/h1")
