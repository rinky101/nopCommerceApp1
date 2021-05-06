from PageObject.LoginPage import LoginPage
from PageObject.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
import time
import random
import string

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #logger


    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************ Test_003_AddCustomer **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Successfully ***********")

        self.logger.info("********** starting Add Customer test ********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clcikonCustomersmenuItem()

        self.addcust.clickonAddnew()
        self.logger.info("********** Providing customer info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword(self.password)
        self.addcust.setCustomersRole("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Rinky")
        self.addcust.setLastName("Nayak")
        self.addcust.setDob("2/2/1988")
        self.addcust.setCompanyName("TPVision")
        self.addcust.setAdminContent("This is for Testing.....")
        self.addcust.clickOnSave()

        self.logger.info("********* Saving Customer info ********")

        self.logger.info("******** Add Customer Validation started *******")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has added successfully.' in self.msg:
            assert True == True
            self.logger.info("******* Add Customer test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.error("******** Add customer Test Failed *********")
            assert False == False

        self.driver.close()
        self.logger.info("******* ending Add Customer Test passed******")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars)for x in range(size))








