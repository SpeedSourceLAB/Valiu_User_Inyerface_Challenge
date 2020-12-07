import sys

from behave.model_core import Status
from behave import fixture, use_fixture
from Page_Objs.HomePage import HomePage
from Page_Objs.Form_Page_1 import Form_Page_1_of_4
from Page_Objs.Form_Page_2 import Form_Page_2_of_4
from Page_Objs.Form_Page_3 import Form_Page_3_of_4
from Page_Objs.Form_Page_4 import Form_Page_4_of_4
from Page_Objs.Final_Page import Final_Page
from Page_Objs.Utilities import Common_Utilities

@fixture
def browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    context.home_page = HomePage()
    context.form_page_1_of_4 = Form_Page_1_of_4()
    context.form_page_2_of_4 = Form_Page_2_of_4()
    context.form_page_3_of_4 = Form_Page_3_of_4()
    context.form_page_4_of_4 = Form_Page_4_of_4()
    context.final_page = Final_Page()
    context.utilities = Common_Utilities()
    context.driver = context.utilities.driver_creation("chrome")
    return context

def before_feature(context, feature):
    print("before_feature activated")
    use_fixture(browser_chrome,context)

def after_scenario(context, scenario):
     print(scenario.status)
     if scenario.status==Status.failed:
         print(scenario,"failed")
         sys.exit()


