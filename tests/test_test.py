from pages.application_page import Application


def test_test(app: Application):
    app.open_main_page()
    assert 0 == 0
