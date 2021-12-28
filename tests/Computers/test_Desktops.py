import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_001_Desktops(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Desktops")
        cls.database = DatabaseWrapper("computers")
        cls.driver.openpage()
        cls.driver.move_mouse("Computers", "link_text")
        cls.driver.click("Desktops", "link_text")
    
    # This will test item1 in section desktops from computers category
    def test_item1(self):
        # The following code is used to get the info from the webpage  it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Build your own computer", "link_text")
        self.ItemName1 = self.driver.find_text("h1", "tag_name")
        self.StockItem1 = self.driver.find_text("stock-availability-value-1", "id")
        self.SkuItem1 = self.driver.find_text("sku-1", "id")
        self.PriceItem1 = self.driver.getintprice(self.driver.find_text("price-value-1", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName1 = self.database.get_from_database("Name", self.SkuItem1)
        self.DatabaseStockItem1 = self.database.get_from_database("Availability", self.SkuItem1)
        self.DatabaseSkuItem1 = self.database.get_from_database("SKU", self.SkuItem1)
        self.DatabasePriceItem1 = self.database.get_from_database("Price", self.SkuItem1)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed
        self.assertEqual([self.ItemName1, self.StockItem1, self.SkuItem1, self.PriceItem1], [self.DatabaseItemName1, self.DatabaseStockItem1, self.DatabaseSkuItem1, self.DatabasePriceItem1])
    
    # This will test item2 in section desktops from computers category
    def test_item2(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Digital Storm VANQUISH 3 Custom Performance PC", "link_text")
        self.ItemName2 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem2 = self.driver.getmanufacturer(self.ItemName2, 2)
        self.StockItem2 = self.driver.find_text("stock-availability-value-2", "id")
        self.SkuItem2 = self.driver.find_text("sku-2", "id")
        self.PriceItem2 = self.driver.getintprice(self.driver.find_text("price-value-2", "class_name"))
        self.driver.prev_page()

        # The following code is used to get the info from the database
        self.DatabaseItemName2 = self.database.get_from_database("Name", self.SkuItem2)
        self.DatabaseManufacturerItem2 = self.database.get_from_database("Manufacturer", self.SkuItem2)
        self.DatabaseStockItem2 = self.database.get_from_database("Availability", self.SkuItem2)
        self.DatabaseSkuItem2 = self.database.get_from_database("SKU", self.SkuItem2)
        self.DatabasePriceItem2 = self.database.get_from_database("Price", self.SkuItem2)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed
        self.assertEqual([self.ItemName2, self.ManufacturerItem2, self.StockItem2, self.SkuItem2, self.PriceItem2], [self.DatabaseItemName2, self.DatabaseManufacturerItem2, self.DatabaseStockItem2, self.DatabaseSkuItem2, self.DatabasePriceItem2])

    # This will test item3 in section desktops from computers category
    def test_item3(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Lenovo IdeaCentre 600 All-in-One PC", "link_text")
        self.ItemName3 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem3 = self.driver.getmanufacturer(self.ItemName3, 1)
        self.StockItem3 = self.driver.find_text("stock-availability-value-3", "id")
        self.SkuItem3 = self.driver.find_text("sku-3", "id")
        self.PriceItem3 = self.driver.getintprice(self.driver.find_text("price-value-3", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName3 = self.database.get_from_database("Name", self.SkuItem3)
        self.DatabaseManufacturerItem3 = self.database.get_from_database("Manufacturer", self.SkuItem3)
        self.DatabaseStockItem3 = self.database.get_from_database("Availability", self.SkuItem3)
        self.DatabaseSkuItem3 = self.database.get_from_database("SKU", self.SkuItem3)
        self.DatabasePriceItem3 = self.database.get_from_database("Price", self.SkuItem3)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName3, self.ManufacturerItem3, self.StockItem3, self.SkuItem3, self.PriceItem3], [self.DatabaseItemName3, self.DatabaseManufacturerItem3, self.DatabaseStockItem3, self.DatabaseSkuItem3, self.DatabasePriceItem3])

    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Desktops", verbosity=2, combine_reports=True))