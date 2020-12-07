import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Utilities import Common_Utilities

class Form_Page_2_of_4:

    driver = None
    # logo_element = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()
    email_element= None
    password_element = None
    domain_element = None

    def __init__(self):
        print("in Form_Page_2_of_4")

    'Get 2_of_4 element to check the current page'
    def get_2_of_4_element(self, driver):
        print("in get_2_of_4_element")
        element_2_of_4 = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "//div[contains(text(),'2 / 4')]",
                                          "2_of_4_element",
                                          "one")
        return element_2_of_4

    'Get \'Upload link element\', click it, abd select picture'
    def get_upload_element(self,driver):
        print("in get_upload_element")
        upload_element = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "//a[contains(text(),'upload')]",
                                          "upload_element",
                                          "one")
        return upload_element

    def click_upload_element(self,driver):
        print("In click_upload_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_upload_element(driver),
                                    "click","","upload_element")
        print(result)
        return result

    def upload_picture(self,driver):
        print("In upload_picture")
        result_click_upload = self.click_upload_element(driver)
        time.sleep(2)
        result_upload_picture = self.common_utility.select_file_through_autoit()
        return result_upload_picture and result_click_upload


    'Get Unselect all element, and click it'
    def get_uselect_all_element(self, driver):
        print("in get_uselect_all_element")
        unselect_all_element = self.common_utility.\
                               find_web_element(driver,
                                                By.XPATH,
                                                "//span[contains(text(),'Unselect all')]//parent::div/span/label/span",
                                                "unselect_all_element", "one")
        return unselect_all_element

    def uncheck_unselect_all_element(self,driver):
        print("In uncheck_unselect_all_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_uselect_all_element(driver),
                                    "click", "", "unselect_all_element")
        print(result)
        return result

    def get_all_checkboxes(self,driver):
        print(" IN get_all_checkboxes")
        all_checkbox_elememts = self.common_utility.\
                                find_web_element(driver,
                                                 By.XPATH,
                                                 "//div[@class='avatar-and-interests__interests-list__item']",
                                                 "all_checkbox_elements", "multiple")
        return all_checkbox_elememts

    def select_3_valid_options(self,driver):
        print("In select_3_valid_options")
        total_check_boxes = 21
        selected_options = []
        result =[]
        while len(selected_options) < 3 :
            #breakpoint()
            xpath_of_option_text = "(//div[@class='avatar-and-interests__interests-list__item']/div/span[2])"
            xpath_of_option_element = "(//div[@class='avatar-and-interests__interests-list__item']/div/span/label/span)"
            option_no = randint(1, total_check_boxes-1)
            if option_no in selected_options:
                continue
            xpath_of_option_text = xpath_of_option_text+"["+str(option_no)+"]"
            xpath_of_option_element = xpath_of_option_element+"["+str(option_no)+"]"
            print(xpath_of_option_text)
            random_option_element_for_text= self.common_utility.\
                find_web_element(driver, By.XPATH, xpath_of_option_text,
                                "random_option_element", "one")

            if random_option_element_for_text.text == "Select all" or\
                    random_option_element_for_text.text == "Unselect all":
                continue
            random_option_element = self.common_utility.\
                                    find_web_element(driver,
                                                     By.XPATH,
                                                     xpath_of_option_element,
                                                     "random_option_element", "one")
            result.append(self.common_utility.
                          web_element_action(driver,
                                             random_option_element,
                                             "click", "",
                                             "random_option_element"))
            selected_options.append(option_no)
        print(result)
        for item in result:
            if item != True:
                return False

        return True

    'Get Next button to goto page 3 of 4'
    def get_next_element(self, driver):
        print("in get_next_element")
        next_element = self.common_utility.\
                       find_web_element(driver,
                                        By.XPATH,
                                        "//button[contains(text(),'Next')]",
                                        "next_element", "one")
        return next_element

    def click_next_element(self, driver):
        print("In click_next_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_next_element(driver),
                                    "click", "", "next_element")
        print(result)
        return result




