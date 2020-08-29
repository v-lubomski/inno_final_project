lint:
	@flake8 --max-line-length=120 tests locators pages common

pytest:
	@pytest -s -v

allure:
	@pytest --alluredir=allure_results -s -v

report:
	@allure serve allure_results