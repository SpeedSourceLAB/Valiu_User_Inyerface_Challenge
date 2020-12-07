Feature: User Inyerface challenge
  Take the User Inyerface challenge, a exploration of
  user interactions and design patterns.
  To play the game, simply fill in the form
  as fast and accurate as possible.

  Scenario: User Inyerface Set up
    Given The User Inyerface URL "https://userinyerface.com/" is entered in browser
    Then User Inyerface website is opened successfully with title "User Inyerface - A worst-practice UI experiment"
     And User Inyerface logo is displayed on webpage

  Scenario: Enter First Page of the Challenge
    When User clicks HERE on page to goto the next page
    Then User enters the First Page of the Challenge

  Scenario: Fill form 1 of 4
    When User accepts cookies
    And Selects Password field, clears the existing text
    And Enters a new password
    And Selects Email field, clears the existing text
    And Enter user's email
    And Selects Domain field, clears the existing text
    And Enters user's domain
    And Click Other drop down field and select ".com"
    And Uncheck I do not accept the Terms & Conditions
    And Click Terms & Conditions
    And Scroll the Terms & Conditions and Click Accept Button
    And Click Next link in form 1 of 4
    Then User form 1 of 4 is completed successfully and enters form 2 of 4

  Scenario: Fill form 2 of 4
    When User clicks on upload to upload picture
    And Click on Unselect all to uncheck all options
    And Selects any 3 options excluding Select all and Unselect all
    And Clicks Next Button
    Then User form 2 of 4 is completed successfully and enters form 3 of 4

  Scenario: Fill form 3 of 4
    When User clicks on First Name textbox, clears existing text and enters User's First Name
    And Chooses Users's title from drop down box
    And Clicks on Surname textbox, clears existing text and enters User's Surname
    And Clicks on Street textbox, clears existing text and enters User's Street
    And Gives Number value by clicking on increment icon
    And Clicks on Zip textbox, clears existing text and enters User's Zip
    And Clicks on City textbox, clears existing text and enters User's City
    And Chooses a Country from drop down list
    And Gives Box value by clicking on increment icon
    And Chooses Day,Month,Year to provide Birthday
    And Slides the Age appropriate to Birthday
    And Selects Gender
    And Clicks Next Button in form 3 of 4
    Then User form 3 of 4 is completed successfully and enters form 4 of 4

  Scenario: Fill form 4 of 4
    When User selects appropriate pictures
    And Clicks Validate
    Then User successfully completed User Inyerface Challenge