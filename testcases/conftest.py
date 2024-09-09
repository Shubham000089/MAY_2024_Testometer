# Setup and Teardown code:
# Mandatory to import
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys

# Optional to import
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup_and_teardown_class(request):
    # Setup code: Runs once before any test methods in the class
    # Driver Setup
    # driver_path = "C://Program Files//Python310//Scripts//chromedriver.exe"
    # service = Service(driver_path)
    # options = Options()
    # driver = webdriver.Chrome(service=service, options=options)
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser} is not supported")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Assign driver and self.wait to the request's class
    request.cls.driver = driver

    yield
    # Teardown code: Runs once after all test methods in the class
    driver.quit()  # Ensure the browser is closed properly


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser option: Chrome or firefox")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This is the hook to get the test report
    outcome = yield
    report = outcome.get_result()

    # We only want to take a screenshot when a test fails during the call phase
    if report.when == "call" and report.failed:
        # Check if the fixture `driver` is used in the test
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            if driver:
                try:
                    screenshot = driver.get_screenshot_as_png()
                    allure.attach(screenshot, name="Failure Screenshot", attachment_type=AttachmentType.PNG)
                    print("Screenshot captured and attached to Allure report.")
                except Exception as e:
                    print(f"Failed to capture screenshot: {e}")
