import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys



class Addcustomerpage:
    # add customer page
    lnk_customers_menu_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]/parent::a"
    lnk_customers_menu_item_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_AddNew_Xpath = "//a[normalize-space()='Add new']"
    txt_Email_Xpath = "//input[@id='Email']"
    txt_Password_Xpath = "//input[@id='Password']"
    txt_FirstName_Xpath = "//input[@id='FirstName']"
    txt_LastName_Xpath = "//input[@id='LastName']"
    Rd_GenderMale_id = "Gender_Male"
    Rd_GenderFemale_id = "Gender_Female"
    txt_CompanyName_Xpath = "(//input[@id='Company'])[1]"
    checkbox_tax_Xpath = "//input[@id='IsTaxExempt']"
    input_Newsletter_css_selector = "input.select2-search__field"
    options_Newsletter_Id = "select2-SelectedNewsletterSubscriptionStoreIds-result-0vy5-1"
    input_Customer_roles_Xpath = "//input[@class='select2-search__field']"
    list_Administrators_Xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-s1qb-1']"
    list_ForumModerators_Xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-22ib-2']"
    list_Registered_Xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-npld-3']"
    list_Guests_Xpath = "//li[contains(@class,'select2-results__option')][normalize-space()='Guests']"
    list_Vendors_Xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-gp3h-5']"
    dr_MOVendors_Xpath = "//option[normalize-space()='Vendor 2']"
    checkbox_Active_Xpath = "//input[@id='Active']"
    checkbox_CMC_password_Xpath = "//input[@id='MustChangePassword']"
    text_AdminComment_Xpath = "//textarea[@id='AdminComment']"
    btn_Save_Xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type, locator_value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )

    def openCustomerMenuAndClickItem(self):
        time.sleep(6)
        self.wait_for_element(By.XPATH, self.lnk_customers_menu_Xpath).click()
        time.sleep(2)
        self.wait_for_element(By.XPATH, self.lnk_customers_menu_item_Xpath).click()


    def clickonAddNewNew(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_AddNew_Xpath))
        ).click()

    def setEmail(self, email):
        self.wait_for_element(By.XPATH, self.txt_Email_Xpath).clear()
        self.wait_for_element(By.XPATH, self.txt_Email_Xpath).send_keys(email)

    def setPassword(self, password):
        self.wait_for_element(By.XPATH, self.txt_Password_Xpath).clear()
        self.wait_for_element(By.XPATH, self.txt_Password_Xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.wait_for_element(By.XPATH, self.txt_FirstName_Xpath).clear()
        self.wait_for_element(By.XPATH, self.txt_FirstName_Xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.wait_for_element(By.XPATH, self.txt_LastName_Xpath).clear()
        self.wait_for_element(By.XPATH, self.txt_LastName_Xpath).send_keys(lastName)

    def selectgender(self, gender):
        if gender == 'Male':
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.Rd_GenderMale_id))
            ).click()
        elif gender == 'Female':
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.Rd_GenderFemale_id))
            ).click()
        else:
            raise ValueError("Invalid gender. Must be 'Male' or 'Female'")

    def setCompanyName(self, companyName):
        self.wait_for_element(By.XPATH, self.txt_CompanyName_Xpath).clear()
        self.wait_for_element(By.XPATH, self.txt_CompanyName_Xpath).send_keys(companyName)

    def clickcheckbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_tax_Xpath))
        ).click()

    def selectnewsletter(self):
        wait = WebDriverWait(self.driver, 15)

        # 1) Open the Select2
        dropdown_box = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//label[normalize-space()='Newsletter']/following::span[@role='combobox'][1]"
        )))
        dropdown_box.click()

        # 2) Type in the search field (it appears only after opening)
        search = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "input.select2-search__field[role='searchbox']"
        )))
        search.clear()
        search.send_keys("nop")

        # 3A) — select by exact visible text
        result = wait.until(EC.visibility_of_element_located((
            By.XPATH,
            "//span[contains(@class,'select2-container--open')]"
            "//li[contains(@class,'select2-results__option')][normalize-space()='nopCommerce admin demo store']"
        )))
        result.click()

    def setCustomerRoles(self, role):
        # Click on the customer roles field
        self.driver.find_element(By.XPATH, self.input_Customer_roles_Xpath).click()
        time.sleep(2)


        if role == 'Guests':
            time.sleep(3)
            remove_button = self.driver.find_element(By.CLASS_NAME, "select2-selection__choice__remove")
            self.driver.execute_script("arguments[0].click();", remove_button)
            time.sleep(2)
            self.listitem = self.driver.find_element(By.XPATH, self.list_Guests_Xpath)

        elif role == 'Registered':
            # FIX: use XPATH, not ID
            self.listitem = self.driver.find_element(By.XPATH, self.list_Registered_Xpath)

        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.list_Administrators_Xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.list_Vendors_Xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_Guests_Xpath)
            time.sleep(2)

        # Final click (single place)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self, value):
        dropdown_el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.dr_MOVendors_Xpath))
        )
        dropdown = Select(dropdown_el)
        dropdown.select_by_visible_text(value)
        print(f"Selected Manager is: {value}")

    def selectActivechekbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_Active_Xpath))
        ).click()

    def selectMCPcheckbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_CMC_password_Xpath))
        ).click()

    def AdminContent(self, content):
        self.wait_for_element(By.XPATH, self.text_AdminComment_Xpath).clear()
        self.wait_for_element(By.XPATH, self.text_AdminComment_Xpath).send_keys(content)

    def clickonsave(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_Save_Xpath))
        ).click()
