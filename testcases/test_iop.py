import pytest
from selenium import webdriver

@pytest.mark.run_this
def test_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

@pytest.mark.run_this
def test_yahoo():
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.com")
    assert "Yahoo" in driver.title
    driver.quit()

def test_bing():
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")
    assert "Bing" in driver.title
    driver.quit()

def test_duckduckgo():
    driver = webdriver.Chrome()
    driver.get("https://www.duckduckgo.com")
    assert "DuckDuckGo" in driver.title
    driver.quit()
