import time
from behave import *


@given(u'The User Inyerface URL "{url}" is entered in browser')
def step_impl(context, url):
    context.driver.get(url)
    time.sleep(5)
    assert context.driver.current_url == url

@then(u'User Inyerface website is opened successfully with title "{title}"')
def step_impl(context, title):
    assert context.driver.title == title


@then(u'User Inyerface logo is displayed on webpage')
def step_impl(context):
    assert context.home_page.get_logo_element(context.driver) is not None


@when(u'User clicks HERE on page to goto the next page')
def step_impl(context):
    assert context.home_page.click_HERE_element(context.driver)


@then(u'User enters the First Page of the Challenge')
def step_impl(context):
    assert context.form_page_1_of_4.get_1_of_4_element(context.driver) is not None


@when(u'User accepts cookies')
def step_impl(context):
    assert context.form_page_1_of_4.click_not_really_no_element(context.driver)


@when(u'Selects Password field, clears the existing text')
def step_impl(context):
    assert context.form_page_1_of_4.clear_password_element(context.driver)


@when(u'Enters a new password')
def step_impl(context):
    assert context.form_page_1_of_4.enter_password(context.driver)


@when(u'Selects Email field, clears the existing text')
def step_impl(context):
    assert context.form_page_1_of_4.clear_email_element(context.driver)


@when(u'Enter user\'s email')
def step_impl(context):
    assert context.form_page_1_of_4.enter_email(context.driver) == True


@when(u'Selects Domain field, clears the existing text')
def step_impl(context):
    assert context.form_page_1_of_4.clear_domain_element(context.driver) == True


@when(u'Enters user\'s domain')
def step_impl(context):
    assert context.form_page_1_of_4.enter_domain(context.driver) == True


@when(u'Click Other drop down field and select ".com"')
def step_impl(context):
    assert context.form_page_1_of_4.choose_other_field(context.driver)


@when(u'Uncheck I do not accept the Terms & Conditions')
def step_impl(context):
    assert context.form_page_1_of_4.click_to_uncheck_tc_field(context.driver)


@when(u'Click Terms & Conditions')
def step_impl(context):
    assert context.form_page_1_of_4.click_tc_link(context.driver)


@when(u'Scroll the Terms & Conditions and Click Accept Button')
def step_impl(context):
    assert context.form_page_1_of_4.scroll_tc_box(context.driver)


@when(u'Click Next link in form 1 of 4')
def step_impl(context):
    assert context.form_page_1_of_4.click_next_button(context.driver)


@then(u'User form 1 of 4 is completed successfully and enters form 2 of 4')
def step_impl(context):
    assert context.form_page_2_of_4.get_2_of_4_element(context.driver) is not None


@when(u'User clicks on upload to upload picture')
def step_impl(context):
    assert context.form_page_2_of_4.upload_picture(context.driver)


@when(u'Click on Unselect all to uncheck all options')
def step_impl(context):
    assert context.form_page_2_of_4.uncheck_unselect_all_element(context.driver)


@when(u'Selects any 3 options excluding Select all and Unselect all')
def step_impl(context):
    assert context.form_page_2_of_4.select_3_valid_options(context.driver)


@when(u'Clicks Next Button')
def step_impl(context):
    assert context.form_page_2_of_4.click_next_element(context.driver)


@then(u'User form 2 of 4 is completed successfully and enters form 3 of 4')
def step_impl(context):
    assert context.form_page_3_of_4.get_3_of_4_element(context.driver) is not None


@when(u'User clicks on First Name textbox, clears existing text and enters User\'s First Name')
def step_impl(context):
    assert context.form_page_3_of_4.enter_first_name(context.driver)


@when(u'Chooses Users\'s title from drop down box')
def step_impl(context):
    assert context.form_page_3_of_4.choose_title(context.driver)


@when(u'Clicks on Surname textbox, clears existing text and enters User\'s Surname')
def step_impl(context):
    assert context.form_page_3_of_4.enter_surname(context.driver)


@when(u'Clicks on Street textbox, clears existing text and enters User\'s Street')
def step_impl(context):
    assert context.form_page_3_of_4.enter_street(context.driver)


@when(u'Gives Number value by clicking on increment icon')
def step_impl(context):
    assert context.form_page_3_of_4.enter_number(context.driver)


@when(u'Clicks on Zip textbox, clears existing text and enters User\'s Zip')
def step_impl(context):
    assert context.form_page_3_of_4.enter_zip(context.driver)


@when(u'Clicks on City textbox, clears existing text and enters User\'s City')
def step_impl(context):
    assert context.form_page_3_of_4.enter_city(context.driver)


@when(u'Chooses a Country from drop down list')
def step_impl(context):
    assert context.form_page_3_of_4.choose_country(context.driver)


@when(u'Gives Box value by clicking on increment icon')
def step_impl(context):
    assert context.form_page_3_of_4.enter_box(context.driver)


@when(u'Chooses Day,Month,Year to provide Birthday')
def step_impl(context):
    assert context.form_page_3_of_4.enter_DOB(context.driver)


@when(u'Slides the Age appropriate to Birthday')
def step_impl(context):
    assert context.form_page_3_of_4.slide_age(context.driver)


@when(u'Selects Gender')
def step_impl(context):
    assert context.form_page_3_of_4.select_gender(context.driver)


@when(u'Clicks Next Button in form 3 of 4')
def step_impl(context):
    assert context.form_page_3_of_4.click_next(context.driver)


@then(u'User form 3 of 4 is completed successfully and enters form 4 of 4')
def step_impl(context):
    assert context.form_page_4_of_4.get_4_of_4_element(context.driver) is not None


@when(u'User selects appropriate pictures')
def step_impl(context):
    assert context.form_page_4_of_4.select_pictures(context.driver)


@when(u'Clicks Validate')
def step_impl(context):
    assert context.form_page_4_of_4.click_validate(context.driver)


@then(u'User successfully completed User Inyerface Challenge')
def step_impl(context):
    time.sleep(2)
    assert context.final_page.get_awesome_element(context.driver)
