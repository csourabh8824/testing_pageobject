# Selenium 

Selenium is a Python library for writing automated test cases.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install selenium
```

## Page Object Model

It help's to keep the code modularized, helps in code reusability and also helps in reducing the amount of duplicated code.


## File Structure and explaination
```
├── home_page.py
├── initialize_driver.py
├── locators.py
├── login_page.py
├── __pycache__
│   ├── home_page.cpython-36.pyc
│   ├── initialize_driver.cpython-36.pyc
│   ├── locators.cpython-36.pyc
│   ├── login_page.cpython-36.pyc
│   └── test.cpython-36.pyc
├── README.md
└── test.py
```
home_page.py : Contains all the actions that are related to the homepage of [this web](http://demo.guru99.com/V4/manager/Managerhomepage.php)  
initialize_driver.py : This file contains all the initializations that are required.  
locators.py : This file contains all the locators, Locators are used to locate the elements in an html page.  
login_page.py: This file contains all the actions that are related to login page of [this web](http://demo.guru99.com/V4/)  
test.py: This file contains test cases , the test cases are written with the help of unittest. Also, test cases are written with the help of actions that are defined in home_page.py and login_page.py file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
