import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.Loginpage import Loginpage
from utilities.readproperties import ReadConfig
from utilities.customeLogger import LogGen
from utilities import XLutilities


class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = "../testdata/LoginData.xlsx"
    logger = LogGen.loggen()
    exp_title = "Dashboard / nopCommerce administration"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******** Test_002_DDT_Login ********")
        driver = setup
        driver.get(self.base_url)
        lp = Loginpage(driver)

        rows = XLutilities.getRowCount(self.path, "Sheet1")
        self.logger.info(f"Rows found: {rows}")

        results = []  # collect "PASS"/"FAIL"

        for r in range(2, rows + 1):
            user = XLutilities.readData(self.path, "Sheet1", r, 1)
            password = XLutilities.readData(self.path, "Sheet1", r, 2)
            expected = str(XLutilities.readData(self.path, "Sheet1", r, 3)).strip().lower()

            self.logger.info(f"Row {r}: user={user}, expected={expected}")

            lp.set_email(user)
            lp.set_password(password)
            lp.click_login()

            # Wait briefly for title to stabilize (avoid hard sleeps)
            try:
                WebDriverWait(driver, 10).until(lambda d: d.title != "")
            except Exception:
                pass

            actual_title = driver.title

            if actual_title == self.exp_title:
                # Logged in scenario
                if expected == "pass":
                    self.logger.info("Login test: PASS")
                    results.append("PASS")
                else:
                    self.logger.info("Login test: FAIL (expected fail but succeeded)")
                    results.append("FAIL")
                # Logout only if logged in
                try:
                    lp.logout()
                    # Optionally wait for login page to reappear
                    WebDriverWait(driver, 5).until(lambda d: d.title != self.exp_title)
                except Exception:
                    self.logger.warning("Logout step not completed (continuing).")
            else:
                # Not logged in scenario
                if expected == "fail":
                    self.logger.info("Login test: PASS (failed as expected)")
                    results.append("PASS")
                else:
                    self.logger.info("Login test: FAIL (expected pass but failed)")
                    results.append("FAIL")

        # Final assertion after all rows
        if "FAIL" in results:
            self.logger.info(f"Login DDT test: FAILED. Results={results}")
            assert False, f"Some login rows failed. Results={results}"
        else:
            self.logger.info("Login DDT test: PASSED")
            assert True
