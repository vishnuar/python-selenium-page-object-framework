import pytest
from pages.login.Login import Login

class TestLogin():

    def test_Login_load(self, driver, url):
        # Arrange
        # driver and class initialization
        login_page = Login(driver)
        
        # Act 
        # Loading login page
        login_page.load_login(url+"login")

        # Assert
        # Verify whether login page loaded or not
        assert login_page.check_login_h1()
    
    def test_valid_login(self, driver, url):
        # Arrange
        # driver and class initialization
        login_page = Login(driver)
        
        # Act 
        # Loading login page
        login_page.load_login(url+"login")

        # Assert
        # Validating valid login usecase
        assert login_page.enter_valid_credentails("Sachin", "123456")

    def test_invalid_login(self, driver, url):
        # Arrange
        # driver and class initialization
        login_page = Login(driver)
        
        # Act 
        # Loading login page
        login_page.load_login(url+"login")

        # Assert
        # Validating invalid login usecase
        assert login_page.enter_invalid_credentails("Sachin", "1234567")