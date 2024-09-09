from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from base.base_driver import BaseDriver


class ResourcePIM(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators of PIM
    TEXT_LOGIN = By.XPATH, "//h5[contains(text(), '')]"
    TEXT_USERNAME = By.XPATH, "//label[contains(text(), 'Username')]"
    TEXT_PASSWORD = By.XPATH, "//label[contains(text(), 'Password')]"
    TB_USERNAME = By.XPATH, "//input[@name = 'username']"
    TB_PASSWORD = By.XPATH, "//input[@name = 'password']"
    B_LOGIN = By.XPATH, "//button[@type='submit']"

    USER_PROFILE = By.XPATH, "//p[contains(@class, 'oxd-userdropdown-name')]"
    L_LOGOUT = By.XPATH, "//a[contains(text(), 'Logout')]"

    NAVBAR_MY_INFO = By.XPATH, "//a[contains(@href, 'viewMyDetails')]"
    H_PIM = By.XPATH, "(//h6) [1]"
    TEXT_PERSONAL = By.XPATH, "(//h6) [3]"
    L_EMPLOYEE_FULL_NAME = By.XPATH, "//label[contains(text(), 'Employee Full Name')]"
    TB_FIRST_NAME = By.XPATH, "//input[@name='firstName']"
    TB_MIDDLE_NAME = By.XPATH, "//input[@name='middleName']"
    TB_LAST_NAME = By.XPATH, "//input[@name='lastName']"
    L_EMPLOYEE_ID = By.XPATH, "//label[contains(text(), 'Employee Id')]"
    TB_EMP_ID = By.XPATH, "(//label[contains(text(), 'Employee Id')]//following::div//input) [1]"
    L_OTHER_ID = By.XPATH, "//label[contains(text(), 'Other Id')]"
    TB_OTHER_ID = By.XPATH, "(//label[contains(text(), 'Employee Id')]//following::div//input) [1]"
    L_DRIVER_LICENSE_NUMBER = By.XPATH, '''//label[contains(text(), "Driver's License Number")]'''
    TB_DRIVER_LIC_NO = By.XPATH, "(//label[contains(text(), 'Driver')]//following::div//input) [1]"
    L_LICENSE_EXPIRY_DATE = By.XPATH, "//label[contains(text(), 'License Expiry Date')]"
    TB_LICENCE_EXP_DATE = By.XPATH, "(//label[contains(text(), 'Expiry')]//following::div//input) [1]"
    L_NATIONALITY = By.XPATH, "//label[contains(text(), 'Nationality')]"
    D_NATIONALITY = By.XPATH, "(//label[contains(text(), 'Nationality')]//following::div[contains(@class, 'select-text')]) [1]"
    TEXT_NATOINALITY = By.XPATH, "(//label[contains(text(), 'Nationality')]//following::div[contains(@class, 'select-text')]) [2]"

    L_MARITAL_STATUS = By.XPATH, "//label[contains(text(), 'Marital Status')]"
    D_MARITAL_STATUS = By.XPATH, "(//label[contains(text(), 'Marital Status')]//following::div[contains(@class, 'text')]) [1]"
    TEXT_MARITAL_STATUS = By.XPATH, "(//label[contains(text(), 'Marital Status')]//following::div[contains(@class, 'text')]) [2]"

    L_DATE_OF_BIRTH = By.XPATH, "//label[contains(text(), 'Date of Birth')]"
    TB_DATE_OF_BIRTH = By.XPATH, "(//label[contains(text(), 'Birth')]//following::div//input) [1]"
    L_GENDER = By.XPATH, "//label[contains(text(), 'Gender')]"
    B_SAVE = By.XPATH, "(//button[@type='submit']) [1]"
    TOAST_CONTENT = By.XPATH, "//div[contains(@class, 'toast-content')]"

    def valid_login(self):
        self.wait_until_page_contains_element(self.TB_USERNAME).send_keys("Admin")
        self.wait_until_page_contains_element(self.TB_PASSWORD).send_keys("admin123")
        self.wait_until_page_contains_element(self.B_LOGIN).click()

    def dashboard_to_navbar(self):
        self.wait_until_page_contains_element(self.NAVBAR_MY_INFO).click()
        self.verify_single_text(self.H_PIM, 'PIM')

    def verifying_label_names(self):
        Label_dict = {
            self.H_PIM: "PIM",
            self.TEXT_PERSONAL: "Personal Details",
            self.L_EMPLOYEE_FULL_NAME: "Employee Full Name",
            self.L_EMPLOYEE_ID: "Employee Id",
            self.L_OTHER_ID: "Other Id",
            self.L_DRIVER_LICENSE_NUMBER: "Driver's License Number",
            self.L_LICENSE_EXPIRY_DATE: "License Expiry Date",
            self.L_NATIONALITY: "Nationality",
            self.L_MARITAL_STATUS: "Marital Status",
            self.L_DATE_OF_BIRTH: "Date of Birth",
            self.L_GENDER: "Gender",
            self.B_SAVE: "Save",
        }
        # Common Keyword for checking labels
        self.verify_multiple_labels(Label_dict)

    def fill_data_in_tb(self):
        # Inserting data in Text Boxes
        TB_Dict = {
            self.TB_FIRST_NAME: "Alpha",
            self.TB_MIDDLE_NAME: "Gamma",
            self.TB_LAST_NAME: "Beta",
            self.TB_EMP_ID: "OTH001",
            self.TB_LICENCE_EXP_DATE: "2026-15-10",
            self.TB_DATE_OF_BIRTH: "1990-21-10"
        }

        self.fill_multiple_data_in_textboxes(TB_Dict)
        self.select_dropdown_option(self.D_NATIONALITY, self.TEXT_NATOINALITY, "Greek")
        self.select_dropdown_option(self.D_MARITAL_STATUS, self.TEXT_MARITAL_STATUS, "Other")

    def save_func(self):
        self.wait_until_page_contains_element(self.B_SAVE).click()
        assert self.wait.until(EC.presence_of_element_located(self.TOAST_CONTENT))

    def logout(self):
        self.wait_until_page_contains_element(self.USER_PROFILE).click()
        self.wait_until_page_contains_element(self.L_LOGOUT).click()

