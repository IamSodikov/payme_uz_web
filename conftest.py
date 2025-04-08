import os  # <--- Qo'shildi
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Avtomatik ChromeDriver

@pytest.fixture(scope="class")
def browser(request):
    options = webdriver.ChromeOptions()
    # Headless rejimni tekshirish (default: true)
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Ekran o'lchami

    # ChromeDriver avtomatik o'rnatish
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()