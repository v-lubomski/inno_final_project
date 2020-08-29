import logging
import os

import allure
import pytest

from pages.application_page import Application

logger = logging.getLogger()


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    allure_dir = request.config.getoption("--report-folder")
    headless = request.config.getoption("--headless")
    fixture = Application(base_url, headless, allure_dir)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.quit_app()


@pytest.fixture(scope="module")
def login(app):
    app.open_main_page()
    app.login.auth()
    yield app
    app.exit_button().click()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="launching browser without gui",
    ),
    parser.addoption(
        "--report-folder",
        action="store",
        default="allure_results",
        help="enter path to allure dir",
    ),


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("allure_results/failures") else "w"
        try:
            with open("allure_results/failures", mode):
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    logger.error("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.wd.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
