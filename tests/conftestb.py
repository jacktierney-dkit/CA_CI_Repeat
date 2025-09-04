import os, time, urllib.request, contextlib, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.environ.get("TEST_BASE_URL", "http://127.0.0.1:5000")

def _is_up(url: str, timeout=0.5) -> bool:
    try:
        with contextlib.closing(urllib.request.urlopen(url, timeout=timeout)) as r:
            return 200 <= r.getcode() < 500
    except Exception:
        return False
      
@pytest.fixture(scope="session")
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,1024")
    d = webdriver.Chrome(options=opts)
    yield d
    d.quit()

@pytest.fixture(scope="session", autouse=True)
def wait_for_server():
    for _ in range(120):
        if _is_up(BASE_URL):
            return
        time.sleep(0.5)
    pytest.fail(f"Server not responding at {BASE_URL}. Start your Flask app before running tests.")
