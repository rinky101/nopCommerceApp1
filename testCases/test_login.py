import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_homePageTitle(self,setup):

        self.logger.info("*************Test_001_Login**********")
        self.logger.info("*********Verifying Homepage Tittle*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home page Title is passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("******* Home Page Title is Failed ********")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********* Verifying Login Case *****")
        self.driver = setup
        self.driver.get(self.baseURL)

        #create object of LoginPage class
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)   #all variable are belonge to class, to access the class variable we are suing self
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****** Login test ia Passed ******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****** Login test ia Failed ******")
            assert False


