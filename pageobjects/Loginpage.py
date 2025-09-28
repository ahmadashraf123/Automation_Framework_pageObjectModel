from selenium.webdriver.common.by import By

class Loginpage:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class ='button-1 login-button']"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_link_text).click()
