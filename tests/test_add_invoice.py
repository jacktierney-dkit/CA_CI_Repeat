import time, pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.usefixtures("driver")
def test_add_invoice_save_and_redirect(driver):
    driver.get(BASE_URL + "/enter_invoice")

    try:
        driver.find_element(By.ID, "save").click()
    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(0.5)
    assert "/showinvoice?order=" in driver.current_url

@pytest.mark.usefixtures("driver")
def test_add_invoice_close_function(driver):
    driver.get(BASE_URL + "/enter_invoice")

    try:
        driver.find_element(By.ID, "close").click()
    except NoSuchElementException:
        driver.find_element(By.LINK_TEXT, "Close").click()

    time.sleep(0.25)
    assert "/enter_invoice" not in driver.current_url
