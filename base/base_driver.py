from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def wait_until_page_contains_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_single_text(self, locator, text):
        Text = self.wait.until(EC.presence_of_element_located(locator)).text
        assert Text == text

    def verify_multiple_labels(self, dictionary):
        for key, value in dictionary.items():
            self.verify_single_text(key, value)

    def fill_single_data_in_textboxes(self, locator, text):
        self.wait_until_page_contains_element(locator).click()
        self.actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        self.wait_until_page_contains_element(locator).send_keys(text)

    def fill_multiple_data_in_textboxes(self, dictionary):
        for key, value in dictionary.items():
            self.fill_single_data_in_textboxes(key, value)

    def select_dropdown_option(self, dropdown_locator, do_text_locator, req_text):
        self.wait_until_page_contains_element(dropdown_locator).click()
        for i in range(1, 100):
            TEXT = self.wait_until_page_contains_element(do_text_locator).text
            if TEXT != req_text:
                self.actions.send_keys(Keys.ARROW_DOWN).perform()
            else:
                self.actions.send_keys(Keys.ENTER).perform()
                break