import unittest
import time

from initialize_driver import InitializeDriver
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

from home_page import HomePage
from login_page import Login

class TestWebPage(HomePage,Login,InitializeDriver,unittest.TestCase):

    def test_login(self):

        self.driver.get("http://demo.guru99.com/V4/") 
        self.driver.maximize_window()
        self.send_username_input("mngr310967")
        self.send_password_input("utanYzU")
        self.login()
        self.logout()

    def test_home_page_add_customer(self):

        self.driver.get("http://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.maximize_window()

        # These are the actions that are written in home_page.py
        self.click_new_customer()
        self.fill_customer_name("Sakshee bhandari")
        self.select_gender()
        self.date_of_birth("03/06/1997")
        self.customer_address("chandralok colony")
        self.customer_city("Indore")
        self.customer_state("Madhya Pradesh")
        self.customer_pin("452007")
        self.customer_mobile_number("1234567890")
        self.customer_email("sochoudhary@deqode.com")
        self.customer_password("sourabh3210")
        
    
    def tearDown(self):

        time.sleep(3)
        self.driver.close()
        self.driver.quit()