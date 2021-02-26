from selenium.webdriver.common.by import By

class Locator:

    #Locators for login page
    username = (By.NAME, "uid")
    password = (By.NAME, "password")
    login_web = (By.NAME, "btnLogin")
    logout_web = (By.LINK_TEXT, "Log out")

    #Locators for home page
    new_customer = (By.LINK_TEXT , "New Customer")
    customer_name = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input")
    gender = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]")
    dob = (By.ID, "dob")
    address = (By.NAME, "addr")
    city = (By.NAME, "city")
    state = (By.NAME, "state")
    pin = (By.NAME, "pinno")
    mobile_no = (By.NAME, "telephoneno")
    email = (By.NAME, "emailid")
    password = (By.NAME, "password")
    add_customer = (By.NAME, "sub")