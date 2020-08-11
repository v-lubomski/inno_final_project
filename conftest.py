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


@pytest.fixture
def login():
    pass


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),
    parser.addoption(
        "--report-folder",
        action="store",
        default="/tmp/allure_results",
        help="enter path to allure dir",
    ),
