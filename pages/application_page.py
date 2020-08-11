import logging

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.logging import setup

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, headless):
        setup("INFO")
        logger.setLevel("INFO")
        driver_path = ChromeDriverManager().install()
        options: Options = Options()
        options.headless = headless
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        logger.info("Open main page")
        self.wd.get(self.base_url)

    def quit_app(self):
        logger.info("Quit app")
        self.wd.quit()
