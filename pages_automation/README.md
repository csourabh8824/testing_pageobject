# Selenium PageObject

Selenium is a Python library for writing automated testcases.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
pip install selenium
```


## File Structure
```
.
├── home_page.py
├── initialize_driver.py
├── locators.py
├── __pycache__
│   ├── home_page.cpython-36.pyc
│   ├── initialize_driver.cpython-36.pyc
│   ├── locators.cpython-36.pyc
│   └── test.cpython-36.pyc
└── test.py

```
## Explaining files
home_page.py:
Contains all the actions.     
initialize_driver.py: Here we have initialized Chrome driver.   
locators.py: This file contains all the locators to get locators we have used By function.  
test.py: This file contain all the test cases. we have written test cases using unittest
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
