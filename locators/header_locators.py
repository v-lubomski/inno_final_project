from selenium.webdriver.common.by import By


class HeaderLocators:
    EXIT = (By.XPATH, '//a[@id="logout-button"]')
    CARDS_TAB = (By.ID, "cards-overview-index")
