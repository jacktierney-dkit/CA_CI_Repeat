import pytest
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"

def test_show_stock_heading(driver):
    driver.get(BASE_URL + "/item_list")
    assert "Stock" in driver.title or "Items" in driver.title
