from framework.UIbase import UIBase
from selenium.webdriver.common.by import By

class Login(UIBase):
    
    #---- Login Page Locators ----#
    username_txt = (By.ID, "username")
    password_txt = (By.ID, "password")
    login_btn = (By.ID, "loginbtn")
    h1_tag = (By.XPATH, "/html/body/div[1]/h1")

    def __init__(self, driver):
        self.driver = driver
    
    def load_login(self, url):
        """
        Loading login page

        :Args:
         - url - login page url
        """
        self.driver.get(url)

    def check_login_h1(self):
        """
        Validating login page h1 text
        """

        return self.assert_element_text(self.h1_tag, " User Login ")


    def enter_valid_credentails(self, username, password):
        """
        validating valid login scenario

        :Args:
         - username - username
         - password - password
        """
        self.enter_text(self.username_txt,username)
        self.enter_text(self.password_txt,password)
        self.click(self.login_btn)
        url_now = self.driver.current_url
        if("noteapp" in url_now):
            return True
        else:
            return False

    def enter_invalid_credentails(self, username, password):
        """
        validating invalid login scenario

        :Args:
         - username - username
         - password - password
        """
        self.enter_text(self.username_txt,username)
        self.enter_text(self.password_txt,password)
        self.click(self.login_btn)
        url_now = self.driver.current_url
        if("noteapp" not in url_now):
            return True
        else:
            return True
