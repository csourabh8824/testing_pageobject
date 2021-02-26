from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators import Locator
from initialize_driver import InitializeDriver

class HomePage(InitializeDriver,Locator):

    def click_new_customer(self):
        
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.new_customer)
        ).click()

    def fill_customer_name(self, customer_name):
        
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.customer_name)
        ).send_keys(customer_name)

    def select_gender(self):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.gender)
        ).click()

    def date_of_birth(self,dateofbirth):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.dob)
        ).send_keys(dateofbirth)

    def customer_address(self,address):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.address)
        ).send_keys(address)
    
    def customer_city(self, city):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.city)
        ).send_keys(city)

    def customer_state(self, state):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.state)
        ).send_keys(state)

    def customer_pin(self, pin):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.pin)
        ).send_keys(pin)

    def customer_mobile_number(self, number):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.mobile_no)
        ).send_keys(number)

    def customer_email(self, email):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.email)
        ).send_keys(email)

    def customer_password(self, password):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.password)
        ).send_keys(password)

    def submit(self):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.add_customer)
        ).click()