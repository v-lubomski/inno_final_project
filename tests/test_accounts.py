import allure
import pytest


@pytest.mark.parametrize(
    "currency, division, agreement",
    [
        (
            "Российский рубль",
            "Центральный: 197374, г. Сланцы, пр. Космонавтов, д. 100A",
            True,
        )
    ],
)
@allure.title("Open account")
def test_open_account(login, currency, division, agreement):
    """
        1. Open the accounts page
        2. Click the "Open account" button
        3. Pick a currency
        4. Pick a division of bank
        5. Mark checkbox, if that is necessary
        6. Click the "Open account" button
        7. Confirm the sms-code

        Result: successful message on the page
    """
    login.accounts.open_accounts_page()
    login.accounts.click_open_account_button()
    login.accounts.fill_form_for_new_account(currency, division, agreement)
    login.accounts.confirm_opening()
    assert login.accounts.is_account_opened()


@pytest.mark.parametrize("account_for_transfer", ["Зарплатный"])
@allure.title("Open account")
@allure.title("Close account")
def test_close_account(login, account_for_transfer):
    """
        1. Open the accounts page
        2. Click closing button for last account
        3. Pick account for transfer left money
        4. Click forward button
        5. Confirm sms-code

        Result: successful message on the page
    """
    login.accounts.open_accounts_page()
    login.accounts.click_close_account_button()
    login.accounts.pick_account_for_transfer(account_for_transfer)
    login.accounts.confirm_closing_account()
    assert login.accounts.is_account_closed()


@allure.title("View requisites of account")
def test_view_requisites(login):
    """
        1. Open the accounts page
        2. Click to the requisites button of one of account's

        Result: there is title "Requisites for cashless transfers" and
    """
    login.accounts.open_accounts_page()
    login.accounts.go_to_requisites()
    assert login.accounts.requisites_title() is True
    login.accounts.close_requisites()


# @allure.title("Show accounting")
# def test_show_accounting(login):
#     """
#         1. Open accounting page
#         2. Pick account for accounting
#
#         Results:
#         - Period = period dates in the filter
#         - Account = selected account
#     """
#     login.accounts.open_accounting_page()
#     login.accounts.pick_account_for_accounting()
#     selected_account = login.accounts.remember_selected_account()
#     selected_dates = login.accounts.remember_selected_dates()
#     assert login.accounts.shown_period_dates == selected_dates
#     assert login.accounts.shown_selected_account == selected_account
