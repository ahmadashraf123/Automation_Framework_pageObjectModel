import pytest
from uuid import uuid4
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.Loginpage import Loginpage
from pageobjects.Addcustomerpage import Addcustomerpage
from utilities.customeLogger import LogGen
from utilities.readproperties import ReadConfig


class Test_003_Login:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("Test_003_add_customer")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("****** Login Successful *****")

        self.logger.info("****** Starting add customer Test *****")
        self.addcustomer = Addcustomerpage(self.driver)
        self.addcustomer.openCustomerMenuAndClickItem()
        self.addcustomer.clickonAddNewNew()

        self.logger.info("****** Providing AddCustomer details *****")
        random_email_id = random_email()
        self.addcustomer.setEmail(random_email_id)
        self.addcustomer.setPassword("test123")
        self.addcustomer.setFirstName("Ahmad")
        self.addcustomer.setLastName("Khan")
        self.addcustomer.selectgender("Male")
        self.addcustomer.setCompanyName("Viral Square")
        self.addcustomer.clickcheckbox()  # Tax Exempt
        self.addcustomer.selectnewsletter()
        self.addcustomer.setCustomerRoles("Guests")
        self.addcustomer.setManagerofVendor("Vendor 1")
        self.addcustomer.selectActivechekbox()
        self.addcustomer.selectMCPcheckbox()
        self.addcustomer.AdminContent("This is for testing purposes")
        self.addcustomer.clickonsave()

        try:
            toast_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissable']"))
            )
            self.toastmessage = toast_element.text
        except:
            self.toastmessage = ""

        self.logger.info(f"Toast message: {self.toastmessage}")

        assert "The new customer has been added successfully." in self.toastmessage, \
            f"Expected success message, but got: {self.toastmessage}"

        self.logger.info("Add customer test passed")
        self.driver.quit()


# Utility: Random Email Generator
def random_email(domain="gmail.com", prefix="user"):
    return f"{prefix}-{uuid4().hex[:10]}@{domain}"
