# Mandatory to import
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys

# Optional to import
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


##### Login Module

# Setup and Teardown code:
@pytest.fixture(scope="class")
def setup_and_teardown_class(request):
    # Setup code: Runs once before any test methods in the class
    # Driver Setup
    driver_path = "C://Program Files//Python310//Scripts//chromedriver.exe"
    service = Service(driver_path)
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)

    # Other setups
    # Explicit self.wait
    wait = WebDriverWait(driver, 10)

    # Keyboard
    actions = ActionChains(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Assign driver and self.wait to the request's class
    request.cls.driver = driver
    request.cls.wait = wait  # Assign self.wait to request class
    request.cls.actions = actions

    yield
    # Teardown code: Runs once after all test methods in the class
    driver.quit()  # Ensure the browser is closed properly


# Locators of Login Module Page
TEXT_LOGIN = (By.XPATH, "//h5[contains(text(), '')]")
TEXT_USERNAME = (By.XPATH, "//label[contains(text(), 'Username')]")
TEXT_PASSWORD = (By.XPATH, "//label[contains(text(), 'Password')]")
TB_USERNAME = (By.XPATH, "//input[@name = 'username']")
TB_PASSWORD = (By.XPATH, "//input[@name = 'password']")
B_LOGIN = (By.XPATH, "//button[@type='submit']")
L_FORGOT = (By.XPATH, "//p[contains(@class, 'forgot')]")
E_USERNAME = (By.XPATH, "(//input[@name = 'username']//..//following::span) [1]")
E_PASSWORD = (By.XPATH, "(//input[@name = 'password']//..//following::span) [1]")
A_INVALID_CRED = (By.XPATH, "//p[contains(@class, 'alert')]")
USER_PROFILE = (By.XPATH, "//p[contains(@class, 'oxd-userdropdown-name')]")
L_LOGOUT = (By.XPATH, "//a[contains(text(), 'Logout')]")


@pytest.mark.usefixtures("setup_and_teardown_class")
class TestLoginModule:
    def test_hrm_001_verify_login_ui(self):
        # TC: HRM-001 Verify Login UI
        text = self.wait.until(EC.presence_of_element_located(TEXT_LOGIN)).text
        assert text == 'Login'
        assert self.driver.title == 'OrangeHRM'

        text = self.wait.until(EC.presence_of_element_located(TEXT_USERNAME)).text
        assert text == 'Username'

        text = self.wait.until(EC.presence_of_element_located(TEXT_PASSWORD)).text
        assert text == 'Password'

        text = self.wait.until(EC.presence_of_element_located(TB_USERNAME)).get_attribute('placeholder')
        assert text == 'Username'

        text = self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).get_attribute('placeholder')
        assert text == 'Password'

        text = self.wait.until(EC.presence_of_element_located(B_LOGIN)).text
        assert text == 'Login'

        text = self.wait.until(EC.presence_of_element_located(L_FORGOT)).text
        assert text == 'Forgot your password?'

    def test_hrm_002_login_without_credentials(self):
        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(E_USERNAME)).text
        assert Text == 'Required'

        Text = self.wait.until(EC.presence_of_element_located(E_PASSWORD)).text
        assert Text == 'Required'

    def test_hrm_003_login_without_username(self):
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).send_keys("admin123")
        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(E_USERNAME)).text
        assert Text == 'Required'

    def test_hrm_004_login_without_password(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin")
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).click()

        self.actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        self.actions.send_keys(Keys.BACKSPACE).perform()

        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(E_PASSWORD)).text
        assert Text == 'Required'

    def test_hrm_005_login_using_invalid_credentials(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin561")
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).send_keys("admin456")

        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(A_INVALID_CRED)).text
        assert Text == 'Invalid credentials'

    def test_hrm_006_login_valid_username_invalid_password(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin")
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).send_keys("admin456")

        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(A_INVALID_CRED)).text
        assert Text == 'Invalid credentials'

    def test_hrm_007_login_invalid_username_valid_password(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin561")
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).send_keys("admin123")

        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

        Text = self.wait.until(EC.presence_of_element_located(A_INVALID_CRED)).text
        assert Text == 'Invalid credentials'

    def test_hrm_008_login_valid_credentials(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin")
        self.wait.until(EC.presence_of_element_located(TB_PASSWORD)).send_keys("admin123")

        self.wait.until(EC.presence_of_element_located(B_LOGIN)).click()

    def test_hrm_009_logout(self):
        self.wait.until(EC.presence_of_element_located(USER_PROFILE)).click()
        self.wait.until(EC.presence_of_element_located(L_LOGOUT)).click()


TEXT_RESET_PASSWORD = By.XPATH, "//h6"
TEXT_SUBHEADING = By.XPATH, "(//p) [1]"
B_RESET_PASSWORD = By.XPATH, "//button[contains(@class, 'reset')]"
TEXT_1 = By.XPATH, "(//p) [2]"
TEXT_2 = By.XPATH, "(//p) [4]"


@pytest.mark.usefixtures("setup_and_teardown_class")
class TestForgetPassword:
    def test_hrm_014_verify_reset_password_ui(self):
        self.wait.until(EC.presence_of_element_located(L_FORGOT)).click()

        Text = self.wait.until(EC.presence_of_element_located(TEXT_RESET_PASSWORD)).text
        assert Text == 'Reset Password'

        Text = self.wait.until(EC.presence_of_element_located(TEXT_SUBHEADING)).text
        assert Text == 'Please enter your username to identify your account to reset your password'

    def test_hrm_015_neg_functionality_reset_password_button(self):
        self.wait.until(EC.presence_of_element_located(B_RESET_PASSWORD)).click()
        Text = self.wait.until(EC.presence_of_element_located(E_USERNAME)).text
        assert Text == 'Required'

    def test_hrm_016_pos_functionality_reset_password_button(self):
        self.wait.until(EC.presence_of_element_located(TB_USERNAME)).send_keys("Admin")
        self.wait.until(EC.presence_of_element_located(B_RESET_PASSWORD)).click()

    def test_hrm_017_verify_post_reset_password_ui(self):
        Text = self.wait.until(EC.presence_of_element_located(TEXT_RESET_PASSWORD)).text
        assert Text == 'Reset Password link sent successfully'

        Text = self.wait.until(EC.presence_of_element_located(TEXT_1)).text
        assert Text == 'A reset password link has been sent to you via email.'

        Text = self.wait.until(EC.presence_of_element_located(TEXT_2)).text
        assert Text == 'You can follow that link and select a new password.'