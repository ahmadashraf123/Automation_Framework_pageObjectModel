from selenium.webdriver.common.by import By


class SearchCustomer():
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastname)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        # Changed to By.XPATH to match the rows properly
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfCols(self):
        # Changed to By.XPATH to match the columns properly
        return len(self.driver.find_elements(By.XPATH, self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        # Flag to track if email is found
        flag = False

        # Loop through each row of the table (1 to number of rows)
        for r in range(1, self.getNoOfRows() + 1):
            # Find the table element (this is your XPath to locate the entire table)
            tables = self.driver.find_element(By.XPATH, self.table_xpath)

            # Find the email in the current row (2nd column in the table)
            emailId = tables.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text

            # Compare the email found in the row with the input email
            if emailId == email:
                # If a match is found, set flag to True and stop the loop
                flag = True
                break  # No need to check further rows once email is found

        # Return the flag (True if found, False if not)
        return flag

    def searchCustomerByName(self, Name):
        # Flag to track if name is found
        flag = False

        # Loop through each row of the table (1 to number of rows)
        for r in range(1, self.getNoOfRows() + 1):
            # Find the table element (this is your XPath to locate the entire table)
            tables = self.driver.find_element(By.XPATH, self.table_xpath)

            # Find the name in the current row (3rd column in the table)
            name = tables.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text

            # Compare the name found in the row with the input name
            if name == Name:
                # If a match is found, set flag to True and stop the loop
                flag = True
                break  # No need to check further rows once name is found

        # Return the flag (True if found, False if not)
        return flag
