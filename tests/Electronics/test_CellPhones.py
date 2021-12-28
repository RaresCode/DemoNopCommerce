import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_005_CellPhones(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_CellPhones")
        cls.database = DatabaseWrapper("electronics")
        cls.driver.openpage()
        cls.driver.move_mouse("Electronics", "link_text")
        cls.driver.click("Cell phones", "link_text")
    
    # This will test item18 in section cellphones from electronics category 
    def test_item18(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("HTC One M8 Android L 5.0 Lollipop", "link_text")
        self.ItemName18 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem18 = self.driver.getmanufacturer(self.ItemName18, 1)
        self.StockItem18 = self.driver.find_text("stock-availability-value-18", "id")
        self.SkuItem18 = self.driver.find_text("sku-18", "id")
        self.PriceItem18 = self.driver.getintprice(self.driver.find_text("price-value-18", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName18 = self.database.get_from_database("Name", self.SkuItem18)
        self.DatabaseManufacturerItem18 = self.database.get_from_database("Manufacturer", self.SkuItem18)
        self.DatabaseStockItem18 = self.database.get_from_database("Availability", self.SkuItem18)
        self.DatabaseSkuItem18 = self.database.get_from_database("SKU", self.SkuItem18)
        self.DatabasePriceItem18 = self.database.get_from_database("Price", self.SkuItem18)
           
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed     
        self.assertEqual([self.ItemName18, self.ManufacturerItem18, self.StockItem18, self.SkuItem18, self.PriceItem18], [self.DatabaseItemName18, self.DatabaseManufacturerItem18, self.DatabaseStockItem18, self.DatabaseSkuItem18, self.DatabasePriceItem18])

    # This will test item19 in section cellphones from electronics category 
    def test_item19(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("HTC One Mini Blue", "link_text")
        self.ItemName19 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem19 = self.driver.getmanufacturer(self.ItemName19, 1)
        self.StockItem19 = self.driver.find_text("stock-availability-value-19", "id")
        self.SkuItem19 = self.driver.find_text("sku-19", "id")
        self.PriceItem19 = self.driver.getintprice(self.driver.find_text("price-value-19", "class_name"))
        self.driver.prev_page()

        # The following code is used to get the info from the database
        self.DatabaseItemName19 = self.database.get_from_database("Name", self.SkuItem19)
        self.DatabaseManufacturerItem19 = self.database.get_from_database("Manufacturer", self.SkuItem19)
        self.DatabaseStockItem19 = self.database.get_from_database("Availability", self.SkuItem19)
        self.DatabaseSkuItem19 = self.database.get_from_database("SKU", self.SkuItem19)
        self.DatabasePriceItem19 = self.database.get_from_database("Price", self.SkuItem19)
                 
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed    
        self.assertEqual([self.ItemName19, self.ManufacturerItem19, self.StockItem19, self.SkuItem19, self.PriceItem19], [self.DatabaseItemName19, self.DatabaseManufacturerItem19, self.DatabaseStockItem19, self.DatabaseSkuItem19, self.DatabasePriceItem19])

    # This will test item20 in section cellphones from electronics category 
    def test_item20(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Nokia Lumia 1020", "link_text")
        self.ItemName20 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem20 = self.driver.getmanufacturer(self.ItemName20, 1)
        self.StockItem20 = self.driver.find_text("stock-availability-value-20", "id")
        self.SkuItem20 = self.driver.find_text("sku-20", "id")
        self.PriceItem20 = self.driver.getintprice(self.driver.find_text("price-value-20", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName20 = self.database.get_from_database("Name", self.SkuItem20)
        self.DatabaseManufacturerItem20 = self.database.get_from_database("Manufacturer", self.SkuItem20)
        self.DatabaseStockItem20 = self.database.get_from_database("Availability", self.SkuItem20)
        self.DatabaseSkuItem20 = self.database.get_from_database("SKU", self.SkuItem20)
        self.DatabasePriceItem20 = self.database.get_from_database("Price", self.SkuItem20)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed     
        self.assertEqual([self.ItemName20, self.ManufacturerItem20, self.StockItem20, self.SkuItem20, self.PriceItem20], [self.DatabaseItemName20, self.DatabaseManufacturerItem20, self.DatabaseStockItem20, self.DatabaseSkuItem20, self.DatabasePriceItem20])

    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_CellPhones", verbosity=2, combine_reports=True))