from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Utilities import Common_Utilities

class Final_Page:

    driver = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()

    def __init__(self):
        print("in Final page")

    'Get \'You are Awesome\' text to check the current page'
    def get_awesome_element(self, driver):
        print("in get_awesome_element")
        element_4_of_4 = self.common_utility.find_web_element(driver,
                                                              By.XPATH,
                                                              "//h1[contains(text(),'You are awesome!')]","awesome_element", "one")
        return element_4_of_4
