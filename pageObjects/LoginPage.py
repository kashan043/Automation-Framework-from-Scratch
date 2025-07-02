from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID,"Password")
    button_login_xpath = (By.XPATH,"//button[text()='Log in']")
    link_logout_linktext = (By.LINK_TEXT,"Logout")

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(*self.textbox_username_id).clear()
        self.driver.find_element(*self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*self.textbox_password_id).clear()
        self.driver.find_element(*self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*self.link_logout_linktext).click()