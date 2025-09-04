import pytest
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.usefixtures("driver")
def test_show_stock_heading(driver):
    driver.get(BASE_URL + "/item_list")
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert "Stock" in heading or "Items" in heading
