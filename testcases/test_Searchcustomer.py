import pytest
from pageobjects.Loginpage import Loginpage
from pageobjects.Addcustomerpage import Addcustomerpage
from pageobjects.Searchcustomerpage import SearchCustomer
from utilities.readproperties import ReadConfig
from utilities.customeLogger import LogGen
import time

class Test_SearchCustomer_004:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("SearchCustomerByEmail")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Logging in
        self.lp = Loginpage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("****** Login Successful *****")

        # Starting the "Add Customer" functionality
        self.logger.info("****** Starting add customer Test *****")
        self.addcustomer = Addcustomerpage(self.driver)
        self.addcustomer.openCustomerMenuAndClickItem()

        # Searching for customer by email
        self.logger.info("****** Searching Customer By Email *****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("arthur_holmes@nopCommerce.com")
        searchcust.clickSearchButton()
        time.sleep(3)  # Ensure that the results have time to load

        # Calling the search function correctly
        status = searchcust.searchCustomerByEmail("arthur_holmes@nopCommerce.com")  # Correct method and argument
        assert status == True, "Customer not found!"  # Improved assertion message

        self.logger.info("****** Testcase Completed *****")
