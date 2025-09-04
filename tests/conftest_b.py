import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
