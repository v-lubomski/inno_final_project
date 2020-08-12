import pytest

from pages.application_page import Application


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
        default="/tmp/allure_results",
        help="enter path to allure dir",
    ),
