from faker import Faker
from framework.UIbase import UIBase
from selenium.webdriver.common.by import By

class Registration(UIBase):
    
    #---- Registration Home Page Locators ----#
    firstname_txt = (By.ID, "first_name")
    lastname_txt = (By.ID, "last_name")
    username_txt = (By.ID, "username")
    email_txt = (By.ID, "email")
    pwd_txt = (By.ID, "pwd")
    con_pwd_txt = (By.ID, "confirm_pwd")
    register_btn = (By.ID, "register")
    h1_tag = (By.XPATH, "/html/body/div[1]/h1")
    register_alert = (By.XPATH, "/html/body/div[1]")


    def __init__(self, driver):
        self.driver = driver
    
    def load_registration(self, url):
        """
        Loading registration page

        :Args:
         - url - registration page url
        """
        self.driver.get(url)

    def check_registration_h1(self):
        """
        Validating login page h1 text
        """
        return self.assert_element_text(self.h1_tag, " User Registration ")

    def check_registration(self):
        """
        Validaing user registration

        :Data:
         - Datas created using faker package
        """
        fake = Faker()
        self.enter_text(self.firstname_txt,fake.first_name())
        self.enter_text(self.lastname_txt,fake.last_name())
        self.enter_text(self.username_txt,fake.first_name())
        self.enter_text(self.email_txt,fake.email())
        self.enter_text(self.pwd_txt,"123456")
        self.enter_text(self.con_pwd_txt,"123456")
        self.click(self.register_btn)
        return self.assert_element_text(self.register_alert, "Registration successful! Please login. ")