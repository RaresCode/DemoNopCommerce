
# Testing DemoNopCommerce
The aim of this project is to ensure the accuracy and reliability of the item information stored in the database while validating the end-to-end workflow of ordering an item. The project will test whether all information about every single item available for sale in various categories corresponds to the data in the database. Additionally, the project will verify the successful creation of entries in the database with comprehensive details about the item and shipping information, followed by a validation process to confirm that the information has been saved successfully.

## Project Objectives:

- Information Validation: Verify if all information regarding every item available for sale from each category matches the corresponding data present in the database.
- End-to-End Workflow Testing: Test the entire order workflow, including item selection, order placement, database entry creation, and shipping information capture.
- Database Entry Verification: Validate that the database accurately reflects the item and shipping information after an order is placed.
- Error Detection and Reporting: Identify any inconsistencies, inaccuracies, or discrepancies in the item information or database entries and report them for resolution.
- Reliability and Data Integrity: Ensure that the data is securely stored in the database, maintaining its integrity throughout the order workflow process.

## Features

- Action Wrapper Pattern
- Database Testing
- Html Reporting
- WebDriverManager
- Selenium
- Unittest

## Usage/Example

![d](https://user-images.githubusercontent.com/91252395/147587792-935aed70-f3bc-4ab3-90e6-65231c45febf.gif)

## Watch The Entire Testing Process

https://user-images.githubusercontent.com/91252395/149943071-41502bac-bf34-4529-8ec9-e029091064be.mp4

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
