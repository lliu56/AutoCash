#########################################################################################
# this module consists of functions that will help you with web activity automation
#########################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class BasicWebActivity ():
    def __init__(self,website,accPW,driver_path) -> None:
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.website = website # correct?
        self.accPW = accPW
    

    # basic activties
    def OpenWebsite (self):
        self.driver.get (self.website)
        sleep (0.5)

    def ClickElement (self,element_Xpath):
        try:
            element = self.driver.find_element (By.XPATH,element_Xpath)
        except NoSuchElementException:
            print ("Clickable Element Not found")
        element.click()
        sleep (0.5)
       
    def InputText (self, element_Xpath,text):
        try: 
            element = self.driver.find_element (By.XPATH,element_Xpath)
        except NoSuchElementException:
            print ("Text Field Not Found")
        element.send_keys(text)
        sleep (0.5)

    #login 
    def login (self, login_button_Xpath,acc_Xpath, pw_Xpath,sign_in_button_Xpath, account, password, login_button_presence = True):
        if login_button_presence: 
            self.ClickElement (login_button_Xpath)
            sleep (0.5) 

        self.InputText (acc_Xpath,account)
        self.InputText (pw_Xpath,password)
        self.ClickElement (sign_in_button_Xpath)
