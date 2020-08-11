import pytest

from pages.application_page import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    allure_dir = request.config.getoption("--report-folder")
    fixture = Application(base_url, allure_dir)
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
    # parser.addoption(
    #     "--username",
    #     action="store",
    #     default="fobiw39468@homedepinst.com",
    #     help="enter username",
    # ),
    # parser.addoption(
    #     "--password",
    #     action="store",
    #     default="Password11",
    #     help="enter password",
    # ),
    parser.addoption(
        "--report-folder",
        action="store",
        default="/tmp/allure_results",
        help="enter path to allure dir",
    ),
