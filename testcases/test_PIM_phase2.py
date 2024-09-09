# Mandatory to import
import pytest
from pages.page_PIM import ResourcePIM
from utilities.utils import UtilsClass
from utilities.readconfig import ReadConfigData
from utilities.XLutils import Excel
from utilities.customlogger import LoggerDemo


@pytest.mark.usefixtures('setup_and_teardown_class')
class TestMyInfoSection:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.RP = ResourcePIM(self.driver)
        self.UT = UtilsClass()
        self.UTC = ReadConfigData()
        self.EX = Excel()
        self.logger = LoggerDemo.sample_logger(self)

    @pytest.mark.sanity
    def test_hrm_010_verify_my_info_ui(self):
        self.logger.info("****This is 1st TC*****")
        # RP = ResourcePIM(self.driver)
        # UT = UtilsClass()
        # Sample File
        test = self.UT.sample()
        print(test)

        # Data from config file
        # UTC = ReadConfigData()
        config_test = self.UTC.get_config_data('Credentials', 'Username')
        print(config_test)

        # Data from excel file
        # EX = Excel()
        Excel_test = self.EX.read_data('Sheet1', 'G5')
        print(Excel_test)

        self.RP.valid_login()
        self.RP.dashboard_to_navbar()
        self.RP.verifying_label_names()

    @pytest.mark.regression
    def test_hrm_011_verify_form_can_accept_data(self):
        # RP = ResourcePIM(self.driver, self.wait, self.actions)
        self.RP.fill_data_in_tb()
    #
    def test_hrm_012_verify_functionality_of_save_button(self):
        # RP = ResourcePIM(self.driver, self.wait, self.actions)
        self.RP.save_func()
    #
    def test_hrm_013_verify_logout(self):
    #     RP = ResourcePIM(self.driver, self.wait, self.actions)
        self.RP.logout()
