from random import randint
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from .Utilities import Common_Utilities

class Form_Page_3_of_4:

    driver = None
    wait = WebDriverWait(driver, 100)
    common_utility = Common_Utilities()
    first_name_element= None
    surname_element = None
    street_element = None
    users_birth_year = None
    def __init__(self):
        print("in Form_Page_3_of_4")

    'Get 3_of_4 element to check the current page'
    def get_3_of_4_element(self, driver):
        print("in get_3_of_4_element")
        element_3_of_4 = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "//div[contains(text(),'3 / 4')]",
                                          "3_of_4_element", "one")
        return element_3_of_4


    'Get First Name textbox element, clear existing text and enter user\'s First Name'
    def get_first_name_element(self, driver):
        print("in get_first_name_element")
        self.first_name_element = self.common_utility.\
                                  find_web_element(driver,
                                                   By.XPATH,
                                                   "(//div[contains(text(),'First name')]/following-sibling::div)/input",
                                                   "first_name_element", "one")
        return self.first_name_element

    def clear_first_name_element(self, driver):
        print("In clear_first_name_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_first_name_element(driver),
                                    "clear_text", "",
                                    "first_name_element")
        print(result)
        return result

    def enter_first_name(self, driver):
        print("In enter_first_name ")
        self.clear_first_name_element(driver)
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.first_name_element,
                                    "send_keys", "Tom",
                                    "first_name_element")
        print(result)
        return result

    'Click \'Choose a title\' drop down and choose a title'
    def get_choose_title_element(self, driver):
        print("in get_choose_title_element")
        choose_title_element = self.common_utility.\
                               find_web_element(driver,
                                                By.XPATH,
                                                "//div[contains(text(),'Choose a title')]",
                                                "choose_title_element", "one")
        return choose_title_element

    def click_choose_title_element(self, driver):
        print("In click_choose_title_element")
        result = self.common_utility.\
                web_element_action(driver,
                                   self.get_choose_title_element(driver),
                                   "click", "",
                                   "choose_title_element")
        print(result)
        return result

    def get_specific_title_element(self, driver):
        print("In specific_title_element")
        self.specific_title_element = self.common_utility.\
                                      find_web_element(driver,
                                                       By.XPATH,
                                                       "//div[contains(text(), 'Mr')][1]",
                                                       "specific_title_element", "one")
        return self.specific_title_element


    def choose_title(self, driver):
        print("In choose_title ")

        result_choose_title= self.click_choose_title_element(driver)

        result_specific_title = self.common_utility.\
                                web_element_action(driver,
                                                   self.get_specific_title_element(driver),
                                                   "click", "",
                                                   "specific_title_element")
        print(result_choose_title, result_specific_title)
        return result_choose_title and result_specific_title


    'Get Surname textbox element, clear existing text and enter user\'s Surname'
    def get_surname_element(self, driver):
        print("in surname_element")
        self.surname_element = self.common_utility.\
                               find_web_element(driver,
                                                By.XPATH,
                                                "(//div[contains(text(),'Surname')]/following-sibling::div)/input",
                                                "surname_element", "one")
        return self.surname_element

    def clear_surname_element(self, driver):
        print("In clear_surname_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_surname_element(driver),
                                    "clear_text", "",
                                    "surname_element")
        print(result)
        return result

    def enter_surname(self, driver):
        print("In enter_surname ")

        result_clear_surname=self.clear_surname_element(driver)
        result_enter_surname = self.common_utility.\
                               web_element_action(driver,
                                                  self.surname_element,
                                                  "send_keys", "Jerry",
                                                  "surname_element")
        print(result_clear_surname,result_enter_surname)
        return result_clear_surname and result_enter_surname

    'Get Street textbox element, clear existing text and enter user\'s Street'
    def get_street_element(self, driver):
        print("in street_element")
        self.street_element = self.common_utility.\
                              find_web_element(driver,
                                               By.XPATH,
                                               "(//div[contains(text(),'Street')]/following-sibling::div)/input",
                                                "street_element", "one")
        return self.street_element

    def clear_street_element(self, driver):
        print("In clear_street_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_street_element(driver),
                                    "clear_text", "",
                                    "street_element")
        print(result)
        return result

    def enter_street(self, driver):
        print("In enter_street ")

        result_clear_street=self.clear_street_element(driver)
        result_enter_street = self.common_utility.\
                              web_element_action(driver,
                                                 self.street_element,
                                                 "send_keys", "Mickey",
                                                 "street_element")
        print(result_clear_street,result_enter_street)
        return result_clear_street and result_enter_street

    'Get Number element, click it up to the desired number'
    def get_number_element(self, driver):
        print("in get_number_element")
        number_element = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "(//div[@class='numeric-stepper'])[2]/div[2]/button[1]",
                                          "number_element", "one")
        return number_element

    def enter_number(self, driver):
        print("In click_number_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_number_element(driver),
                                    "click", "", "number_element")
        print(result)
        return result

    'Get Box element, click it up to the desired number'
    def get_box_element(self, driver):
        print("in get_box_element")
        box_element = self.common_utility.\
                      find_web_element(driver,
                                       By.XPATH,
                                       "(//div[@class='numeric-stepper'])[1]/div[2]/button[1]",
                                       "box_element", "one")
        return box_element

    def enter_box(self, driver):
        print("In box_number_element")
        box_element = self.get_box_element(driver)
        result = set()
        for click in range(10):
            result = self.common_utility.\
                     web_element_action(driver,
                                        box_element,
                                        "click", "", "box_element")
        print(result)
        return result

    'Get Zip textbox element, clear existing text and enter user\'s Zip'
    def get_zip_element(self, driver):
        print("in zip_element")
        self.zip_element = self.common_utility.\
                           find_web_element(driver,
                                            By.XPATH,
                                            "(//div[contains(text(),'Zip')]/following-sibling::div)/input",
                                            "zip_element", "one")
        return self.zip_element

    def clear_zip_element(self, driver):
        print("In clear_zip_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_zip_element(driver),
                                    "clear_text", "", "zip_element")
        print(result)
        return result

    def enter_zip(self, driver):
        print("In enter_zip ")

        result_clear_zip = self.clear_zip_element(driver)
        result_enter_zip = self.common_utility.\
                           web_element_action(driver,
                                              self.zip_element,
                                              "send_keys", "40001",
                                               "zip_element")
        print(result_clear_zip, result_enter_zip)
        return result_clear_zip and result_enter_zip

    'Get City textbox element, clear existing text and enter user\'s City'
    def get_city_element(self, driver):
        print("in city_element")
        self.city_element = self.common_utility.\
                            find_web_element(driver,
                                             By.XPATH,
                                             "(//div[contains(text(),'City')]/following-sibling::div)/input",
                                             "city_element", "one")
        return self.city_element

    def clear_city_element(self, driver):
        print("In clear_city_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_city_element(driver),
                                    "clear_text", "",
                                    "city_element")
        print(result)
        return result

    def enter_city(self, driver):
        print("In enter_city ")

        result_clear_city = self.clear_city_element(driver)
        result_enter_city = self.common_utility.\
                            web_element_action(driver,
                                               self.city_element,
                                               "send_keys", "Disney",
                                               "city_element")
        print(result_clear_city, result_enter_city)
        return result_clear_city and result_enter_city

    'Click \'Choose a country\' drop down and choose a Country'
    def get_choose_country_element(self, driver):
        print("in get_choose_country_element")
        choose_country_element = self.common_utility.\
                                 find_web_element(driver,
                                                  By.XPATH,
                                                  "//span[contains(text(),'Choose a country')]",
                                                  "choose_country_element", "one")
        return choose_country_element

    def click_choose_country_element(self, driver):
        print("In click_choose_country_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_choose_country_element(driver),
                                    "click", "","choose_country_element")
        print(result)
        return result

    def get_all_country_element(self, driver):
        print("In all_country_element")
        all_country_elements = self.common_utility.\
                               find_web_element(driver,
                                                By.XPATH,
                                                "//div[contains(text(),'Country')]/following-sibling::div/div/div[2]/div",
                                                "all_country_elements", "multiple")
        return all_country_elements

    def choose_country(self, driver):
        print("In choose_country ")
        result_country_element = self.click_choose_country_element(driver)
        all_country_elements = self.get_all_country_element(driver)
        option_no = randint(1, len(all_country_elements))
        print(option_no)
        result_specific_country = self.common_utility.\
                                  web_element_action(driver,
                                                     all_country_elements[option_no-1],
                                                     "click","","specific_country_element")
        print(result_country_element, result_specific_country)
        return result_country_element and result_specific_country

    'Choose Day for birthday'
    def get_day_element(self, driver):
        print("in get_day_element")
        day_element = self.common_utility.\
                      find_web_element(driver,
                                       By.XPATH,
                                       "//div[contains(text(),'Day')]",
                                       "day_element", "one")
        return day_element

    def click_day_element(self, driver):
        print("In click_day_element")
        result = self.common_utility.\
                web_element_action(driver,
                                   self.get_day_element(driver),
                                   "click", "", "day_element")
        print(result)
        return result

    def get_all_day_elements(self, driver):
        print("In all_day_elements")
        all_day_elements = self.common_utility.\
                           find_web_element(driver,
                                            By.XPATH,
                                            "((//div[contains(text(),'Day')])//parent::div)/following-sibling::div/div",
                                            "all_day_elements", "multiple")
        return all_day_elements

    def choose_specific_day(self, driver):
        print("In choose_specific_day ")

        'Click Day element'
        result_day_element = self.click_day_element(driver)

        'Get All Day elements'
        all_day_elements = self.get_all_day_elements(driver)
        option_no = randint(1, len(all_day_elements))
        print(option_no)

        'Select a random day element'
        result_specific_day = self.common_utility.\
                              web_element_action(driver,
                                                 all_day_elements[option_no-1],
                                                 "click","", "specific_day_element")
        print(result_day_element, result_specific_day)
        return result_day_element and result_specific_day

    'Choose Month for birthday'
    def get_month_element(self, driver):
        print("in get_month_element")

        month_element = self.common_utility.\
                        find_web_element(driver,
                                         By.XPATH,
                                         "//div[contains(text(),'Month')]",
                                         "month_element", "one")
        return month_element

    def click_month_element(self, driver):
        print("In click_month_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_month_element(driver),
                                    "click", "","month_element")
        print(result)
        return result

    def get_all_month_elements(self, driver):
        print("In all_month_elements")
        all_month_elements = self.common_utility.\
                             find_web_element(driver,
                                               By.XPATH,
                                               "((//div[contains(text(),'Month')])//parent::div)/following-sibling::div/div",
                                               "all_month_elements", "multiple")
        return all_month_elements

    def choose_specific_month(self, driver):
        print("In choose_specific_month ")

        'Click Month element'
        result_month_element = self.click_month_element(driver)

        'Get all month elements'
        all_month_elements = self.get_all_month_elements(driver)
        option_no = randint(1, len(all_month_elements)-2)
        print(option_no)

        'Select a random month element'
        result_specific_month = self.common_utility.\
                                web_element_action(driver,
                                                   all_month_elements[option_no-1],
                                                   "click","", "specific_month_element")
        print(result_month_element, result_specific_month)
        return result_month_element and result_specific_month

    'Choose year for birthday'
    def get_year_element(self, driver):
        print("in get_year_element")
        year_element = self.common_utility.\
                       find_web_element(driver,
                                        By.XPATH,
                                        "//div[contains(text(),'Year')]",
                                        "year_element", "one")
        return year_element

    def click_year_element(self, driver):
        print("In click_year_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_year_element(driver),
                                    "click", "","year_element")
        print(result)
        return result

    def get_all_year_elements(self, driver):
        print("In all_year_elements")
        all_year_elements = self.common_utility.\
                            find_web_element(driver,
                                             By.XPATH,
                                             "((//div[contains(text(),'Year')])//parent::div)/following-sibling::div/div",
                                             "all_year_elements", "multiple")
        return all_year_elements

    def choose_specific_year(self, driver):
        print("In choose_specific_year ")

        'Click Year element'
        result_year_element = self.click_year_element(driver)

        'Get all Year elements'
        all_year_elements = self.get_all_year_elements(driver)

        'Select a random year'
        #option_no = randint(1, len(all_year_elements))

        'Selecting a specific year as the age slider is not giving ' \
        'consistent results for a particular formula'
        option_no = 101
        print(option_no)
        print(all_year_elements[option_no - 1].text)
        self.users_birth_year=all_year_elements[option_no - 1].text

        result_specific_year = self.common_utility.\
                               web_element_action(driver,
                                                  all_year_elements[option_no-1],
                                                  "click","", "specific_year_element")
        print(result_year_element, result_specific_year)
        return result_year_element and result_specific_year

    'Enter Birthday by Selecting Day, Month, Year'
    def enter_DOB(self,driver):
        return self.choose_specific_day(driver) and\
               self.choose_specific_month(driver) and\
               self.choose_specific_year(driver)

    'Click Choose Gender drop down and choose a title'
    def get_gender_element(self, driver):
        print("in get_gender_element")
        gender_element = self.common_utility.\
                         find_web_element(driver,
                                          By.XPATH,
                                          "// div[contains(text(), 'Female')]",
                                          "gender_element", "one")
        return gender_element

    def select_gender(self, driver):
        print("In click_gender_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_gender_element(driver),
                                    "click", "","gender_element")
        print(result)
        return result

    'Click Next drop down and choose a title'
    def get_next_element(self, driver):
        print("in get_next_element")
        next_element = self.common_utility.\
                       find_web_element(driver,
                                        By.XPATH,
                                        "//button[contains(text(),'Next')]",
                                        "next_element", "one")
        return next_element

    def click_next(self, driver):
        print("In click_next_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_next_element(driver),
                                    "click", "", "next_element")
        print(result)
        return result

    def get_send_to_bottom(self,driver):
        print("in get_send_to_bottom_element")
        send_to_bottom_element = self.common_utility.\
                                 find_web_element(driver,
                                                  By.XPATH,
                                                  "//span[contains(text(),'to bottom')]",
                                                  "send_to_bottom", "one")
        return send_to_bottom_element

    def click_send_to_bottom_element(self,driver):
        print("In click_send_to_bottom_element")
        result = self.common_utility.\
                 web_element_action(driver,
                                    self.get_send_to_bottom(driver),
                                    "click", "", "send_to_bottom")
        print(result)
        return result

    'Get Age element and slide Age appropriate to Birthday'
    def get_age_element(self, driver):
        print("in get_age_element")
        age_element = self.common_utility.\
                      find_web_element(driver,
                                       By.XPATH,
                                       "//div[contains(text(),'Age')]//parent::div/following-sibling::div/div/div/div[2]",
                                       "age_element", "one")
        return age_element

    def slide_age(self, driver):

        print("In slide_age")
        print(int(date.today().year) , int(self.users_birth_year))

        'Get age by subtracting birth year from current year '
        age = int(date.today().year) - int(self.users_birth_year)
        print(age)

        'Slide the Age element to appropriate age'
        'Get age element'
        age_slider = self.get_age_element(driver)

        'Perfom drag n drop action to slide age'
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(age_slider, 42, 0).perform()

        return True
