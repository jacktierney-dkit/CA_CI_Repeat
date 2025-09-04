import pytest
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"

def test_home_page_heading(driver):
    driver.get(BASE_URL + "/get_orders")
    assert "Orders" in driver.title
