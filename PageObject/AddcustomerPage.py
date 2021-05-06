from selenium.webdriver.support.ui import Select
import time

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_xpath = "//input[@id='FirstName']"
    #txtLastName_xpath = "//input[@id='LastName']"
    txtLastName_id= "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRole_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdminstrators_xpath = "//li[contains(text(),'Adminstrators)]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered)]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors']"
    drpmgrvendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    #constructor of class

    def __init__(self,driver):
        self.driver = driver #self.driver belong to class

    def clickonCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        
        
    def clcikonCustomersmenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setCustomersRole(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRole_xpath).click()
        time.sleep(3)

        if role == "Registered":
           self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdminstrators_xpath).click()

        elif role == "Guest":
            # here user can be Registered or Guest, only one can be
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

            time.sleep(3)
            self.driver.execute_script("argument[0].click;",self.listitem) # if click is not working any other element use driver.execute method

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrvendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
