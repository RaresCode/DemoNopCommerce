from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import re

"""
Selenium wrapper class is used to store all the actions related to selenium and methods for string formatting then call them when required to get the expected results
Eval It's used a lot in this class due to not being able to use the arguments directly in the code so to avoid this issue eval will execute the string as code
"""
class SeleniumWrapper():
    pageurl = "https://demo.nopcommerce.com/"
    # Initializing driver, setting webdriverwait to 10 seconds, maximizing window and settingtest_name which will be used to give image file name in case of errors during the execution
    def __init__(self, test_name):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.WebDriverWait = WebDriverWait(self.driver, 10)
        self.test_name = test_name
    
    # Quit the browser during test executions
    def closebrowser(self):
        self.driver.quit()
    
    # Open the webpage in which the test will be executed
    def openpage(self):
        self.driver.get(self.pageurl)
    
    # Wait for element to be located, clear and type text into an input field by getting the element, element_type, text to be inputed but not return it
    def type_text(self, element, element_type, text):
        try:
            eval("self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}'))).clear()")
            eval(f"self.driver.find_element_by_{element_type.lower()}('{element}').send_keys('{text}')")
        except (TimeoutException, NoSuchElementException):
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # Wait for element to be located, clear and type text into an input field by getting the element, element_type and text to be inputed and return it
    def type_and_returntext(self, element, element_type, text):
        try:
            eval("self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}'))).clear()")
            eval(f"self.driver.find_element_by_{element_type.lower()}('{element}').send_keys('{text}')")
            return text
        except (TimeoutException, NoSuchElementException):
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
            
    # Wait for element to be located, select the option from dropdown and return it
    def select_and_returnfromdrp(self, element, element_type, drp_select):
        try:
            eval("Select(self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}')))).select_by_visible_text('{drp_select}')")
            return drp_select
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # If a certain element in the page it's present then return yes otherwise no
    def find_if_elementAvailiable(self, element, element_type):
        try:
            eval(f"self.driver.find_element_by_{element_type.lower()}('{element}')")
        except NoSuchElementException:
            return "No"
        else:
            return "Yes"
            
    # It's the same as type_text but uses javascript 
    # def fast_type_text(self, element, element_type, text):
    #     try:
    #         self.driver.execute_script(f'document.getElementBy{element_type}("{element}").value="{text}";')
    #     except TimeoutException:
    #         self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # Return text present in a specific element
    def find_text(self, element, element_type):
        try:
            text = eval("self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}'))).text")
            return text
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # Return to the previous page
    def prev_page(self):
        self.driver.back()

    # Do a click action when called
    def click(self, element, element_type):
        try:
            eval("self.WebDriverWait.until(EC.element_to_be_clickable((By." + f"{element_type.upper()}, '{element}'))).click()")
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # Select a value from dropdown but not return it
    def select_fromdrp(self, element, element_type, drp_select):
        try:
            eval("Select(self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}')))).select_by_value('{drp_select}')")
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
    
    # Move mouse to an element
    def move_mouse(self, element, element_type):
        try:
            self.move_to = eval("self.WebDriverWait.until(EC.presence_of_element_located((By." + f"{element_type.upper()}, '{element}')))")
            self.actions = ActionChains(self.driver)
            self.actions.move_to_element(self.move_to).perform()
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
            
    # Find if the option giftwrap in the page is enabled then return yes otherwise no
    def giftwrap(self, element, element_type):
        try:
            self.giftwrap = eval("self.WebDriverWait.until(EC.visibility_of_element_located((By." + f"{element_type.upper()}, '{element}'))).text")
        except TimeoutException:
            self.driver.save_screenshot("..\\images\\" + f"{self.test_name}" + ".png")
        else:
            for i in self.giftwrap:
                if i == "Yes":
                    return "Yes"
                else:
                    return "No"
    
    # Return the expected manufacturer text from the element text passed to it and the number of names the manufacturer has
    @staticmethod
    def getmanufacturer(ItemName, ManufacturerNameCount):
        manufacturer = ItemName.split()[:ManufacturerNameCount]
        return ' '.join(x for x in manufacturer)

    # Return the intiger or float price from a price string received as argument
    @staticmethod
    def getintprice(price):
        pattern = re.sub("\$|,", "", price.replace(".00", ""))
        try:
            return int(pattern)
        except ValueError:
            return float(pattern)
    
    # Return the intiger variant of the quantity which is received as string
    @staticmethod
    def getintquantity(quantity):
        return int(quantity)
    
    # Return the proper shippingmethod text without the price
    @staticmethod
    def getshippingmethod(shippingmethod):
        return shippingmethod.replace(" ($0.00)", "")
    
    # Return the proper order status
    @staticmethod
    def getorderstatus(orderstatus):
        return orderstatus.replace("Order Status: ", "")
    
    # Return the proper order number
    @staticmethod
    def getordernumber(ordernumber):
        return int(ordernumber.replace("ORDER NUMBER: ", ""))

            
            