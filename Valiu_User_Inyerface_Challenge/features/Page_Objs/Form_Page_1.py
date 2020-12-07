import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .Utilities import Common_Utilities

class Form_Page_1_of_4:
    driver = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()
    email_element = None
    password_element = None
    domain_element = None

    def __init__(self):
        print("in Form_Page_1_of_4")

    'Get 1_of_4 element to check the current page'

    def get_1_of_4_element(self, driver):
        print("in get_1_of_4_element")
        element_1_of_4 = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//div[contains(text(),'1 / 4')]", "1_of_4_element",
                             "one")
        return element_1_of_4

    'Get \'Not really no element\', and click it'

    def get_not_really_no_element(self, driver):
        print("in get_not_really_no_element")
        not_really_no_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//button[contains(text(),'Not really, no')]",
                             "not_really_no_element", "one")
        return not_really_no_element

    def click_not_really_no_element(self, driver):
        print("In click_not_really_no_element")
        result = self.common_utility. \
            web_element_action(driver,self.get_not_really_no_element(driver),
                               "click", "", "not_really_no_element")
        print(result)
        return result

    'Get Password textbox element, clear existing text and enter user\'s Password'

    def get_password_element(self, driver):
        print("in get_password_element")
        self.password_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//input[@placeholder='Choose Password']", "password_element", "one")
        return self.password_element

    def clear_password_element(self, driver):
        print("In clear_password_element")
        result = self.common_utility. \
            web_element_action(driver,self.get_password_element(driver),
                               "clear_text", "", "password_element")
        print(result)
        return result

    def enter_password(self, driver):
        print("In enter_password")
        result = self.common_utility. \
            web_element_action(driver,self.password_element,
                               "send_keys",
                               "Whatpwd@7890!@#$",
                               "password_element")
        print(result)
        return result

    'Get Email textbox element, clear existing text and enter user\'s email'

    def get_email_element(self, driver):
        print("in get_email_element")
        self.email_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//input[@placeholder='Your email']",
                             "email_element", "one")
        return self.email_element

    def clear_email_element(self, driver):
        print("In clear_email_element")
        result = self.common_utility. \
            web_element_action(driver,self.get_email_element(driver),
                               "clear_text",
                               "",
                               "clear_email_element")
        print(result)
        return result

    def enter_email(self, driver):
        print("In enter_email")
        result = self.common_utility. \
            web_element_action(driver,self.email_element,
                               "send_keys",
                               "cheese.pasta",
                               "email_element")
        print(result)
        return result

    'Get Domain textbox element, clear existing text and enter user\'s domain'

    def get_domain_element(self, driver):
        print("in get_domain_element")
        self.domain_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//input[@placeholder='Domain']",
                             "domain_element", "one")
        return self.domain_element

    def clear_domain_element(self, driver):
        print("In clear_domain_element")
        result = self.common_utility. \
            web_element_action(driver,self.get_domain_element(driver),
                               "clear_text",
                               "",
                               "clear_domain_element")
        print(result)
        return result

    def enter_domain(self, driver):
        print("In enter_domain")
        result = self.common_utility. \
            web_element_action(driver,self.domain_element,
                               "send_keys",
                               "gmail",
                               "domain_element")
        print(result)
        return result

    'Get Other dropdown element and click it'

    def get_other_element(self, driver):
        other_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//div[contains(text(),'other')]",
                             "other_element", "one")
        return other_element

    'Get .com element from dropdown and click it to choose it'

    def get_com_element(self, driver):
        com_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//div[contains(text(),'.com')]",
                             "com_element", "one")
        return com_element

    def choose_other_field(self, driver):
        print("In choose_other_field")

        result_other = self.common_utility. \
            web_element_action(driver,self.get_other_element(driver),
                               "click",
                               "",
                               "other_element")
        result_com = self.common_utility. \
            web_element_action(driver,self.get_com_element(driver),
                               "click",
                               "",
                               "com_element")
        print(result_other and result_com)
        if result_com == result_other == True:
            return True
        else:
            return False

    'Get Checkbox element for \'I do not accept the Terms & Conditions and uncheck it\' '

    def get_uncheck_tc_element(self, driver):
        uncheck_tc_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//input[@id='accept-terms-conditions']/following-sibling::span",
                             "uncheck_tc_element",
                             "one")
        return uncheck_tc_element

    def click_to_uncheck_tc_field(self, driver):
        result = self.common_utility. \
            web_element_action(driver,self.get_uncheck_tc_element(driver),
                               "click",
                               "",
                               "uncheck_tc_element")
        print(result)
        return result

    'Get Terms and Conditions link element and click it'

    def get_tc_element(self, driver):
        tc_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//span[contains(text(),'Terms & Conditions')]",
                             "tc_element", "one")
        return tc_element

    def click_tc_link(self, driver):
        result = self.common_utility. \
            web_element_action(driver,self.get_tc_element(driver),
                               "click",
                               "",
                               "tc_element")
        print(result)
        return result

    def get_send_to_bottom(self,driver):
        print("in get_send_to_bottom_element")
        send_to_bottom_element = self.common_utility.find_web_element(driver, By.XPATH,
                                                            "//span[contains(text(),'to bottom')]",
                                                            "send_to_bottom", "one")
        return send_to_bottom_element

    def click_send_to_bottom_element(self,driver):
        print("In click_send_to_bottom_element")
        result = self.common_utility.web_element_action(driver,self.get_send_to_bottom(driver), "click", "",
                                                        "send_to_bottom")
        print(result)
        return result

    'Get scroller element'
    def get_scroller_element(self, driver):
        scroller_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//div[@class='terms-and-conditions__text-scrollbar__scroller']",
                             "scroller_element", "one")
        return scroller_element

    "Get Close element"
    def get_close_element(self, driver):
        close_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//span[contains(text(),'©lose')]",
                             "close_element", "one")
        return close_element


    'Scroll T & C and click Accept'
    def scroll_tc_box(self, driver):
        'Get Scroller element'
        scroller = self.get_scroller_element(driver)
        print(datetime.now())
        'Get Accept element'
        accept_element = self.get_accept_element(driver)
        'Scroll T & C'
        for i in range(188):
            print("Scrolling T & C, Please wait", i)
            actions = None
            actions = ActionChains(driver)

            'Drag and Drop Scroller element to offset provided'
            for j in range(3):
                actions.drag_and_drop_by_offset(scroller, 0, 100).perform()
            self.common_utility.close_alert(driver)

        'Click Send to bottom to close help box and wait till it closes'
        self.click_send_to_bottom_element(driver)
        time.sleep(12)

        'Click Accept Button'
        self.common_utility.close_alert(driver)
        result = self.common_utility. \
                  web_element_action(driver,accept_element,
                                       "click",
                                       "",
                                       "accept_element")

        return result


    'Get Next link element and click it'

    def get_next_element(self, driver):
        next_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//a[contains(text(),'Next')]",
                             "next_element", "one")
        return next_element

    def click_next_button(self, driver):
        result = self.common_utility. \
            web_element_action(driver,self.get_next_element(driver),
                               "click",
                               "",
                               "next_element")
        print(result)
        return result

    'Get Accept Button element and click it'
    def get_accept_element(self, driver):
        accept_element = self.common_utility. \
            find_web_element(driver,
                             By.XPATH,
                             "//button[contains(text(),'Accept')]",
                             "accept_element", "one")
        return accept_element

    def click_accept_button(self, driver):
        result = self.common_utility. \
            web_element_action(driver,self.get_accept_element(driver),
                               "click",
                               "",
                               "accept_element")
        print(result)
        return result
