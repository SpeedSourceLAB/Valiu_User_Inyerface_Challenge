import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException
from webdriver_manager.firefox import GeckoDriverManager
from autoit import *

class Common_Utilities:
    driver = None

    'Get the driver object - Selenium'
    def get_driver(self, browser):
        print("Trying to open browser in Common defs")
        if (browser == "chrome"):
            try:
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificates-errors')
                options.add_argument("--test-type")
                options.add_argument("start-maximized")
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
                time.sleep(3)
                print("Browser opened successfully")
                logging.info("Browser opened successfully")

            except Exception as e:
                logging.exception("Browser closed unexpectedly")
                logging.exception(e)
                print("Browser closed unexpectedly, hence the script stopped.")

        elif (browser == "gecko"):
            try:
                options = webdriver.FirefoxOptions()
                options.add_argument("-start-maximized")
                caps = DesiredCapabilities().FIREFOX
                caps["marionette"] = True
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options,
                                                capabilities=caps)
                self.driver.maximize_window()
                time.sleep(3)
                print("Browser opened successfully")
                logging.info("Browser opened successfully")
            except Exception as e:
                logging.exception("Browser closed unexpectedly")
                logging.exception(e)
                print("Browser closed unexpectedly, hence the script stopped.")

        return self.driver

    # Crete the driver -Selenium
    def driver_creation(self, browser):
        self.browser = browser
        self.driver = self.get_driver(browser)

        for i in range(5):
            while (self.driver == None):
                if (i < 5):
                    print("Opening Browser, Attempts:", i + 1, "/5 times")
                    self.driver = self.get_driver(browser)
                    time.sleep(10)
                    i += 1
                    if (self.driver != None):
                        break

        return self.driver


    def close_alert(self,driver):
        try:
            'Get Close Element'
            close_element = driver.find_element_by_xpath("//span[contains(text(),'©lose')]")

            'If Close Element found click to close alert box'
            if close_element:
                self. \
                    web_element_action(driver,close_element,
                                       "click",
                                       "",
                                       "close_element")
        except Exception as e:
            print(e)

    def get_send_to_bottom(self,driver):
        print("in get_send_to_bottom_element")
        send_to_bottom_element = self.find_web_element(driver, By.XPATH,
                                                            "//span[contains(text(),'to bottom')]",
                                                            "send_to_bottom", "one")
        return send_to_bottom_element

    def click_send_to_bottom_element(self,driver):
        print("In click_send_to_bottom_element")
        try:
            'Get send to bottom Element'
            send_to_bottom_element = driver.find_element_by_xpath("//span[contains(text(),'to bottom')]")

            'Click send_to_bottom if exists '
            if send_to_bottom_element:
                self.web_element_action(driver,send_to_bottom_element, "click", "",
                                                        "send_to_bottom")
                time.sleep(15)
        except Exception as e:
            print(e)


    'Find the Web element using Selenium'
    def find_web_element(self, driver, locator_type, locator, element_desc, element_count):
        wait = WebDriverWait(driver, 30)
        web_element = None
        while web_element is None:
            if element_count == "one":
                try:
                    print(locator)
                    web_element = wait.until(EC.presence_of_element_located((locator_type, locator)))
                    print(element_desc, "found")
                    logging.info(element_desc + " found")
                    return web_element
                except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                    self.close_alert(driver)
                    self.click_send_to_bottom_element(driver)
                    continue
                except Exception as e:
                    print(element_desc + " not found", e)
                    driver.get_screenshot_as_file("ScreenShots\\find_web_element.png")

            elif element_count == "multiple":
                try:
                    print(locator)
                    web_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
                    print(element_desc, "found and returned list of web elements")
                    return web_elements
                except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                    self.close_alert(driver)
                    self.click_send_to_bottom_element(driver)
                    continue
                except Exception as e:
                    print(element_desc, "not found", e)
                    driver.get_screenshot_as_file("ScreenShots\\find_web_element.png")

    'Perform action on web element using Selenium'
    def web_element_action(self,driver, web_element, action, send_keys_values, element_desc):
        result = False
        try:
            while not result :
                if action == "send_keys":
                    try:
                        web_element.send_keys(send_keys_values)
                        print(action, "to", element_desc)
                        logging.info(action + " to " + element_desc)
                        result =True
                        return result
                    except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                        self.close_alert(driver)
                        self.click_send_to_bottom_element(driver)
                        continue
                    except Exception as e:
                        print("Unexpected Exception raised when", action, "to", element_desc, e)
                        logging.exception("Unexpected Exception raised when", action, "to" + element_desc)
                        logging.exception(e)
                        result = False
                        return result
                elif action == "click":
                    try:
                        web_element.click()
                        print(element_desc, "clicked")
                        logging.info(element_desc + " clicked")
                        result = True
                        return result
                    except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                        print(e)
                        self.close_alert(driver)
                        self.click_send_to_bottom_element(driver)
                        continue
                    except Exception as e:
                        print("Unexpected error while clicking", element_desc, e)
                        logging.exception("Unexpected error while clicking " + element_desc)
                        logging.exception(e)
                        result = False
                        return result
                elif action == "get_text":
                    try:
                        print(element_desc, "get_text")
                        logging.info(element_desc + "get_text ")
                        print(web_element.get_attribute('text'))
                        result = True
                        return web_element.get_attribute('text')
                    except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                        self.close_alert(driver)
                        self.click_send_to_bottom_element(driver)
                        continue
                    except Exception as e:
                        print("Unexpected error while getting text ", element_desc, e)
                        logging.exception("Unexpected error while getting text" + element_desc)
                        logging.exception(e)
                        result = False
                        return result
                elif action == "clear_text":
                    try:
                        print(element_desc, "clear_text")
                        logging.info(element_desc + " clear_text")
                        web_element.clear()
                        result = True
                        return result
                    except (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException) as e:
                        self.close_alert(driver)
                        self.click_send_to_bottom_element(driver)
                        continue
                    except Exception as e:
                        print("Unexpected error while clearing text at ", element_desc, e)
                        logging.exception("Unexpected error while clearing text" + element_desc)
                        logging.exception(e)
                        result = False
                        return result
        except Exception as e:
            print("Unexpected exception occurred in def web_element_action", e)
            driver.get_screenshot_as_file("ScreenShots\web_element_action.png")
            logging.error("Unexpected exception occurred in web_element_action")
            logging.exception(e)

    def select_file_through_autoit(self):
        try:
            print("In select_picture_through_autoit")
            time.sleep(2)

            'Autoit tool identifies the Open window and selects a picture to upload '
            control_focus("Open", "Edit1")

            'Change the path according to your file system'
            control_set_text("Open", "Edit1", "C:\\Users\\prade\\Downloads\\cute_dog.jpeg")

            'Click Open button'
            control_click("Open", "Button1")

            return True
        except Exception as e:
            print("Unexpected exception occurred in def select_picture_through_autoit", e)

