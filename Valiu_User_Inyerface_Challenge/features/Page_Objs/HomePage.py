from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Utilities import Common_Utilities

class HomePage:

    driver = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()

    def __init__(self):
        print("in HomePage")

    'Get Logo Element'
    def get_logo_element(self, driver):
        print("in get_log_element")
        logo_element = self.common_utility.\
                       find_web_element(driver,
                                        By.CSS_SELECTOR,
                                        ".logo__icon",
                                        "get_logo_element",
                                        "one")
        return logo_element

    'Get NO Element and click it'
    def get_NO_element(self,driver):
        print("In get_NO_element")
        NO_element = self.common_utility.\
                     find_web_element(driver,
                                      By.CSS_SELECTOR,
                                      "#app > div > div > div:nth-child(4) > p > u",
                                      "get_NO_element","one")
        return NO_element

    def click_NO_element(self,driver):
        print("In click_NO_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_NO_element(driver),
                                    "click","","click_NO_element")
        print(result)
        return result

    'Get HERE Element and click it.'
    def get_HERE_element(self,driver):
        print("In get_HERE_element")
        HERE_element = self.common_utility.\
                       find_web_element(driver,
                                        By.XPATH,
                                        "//a[contains(text(),'HERE')]",
                                        "get_HERE_element","one")
        return HERE_element

    def click_HERE_element(self,driver):
        print("In click_HERE_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_HERE_element(driver),
                                    "click","","click_HERE_element")
        print(result)
        return result

