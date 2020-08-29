import allure
import pytest


@pytest.mark.parametrize(
    "currency, time, account, due_date, amount",
    [("RUB", "367", "Зарплатный", "01.09.2022", 20000)],
)
@allure.title("Open the deposit")
def test_open_deposit(login, currency, time, account, due_date, amount):
    """
        1. Open the deposits page
        2. Click "Open the deposit" button
        3. Pick currency
        4. Pick time
        5. Click "Open the deposit" button
        6. Fill form
        7. Confirm form

        Result: successful message on the page
    """
    login.deposits.open_deposits_page()
    login.deposits.select_deposit(currency, time)
    login.deposits.fill_new_deposit_form(account, due_date, amount)
    login.deposits.confirm_deposit_opening()
    assert login.deposits.is_deposit_opened()


@allure.title("Show the closed deposits")
def test_show_closed_deposits(login):
    """
        1. Open the deposits page
        2. Click "Show closed deposits"

        Result: we are in the closed deposits page
    """
    login.deposits.open_deposits_page()
    login.deposits.show_closed_deposits()
    assert login.deposits.closed_deposits_title() == "Closed deposits"


@allure.title("Show deposits details")
def test_show_deposit_details(login):
    """
        1. Open the deposits page
        2. Click to the deposit alias

        Result: there is title "Details of deposit" on the page
    """
    login.deposits.open_deposits_page()
    login.deposits.click_to_the_deposit_alias()
    assert login.deposits.deposit_details_title() == "Deposit details"


@pytest.mark.parametrize("alias", ["Test2"])
@allure.title("Rename deposit")
def test_rename_deposit(login, alias):
    """
        1. Open the deposits page
        2. Click to the alias editor button
        3. Input the new alias
        4. Confirm

        Result: there is new alias of the deposit
    """
    login.deposits.open_deposits_page()
    login.deposits.edit_alias(alias)
    assert login.deposits.deposit_alias() == alias
