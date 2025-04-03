from pages.main_page import PayBtn
from locators.locators import PayBtnLocators

def test_pay_btn_visible(browser):
    page = PayBtn(browser)
    page.open()
    page.open_info()

    assert page.is_element_visible(PayBtnLocators.PAY_BTN), \
        "[❌FAILED] Pay button isn't visible"
    
def test_pay_btn_clickable(browser):
    page = PayBtn(browser)
    page.open()
    page.open_info()

    assert page.is_element_clickable(PayBtnLocators.PAY_BTN),\
        "[❌ FAILED] Pay button isn't clickable"
def test_pay_btn_url(browser):
    page = PayBtn(browser)
    page.open()
    page.open_info()

    page.wait_for_url_contains("payment")

    assert "payment" in browser.current_url,\
        "[❌ FAILED] 'payment' page didn't load"

