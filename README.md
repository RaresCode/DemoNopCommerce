
# Testing DemoNopCommerce
Testing if all informations about every single item available for selling from every category correspond to the ones present in the database, test end to end workflow of ordering an item, creating an entry in the database with informations about the item and about shipping info, validate if the info have been saved succesfully in the database.

## Features

- Action Wrapper Pattern
- Database Testing
- Html Reporting
- WebDriverManager
- Selenium
- Unittest

## Usage/Example

![d](https://user-images.githubusercontent.com/91252395/147587792-935aed70-f3bc-4ab3-90e6-65231c45febf.gif)


## HtmlTestRunner Result Example

![Capture1](https://user-images.githubusercontent.com/91252395/147588021-a168a561-b5c3-4cac-a767-70699ecd8e5a.PNG)


## Installation

- Install and configure Python3

- Install and configure MySql Server

- Import cloned repository as project

- Import the self-contained file available in fixtures folder

- Make sure you change database connection informations such as host, username, password to yours in the DatabaseWrapper.py available in the helpers folder otherwise it will not work

- Install all the required packages:

```bash
  pip install -r requirements.txt
```
- To run all tests at once use All_TestSuites.py available in TestSuites under Tests folder, you can also run tests individually if you want to
