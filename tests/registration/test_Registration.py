import pytest
from pages.registration.Registration import Registration

class TestRegistration():

    def test_registration_load(self, driver, url):
        # Arrange
        # driver and class initialization
        register_page = Registration(driver)
        
        # Act 
        # Loading regisration page
        register_page.load_registration(url+"register")

        # Assert
        # Verify whether regisration page loaded or not
        assert register_page.check_registration_h1()
    
    def test_user_registration(self, driver, url):
        # Arrange
        # driver and class initialization
        register_page = Registration(driver)
        
        # Act 
        # Loading regisration page
        register_page.load_registration(url+"register")

        # Assert
        # Validating user registration
        assert register_page.check_registration()