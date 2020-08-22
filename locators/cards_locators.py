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
