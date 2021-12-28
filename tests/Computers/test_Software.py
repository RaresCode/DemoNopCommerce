import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_003_Software(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Software")
        cls.database = DatabaseWrapper("computers")
        cls.driver.openpage()
        cls.driver.move_mouse("Computers", "link_text")
        cls.driver.click("Software", "link_text")
    
    # This will test item10 in section software from computers category   
    def test_item10(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Adobe Photoshop CS4", "link_text")
        self.ItemName10 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem10 = self.driver.getmanufacturer(self.ItemName10, 1)
        self.StockItem10 = self.driver.find_text("stock-availability-value-10", "id")
        self.SkuItem10 = self.driver.find_text("sku-10", "id")
        self.PriceItem10 = self.driver.getintprice(self.driver.find_text("price-value-10", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName10 = self.database.get_from_database("Name", self.SkuItem10)
        self.DatabaseManufacturerItem10 = self.database.get_from_database("Manufacturer", self.SkuItem10)
        self.DatabaseStockItem10 = self.database.get_from_database("Availability", self.SkuItem10)
        self.DatabaseSkuItem10 = self.database.get_from_database("SKU", self.SkuItem10)
        self.DatabasePriceItem10 = self.database.get_from_database("Price", self.SkuItem10)
                
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName10, self.ManufacturerItem10, self.StockItem10, self.SkuItem10, self.PriceItem10], [self.DatabaseItemName10, self.DatabaseManufacturerItem10, self.DatabaseStockItem10, self.DatabaseSkuItem10, self.DatabasePriceItem10])
    
    # This will test item11 in section software from computers category   
    def test_item11(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Windows 8 Pro", "link_text")
        self.ItemName11 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem11 = self.driver.getmanufacturer(self.ItemName11, 1)
        self.StockItem11 = self.driver.find_text("stock-availability-value-11", "id")
        self.SkuItem11 = self.driver.find_text("sku-11", "id")
        self.PriceItem11 = self.driver.getintprice(self.driver.find_text("price-value-11", "class_name"))
        self.driver.prev_page()
                
        # The following code is used to get the info from the database
        self.DatabaseItemName11 = self.database.get_from_database("Name", self.SkuItem11)
        self.DatabaseManufacturerItem11 = self.database.get_from_database("Manufacturer", self.SkuItem11)
        self.DatabaseStockItem11 = self.database.get_from_database("Availability", self.SkuItem11)
        self.DatabaseSkuItem11 = self.database.get_from_database("SKU", self.SkuItem11)
        self.DatabasePriceItem11 = self.database.get_from_database("Price", self.SkuItem11)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed      
        self.assertEqual([self.ItemName11, self.ManufacturerItem11, self.StockItem11, self.SkuItem11, self.PriceItem11], [self.DatabaseItemName11, self.DatabaseManufacturerItem11, self.DatabaseStockItem11, self.DatabaseSkuItem11, self.DatabasePriceItem11])

    # This will test item12 in section software from computers category   
    def test_item12(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Sound Forge Pro 11 (recurring)", "partial_link_text")
        self.ItemName12 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem12 = self.driver.getmanufacturer(self.ItemName12, 2)
        self.StockItem12 = self.driver.find_text("stock-availability-value-12", "id")
        self.SkuItem12 = self.driver.find_text("sku-12", "id")
        self.PriceItem12 = self.driver.getintprice(self.driver.find_text("price-value-12", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName12 = self.database.get_from_database("Name", self.SkuItem12)
        self.DatabaseManufacturerItem12 = self.database.get_from_database("Manufacturer", self.SkuItem12)
        self.DatabaseStockItem12 = self.database.get_from_database("Availability", self.SkuItem12)
        self.DatabaseSkuItem12 = self.database.get_from_database("SKU", self.SkuItem12)
        self.DatabasePriceItem12 = self.database.get_from_database("Price", self.SkuItem12)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName12, self.ManufacturerItem12, self.StockItem12, self.SkuItem12, self.PriceItem12], [self.DatabaseItemName12, self.DatabaseManufacturerItem12, self.DatabaseStockItem12, self.DatabaseSkuItem12, self.DatabasePriceItem12])

    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Software", verbosity=2, combine_reports=True))