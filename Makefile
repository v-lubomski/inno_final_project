lint:
	@flake8 --max-line-length=120 tests models locators pages common

pytest:
	@pytest -s -v