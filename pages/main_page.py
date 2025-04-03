from pages.base_page import BasePage
from locators.locators import LanguageLocators, InfoCompanyLocators, PayBtnLocators
from config.config import Urls


class InfoCompany(BasePage):
    def open(self):
        self.browser.get(Urls.BASE_URL)
    
    def open_info(self):
        self.click_element(InfoCompanyLocators.ABOUT_US_BTN)

    def check_btns_visible(self, btns):
        return [self.is_element_visible(btn) for btn in btns]

    def check_btns_clickable(self, btns):
        return [self.is_element_clickable(btn) for btn in btns]

class PayBtn(BasePage):
    def open(self):
        self.browser.get(Urls.BASE_URL)
    
    def open_info(self):
        self.click_element(PayBtnLocators.PAY_BTN)

class LanguageSwitch(BasePage):
    def open(self):
        self.browser.get(Urls.BASE_URL)
    
    def open_language_menu(self):
        self.click_element(LanguageLocators.LANGUAGE_BUTTON)
    
    def choose_language(self, language):
        if language == 'uz':
            self.click_element(LanguageLocators.LANGUAGE_UZ)
        elif language == 'ru':
            self.click_element(LanguageLocators.LANGUAGE_RU)
        elif language == 'en':
            self.click_element(LanguageLocators.LANGUAGE_ENG)
        else:
            raise ValueError(f"Not supported language: {language}")
    
    def get_header_text(self):
        return self.get_element_text(LanguageLocators.HEADER_TEXT)
