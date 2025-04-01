import pytest
from pages.home_page import MainPage

@pytest.mark.parametrize("language, expected_text", [
    ("uz", "Payme to’lov xizmati"),
    ("ru", "Платежный сервис Payme"),
    ("en", "Payme payment service")
])
def test_language_switch(browser, language, expected_text):
    page = MainPage(browser)
    page.open()
    page.open_language_menu()
    page.choose_language(language)

    actual_text = page.get_header_text()
    assert expected_text in actual_text, (
        f"[❌ FAILED] Til: {language} — Matn topilmadi!\n"
        f"Kutilgan: '{expected_text}'\nTopilgan: '{actual_text}'"
    )
