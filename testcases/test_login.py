import pytest
from selenium import webdriver
from pageobjects.Loginpage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customeLogger import LogGen
import os

class Test_001_login:
    base_url = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.logger.info("Starting test_login")
        self.logger.info("******** Test_001_Login *********")
        self.logger.info("******** Verifying Home page Title *********")  # Fixed closing parenthesis

        driver = setup
        driver.get(self.base_url)
        actual_title = driver.title

        if actual_title == 'nopCommerce demo store. Login':
            self.logger.info("Home page title verified successfully.")
            assert True
        else:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "test_homepageTitle.png")
            driver.save_screenshot(screenshot_path)
            self.logger.error("Home page title verification failed.")
            driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******** Verifying login test case *********")
        driver = setup
        driver.get(self.base_url)

        lp = Loginpage(driver)
        lp.set_email(self.email)
        lp.set_password(self.password)
        lp.click_login()

        actual_title = driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("Login test passed.")
            assert True
        else:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "test_login.png")
            driver.save_screenshot(screenshot_path)
            self.logger.error("Login test failed.")
            assert False
