import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from pathlib import Path
import invoice as inv

@pytest.fixture
def tmp_stock_file(tmp_path: Path):
    p = tmp_path / "stock.txt"
    p.write_text("pencil,0.15,85\nfolder,1.4,40\n")
    return p

@pytest.fixture
def stock(tmp_stock_file):
    return inv.loadStock(str(tmp_stock_file))

@pytest.fixture
def tmp_orders_file(tmp_path: Path):
    p = tmp_path / "orders.txt"
    p.write_text("pencil,15,EUR,0.15,2.25,0.0,0.49,2.75\n")
    return p
    
@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
