import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    remote_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
