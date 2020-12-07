# Valiu_User_Inyerface_Challenge

This project's main purpose is to automate the user interactions and successfully finish the challenge by filling the 4 forms that requires interactions with different web elements.

The project is implemented with Python and Gherkin Language.

##Setup and Execution instructions.

1. Python version used: Python 3.7.7

   Operation system : Windows 10 (Using pyautoit python module which is specific to Windows)

2. Install Git if you dont have in your system.
 
   https://git-scm.com/download/win 

3. Open Git Bash and clone this repository in a directory.
   
   $ git clone https://github.com/SpeedSourceLAB/Valiu_User_Inyerface_Challenge.git

4. Open the cloned project in a code editor.

5. Activate Virtual environment by moving to folder Valiu_User_Inyerface_Challenge\Valiu_User_Inyerface_Challenge
   and providig command .\venv\Scripts\activate

   Valiu_User_Inyerface_Challenge\Valiu_User_Inyerface_Challenge>.\venv\Scripts\activate
   
6. There is a place while filling form 2 / 4 where we need to upload a picture for that goto file


   Valiu_User_Inyerface_Challenge\Valiu_User_Inyerface_Challenge\features\Page_Objs\Utilities.py
   and change the path in line 233.
   'control_set_text("Open", "Edit1", "C:\\Users\\prade\\Downloads\\cute_dog.jpeg")'

7. Open terminal and move to features folder and give command "behave"

8. The script runs and completes the User Inyerface Challenge.

*A known behaviour in this automation is that the Terms and Conditions box is scrolled for about 10 mins.
 Please wait till the entire scrolling is finished and the script to click the Accept button* 


For additional overview and some issues with web application and code are provied in a word document in mail.
