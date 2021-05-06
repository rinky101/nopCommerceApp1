from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObject.SearchCustomerPage import SearchCustomer
from PageObject.AddcustomerPage import AddCustomer
import time
import pytest

class Test_005_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("****SearchCustomerByName_005**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Page success ********")

        self.logger.info("********** starting AddCustomer********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clcikonCustomersmenuItem()

        self.logger.info("******* SearchCustomeByName********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)

        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("********* TC _searchCustomerByName_005 finished***")
        self.driver.close()
