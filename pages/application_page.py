import logging
import os

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.logging import setup

logger = logging.getLogger()


class Application:
    def __init__(self, base_url, headless, allure_dir):
        setup("INFO")
        logger.setLevel("INFO")
        driver_path = ChromeDriverManager().install()
        options = Options()
        options.headless = headless
        self.create_dir_for_report(allure_dir)
        self.wd = webdriver.Chrome(driver_path, options=options)
        self.base_url = base_url

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        logger.info("Open main page")
        self.wd.get(self.base_url)

    def quit_app(self):
        logger.info("Quit app")
        self.wd.quit()

    @staticmethod
    def create_dir_for_report(dir_name):
        if not os.path.exists(dir_name):
            logger.info(f"Create dir {dir_name}")
            os.makedirs(dir_name)
