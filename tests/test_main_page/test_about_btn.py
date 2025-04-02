import pytest
from pages.main_page import InfoCompany
from locators.locators import InfoCompanyLocators

def test_about_us_button_visible(browser):
    page = InfoCompany(browser)
    page.open()

    assert page.is_element_visible(InfoCompanyLocators.ABOUT_US_BTN),\
        "[❌ FAILED] About us button isn't visible"
    
def test_about_us_button_clickable(browser):
    page = InfoCompany(browser)
    page.open()

    assert page.is_element_clickable(InfoCompanyLocators.ABOUT_US_BTN),\
        "[❌ FAILED] About us button isn't clickable!"

def test_about_us_sub_button_visible(browser):
    page = InfoCompany(browser)
    page.open()
    page.open_info()

    btns = [
        InfoCompanyLocators.NEWS_BTN,
        InfoCompanyLocators.DOCUMENTS_BTN,
        InfoCompanyLocators.TENDERS_BTN
    ]

    results = page.check_btns_visible(btns)
    for i, result in enumerate(results):
        assert result, f"[❌ FAILED] Button not found: {btns[i]}"
    

def test_about_us_sub_button_clickable(browser):
    page = InfoCompany(browser)
    page.open()
    page.open_info()

    btns = [
        InfoCompanyLocators.NEWS_BTN,
        InfoCompanyLocators.DOCUMENTS_BTN,
        InfoCompanyLocators.TENDERS_BTN
    ]

    results = page.check_btns_clickable(btns)
    for i, result in enumerate(results):
        assert result, f"[❌ FAILED] Button isn't clickable: {btns[i]}"

@pytest.mark.parametrize("btn_locator, expected_url_part", [
    (InfoCompanyLocators.NEWS_BTN, "/home/news"),
    (InfoCompanyLocators.DOCUMENTS_BTN, "/home/documents"),
    (InfoCompanyLocators.TENDERS_BTN, "/home/tenders")
])
def test_about_us_sub_button_navigation(browser, btn_locator, expected_url_part):
    page = InfoCompany(browser)
    page.open()
    page.open_info()
    page.click_element(btn_locator)

    assert expected_url_part in browser.current_url, \
        f"[❌ FAILED] Navigation failed! Expected part: {expected_url_part}, Actual URL: {browser.current_url}"


    