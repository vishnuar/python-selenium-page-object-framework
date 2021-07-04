# python-selenium-page-object-framework
This is automation framework in Python integrated with the Azure pipeline. The framework developed in page object model. Automates the login and registration scenarios of noteapp application [Github](https://github.com/vishnuar/python-flask-noteapp). Webdriver will get downloaded automatically with the help of webdriver manager  

## Prerequisites
Azure pipelines. Azure pipelines can be intergrated with [Github](https://github.com/marketplace/azure-pipelines).

## Run test locally
This suite is designed for linux enviorment
- Install pip libraries: 
    - `pip install pytest`
    - `pip install selenium`
    - `pip install Faker`
    -  `pip install webdriver-manager`
- To run the test, Navigate to the directory and enter the command `pytest -vv -ss --url <url to be validated>`

## Test Report
Test report will be printed in the running console, We can generate the report in various other formats like HTML, junit etc


## Authors
* **Vishnu A R**
