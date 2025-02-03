# Capstone-Project
Automated Testing of SauceDemo using Python Selenium and Pytest

## Description

This respository contains a Python pragram that performs Orange HRM Application Automation utilize Selenium WebDriver to automate various test cases.
## Project Description

This project automates testing of the SauceDemo Application using Python Selenium and Pytest. It covers both positive and negative test cases.

## Project Overview

This project aims to automate the testing of the e-commerce demo web application SauceDemo using Python Selenium and the Pytest framework. The automation framework follows best practices such as Page Object Model (POM) and Data-Driven Testing Format (DDTF). The project ensures that both positive and negative test scenarios are covered and generates pytest-based HTML reports.

## Program Descrition
*  Functionality: Performs Automation testing on a website.
*  Programmer: Naveen Kumar K
*  Date: 02 Feb 2025
*  Version: 1.0
*  Code Library: Selenium
*  Prerequisites: Python, Selenium, ChromeDriver

## Key Tools and Technologies Used:
*  Python: Programming language used to write the test scripts.
*  Selenium: Framework for automating web browsers.
*  Pytest: Testing framework for running tests and generating reports.
*  POM (Page Object Model): Design pattern used for structuring the test scripts.
*  DDTF (Data-Driven Testing Framework): Used for reading test data from an Excel or CSV file and running tests with different sets of data.
*  Explicit Wait: Used in Selenium for waiting for elements to become clickable or visible, improving the reliability of the tests.
*  HTML Reports: Pytest-based reports generated for test results.

## Test Cases
The project includes the following test cases:

Test-Case 1: Login Functionality
* Test login with the following users:
  * standard_user
  * problem_user
  * performance_glitch_user
  * locked_out_user
  * Password: secret_sauce
* Check login using cookies (without URL or page title verification).
* Generate pytest HTML reports.

Test-Case 2: Negative Login Test
* Test login with invalid credentials:
  * Username: guvi_user
  * Password: Secret@123
  * Generate pytest HTML reports.

Test-Case 3: Logout Functionality
* Test whether the logout button is functional.
* Check the visibility of the logout button.
* Generate pytest HTML reports.

Test-Case 4: Cart Button Visibility
* Verify the cart button is visible.
* Generate pytest HTML reports.

Test-Case 5: Random Product Selection
* Randomly select 4 out of the 6 available products using Python.
* Fetch the product name and price.
* Generate pytest HTML reports.

Test-Case 6: Adding Products to Cart
* Randomly select 4 out of 6 products.
* Add selected products to the cart.
* Verify the cart button shows 4 products.
* Generate pytest HTML reports.

Test-Case 7: Cart Product Verification
* Click the cart button and verify the products added.
* Fetch product details from the cart.
* Generate pytest HTML reports.

Test-Case 8: Checkout Process
* Click the checkout button and enter details:
  * First Name
  * Last Name
  * ZIP Code
* Capture a screenshot of the checkout overview in PNG/JPEG format.
* Verify that the products and details match the ones added to the cart.
* Click the finish button and confirm the order.
* Generate pytest HTML reports.

## Project Setup
Prerequisites
Before running the test cases, ensure you have the following installed:
1) Python 3.x
2) Selenium
3) Pytest
4) Pylint
5) WebDriver (ChromeDriver or appropriate WebDriver for your browser)

## Installation
Install the required packages using pip:
1. Intal dependencies `pip install selenium webdriver-manager`.
2. Install dependencies: `pip install selenium pytest`.

## Run Tests
Execute the test cases using the following command:
`pytest -v -s Tests`.

## Test Reports
`pytest -v -s --capture=sys --html=Reports\Tests.html Tests`.
After execution, view the generated HTML report in the reports/ directory.
