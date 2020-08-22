import allure
import pytest


@pytest.mark.parametrize(
    "card_name, credit_limit, division",
    [("YARKO", False, "Центральный: 197374, г. Сланцы, пр. Космонавтов, д. 100A")],
)
@allure.title("Order card")
def test_order_new_card(login, card_name, credit_limit, division):
    """
        0. Log in user
        1. Open the cards page
        2. Click to the "Order new card" button
        3. Switch of the "Connect credit limit" button
        4. Click to the "Order" button (for "Яркая" card)
        5. Pick the division of bank
        6. Click the "Order" button
        7. Confirm the sms code
        8. Check the successful message

        Result: successful message on the page
    """
    login.cards.open_cards_page()
    login.cards.click_order_new_card_button()
    login.cards.click_credit_limit_radiobutton(card_name, credit_limit)
    login.cards.click_order_button()
    login.cards.pick_division_of_bank(division)
    login.cards.submit_application()
    login.cards.confirm_sms_code()
    assert login.cards.successful_message() == "Card was successfully ordered!"


@pytest.mark.parametrize(
    "card_number, card_month, card_year, cvv",
    [("1234567812345678", "12", "2024", "123")],
)
@allure.title("Add other bank card")
def test_add_other_bank_card(login, card_number, card_month, card_year, cvv):
    """
        1. Open the cards page
        2. Click to the "Add the other bank card" button
        3. Fill card's data and confirm form
        4. Confirm the sms code
        5. Check the successful message

        Result: successful message on the page
    """
    login.cards.open_cards_page()
    login.cards.click_add_other_bank_button()
    login.cards.fill_other_bank_card_fields(card_number, card_month, card_year, cvv)
    login.cards.submit_adding_other_bank_card()
    login.cards.confirm_sms_code()
    assert (
        login.cards.successful_message()
        == f"Card {card_number[0:4]} {card_number[4:6]}** "
        f"**** {card_number[-4:]} successfully added"
    )


#
# def test_create_virtual_card(login):
#     """
#         1. Open the cards page
#         2. Click to the "Order new card" button
#         3. Click to the "Order" button (for "Virtual" card)
#         4. Click the "Create virtual card" button
#         5. Mark agreement checkbox
#         6. Confirm the sms code
#         7. Check the successful message
#
#         Result: successful message on the page
#     """
#     app.cards.open_cards_page()
#     app.cards.order_card(cardname='virtual', division=division)
#     assert app.cards.is_order_successful()
#
#
# def test_blocking_card(login):
#     """
#         1. Open the cards page
#         2. Click the "block" button
#         3. Confirm the pop-up "block" button
#         4. Confirm the sms code
#         5. Check the successful message
#
#         Result: successful message on the page
#     """
#     app.cards.open_cards_page()
#     app.cards.block_card()
#     assert app.cards.is_card_blocked()
