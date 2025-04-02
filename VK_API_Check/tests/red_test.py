import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get('http://127.0.0.1:8000/home/')
    assert driver.title == 'VK Check'

