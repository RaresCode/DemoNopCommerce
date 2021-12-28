import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_006_Others(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Others")
        cls.database = DatabaseWrapper("electronics")
        cls.driver.openpage()
        cls.driver.move_mouse("Electronics", "link_text")
        cls.driver.click("Others", "link_text")
    
    # This will test item21 in section others from electronics category 
    def test_item21(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Beats Pill 2.0 Wireless Speaker", "link_text")
        self.ItemName21 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem21 = self.driver.getmanufacturer(self.ItemName21, 2)
        self.StockItem21 = self.driver.find_text("stock-availability-value-21", "id")
        self.SkuItem21 = self.driver.find_text("sku-21", "id")
        self.PriceItem21 = self.driver.getintprice(self.driver.find_text("price-value-21", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName21 = self.database.get_from_database("Name", self.SkuItem21)
        self.DatabaseManufacturerItem21 = self.database.get_from_database("Manufacturer", self.SkuItem21)
        self.DatabaseStockItem21 = self.database.get_from_database("Availability", self.SkuItem21)
        self.DatabaseSkuItem21 = self.database.get_from_database("SKU", self.SkuItem21)
        self.DatabasePriceItem21 = self.database.get_from_database("Price", self.SkuItem21)
                  
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName21, self.ManufacturerItem21, self.StockItem21, self.SkuItem21, self.PriceItem21], [self.DatabaseItemName21, self.DatabaseManufacturerItem21, self.DatabaseStockItem21, self.DatabaseSkuItem21, self.DatabasePriceItem21])
    
    # This will test item22 in section others from electronics category 
    def test_item22(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Universal 7-8 Inch Tablet Cover", "link_text")
        self.ItemName22 = self.driver.find_text("h1", "tag_name")
        self.StockItem22 = self.driver.find_text("stock-availability-value-22", "id")
        self.SkuItem22 = self.driver.find_text("sku-22", "id")
        self.PriceItem22 = self.driver.getintprice(self.driver.find_text("price-value-22", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName22 = self.database.get_from_database("Name", self.SkuItem22)
        self.DatabaseStockItem22 = self.database.get_from_database("Availability", self.SkuItem22)
        self.DatabaseSkuItem22 = self.database.get_from_database("SKU", self.SkuItem22)
        self.DatabasePriceItem22 = self.database.get_from_database("Price", self.SkuItem22)
                    
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName22, self.StockItem22, self.SkuItem22, self.PriceItem22], [self.DatabaseItemName22, self.DatabaseStockItem22, self.DatabaseSkuItem22, self.DatabasePriceItem22])

    # This will test item23 in section others from electronics category 
    def test_item23(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Portable Sound Speakers", "link_text")
        self.ItemName23 = self.driver.find_text("h1", "tag_name")
        self.StockItem23 = self.driver.find_text("stock-availability-value-23", "id")
        self.SkuItem23 = self.driver.find_text("sku-23", "id")
        self.PriceItem23 = self.driver.getintprice(self.driver.find_text("price-value-23", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName23 = self.database.get_from_database("Name", self.SkuItem23)
        self.DatabaseStockItem23 = self.database.get_from_database("Availability", self.SkuItem23)
        self.DatabaseSkuItem23 = self.database.get_from_database("SKU", self.SkuItem23)
        self.DatabasePriceItem23 = self.database.get_from_database("Price", self.SkuItem23)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName23, self.StockItem23, self.SkuItem23, self.PriceItem23], [self.DatabaseItemName23, self.DatabaseStockItem23, self.DatabaseSkuItem23, self.DatabasePriceItem23])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Others", verbosity=2, combine_reports=True))