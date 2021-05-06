import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginDetails.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.sanity
    def test_login_ddt(self,setup):
        self.logger.info("********* Test_002_DDT_Login *********")
        self.logger.info("********* verifying Login DDT test ********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:",self.rows)

        lst_status=[]#empty list Variable

        for r in range(2,self.rows+1):

            self.user= XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("********** Passed **********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("******** Failed *********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("****** Failed ********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******** Passed *********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test is pass")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test ia Fail")
            self.driver.close()
            assert False


