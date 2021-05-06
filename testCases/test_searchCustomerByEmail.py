from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObject.SearchCustomerPage import SearchCustomer
from PageObject.AddcustomerPage import AddCustomer
import time
import pytest

class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********* SearchCustomerByEmail_004***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Successfuly*****")

        self.logger.info("******** Starting Add Customer **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clcikonCustomersmenuItem()

        self.logger.info("********Searching customer by Emailid******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********* TC _searchCustomerByemail_004 finished***")
        self.driver.close()


