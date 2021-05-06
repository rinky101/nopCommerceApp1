
class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//*[@class='button-1 login-button']"
        #"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
        #"//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    # constructor of page class/ capture driver from test cases and pass the driver to the testcases
    # and driver pass tothe class variable(self.driver=driver)
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

