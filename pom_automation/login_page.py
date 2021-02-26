from initialize_driver import InitializeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators import Locator

class Login(InitializeDriver):

    def send_username_input(self,username):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(Locator.username)
        ).send_keys(username,Keys.TAB)

    def send_password_input(self,password):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(Locator.password)
        ).send_keys(password,Keys.TAB)

    def login(self):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(Locator.login_web)
        ).send_keys(Keys.ENTER)


    def logout(self):

        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(Locator.logout_web)
        ).send_keys(Keys.ENTER)