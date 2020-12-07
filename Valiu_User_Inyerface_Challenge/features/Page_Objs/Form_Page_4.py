import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Utilities import Common_Utilities

class Form_Page_4_of_4:

    driver = None
    # logo_element = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()

    def __init__(self):
        print("in Form_Page_4_of_4")

    'Get 4_of_4 element to check the current page'
    def get_4_of_4_element(self, driver):
        print("in get_4_of_4_element")
        element_4_of_4 = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "//div[contains(text(),'4 / 4')]",
                                          "4_of_4_element", "one")
        return element_4_of_4

    'Get all check box elements and check them'
    def get_all_checkbox_elements(self,driver):
        print("get_all_checkbox_elements")
        all_checkbox_elements= self.common_utility.\
                               find_web_element(driver,
                                                By.XPATH,
                                                "//div[@class='captcha-gallery__row captcha-gallery__row-check']/div/span",
                                                "all_checkbox_elements","multiple")
        return all_checkbox_elements

    def select_pictures(self,driver):
        print("select_pictures")
        all_checkbox_elements = self.get_all_checkbox_elements(driver)
        result = set()
        for checkbox_element in all_checkbox_elements:
            result.add(self.common_utility.
                       web_element_action(driver,
                                          checkbox_element,
                                          "click", "",
                                          "select_pictures"))
        return result

    'Get Validate Element and click it.'
    def get_validate_element(self,driver):
        print("get_validate_element")
        validate_element= self.common_utility.\
                          find_web_element(driver,
                                           By.XPATH,
                                           "//button[contains(text(),'Validate')]",
                                           "validate_button","one")
        return validate_element

    def click_validate(self,driver):
        print("click_validte")
        time.sleep(2)
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_validate_element(driver),
                                    "click", "",
                                    "validate_button")
        return result