from pages.base_page import BasePage
from locators.locators import LanguageLocators
from config.config import Urls

class MainPage(BasePage):
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
