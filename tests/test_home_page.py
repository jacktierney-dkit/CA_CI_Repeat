import pytest
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.usefixtures("driver")
def test_home_page_heading(driver):
    driver.get(BASE_URL + "/")
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert "Order" in heading or "Orders" in heading
