from selenium.webdriver.common.by import By

class LanguageLocators:
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, ".icon-globe")
    LANGUAGE_CURRENT = (By.XPATH, "//a[@id='navbarDropdownLocalization']/span[2]/text()")
    LANGUAGE_RU = (By.CSS_SELECTOR, ".navbar-icon-lang-ru")
    LANGUAGE_ENG = (By.CSS_SELECTOR, ".navbar-icon-lang-en")
    LANGUAGE_UZ = (By.CSS_SELECTOR, ".navbar-icon-lang-uz")
    HEADER_TEXT = (By.XPATH, "//div[@id='home-content']//h1")