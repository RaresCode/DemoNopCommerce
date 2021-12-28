import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_011_Books(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper and it will perform a click on the category
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Books")
        cls.database = DatabaseWrapper("books")
        cls.driver.openpage()
        cls.driver.click("Books", "link_text")
        
    # This will test item37 from books category
    def test_item37(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Fahrenheit 451 by Ray Bradbury", "link_text")
        self.ItemName37 = self.driver.find_text("h1", "tag_name")
        self.StockItem37 = self.driver.find_text("stock-availability-value-37", "id")
        self.SkuItem37 = self.driver.find_text("sku-37", "id")
        self.PriceItem37 = self.driver.getintprice(self.driver.find_text("price-value-37", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName37 = self.database.get_from_database("Name", self.SkuItem37)
        self.DatabaseStockItem37 = self.database.get_from_database("Availability", self.SkuItem37)
        self.DatabaseSkuItem37 = self.database.get_from_database("SKU", self.SkuItem37)
        self.DatabasePriceItem37 = self.database.get_from_database("Price", self.SkuItem37)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName37, self.StockItem37, self.SkuItem37, self.PriceItem37], [self.DatabaseItemName37, self.DatabaseStockItem37, self.DatabaseSkuItem37, self.DatabasePriceItem37])

    # This will test item38 from books category
    def test_item38(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("First Prize Pies", "link_text")
        self.ItemName38 = self.driver.find_text("h1", "tag_name")
        self.StockItem38 = self.driver.find_text("stock-availability-value-38", "id")
        self.SkuItem38 = self.driver.find_text("sku-38", "id")
        self.PriceItem38 = self.driver.getintprice(self.driver.find_text("price-value-38", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName38 = self.database.get_from_database("Name", self.SkuItem38)
        self.DatabaseStockItem38 = self.database.get_from_database("Availability", self.SkuItem38)
        self.DatabaseSkuItem38 = self.database.get_from_database("SKU", self.SkuItem38)
        self.DatabasePriceItem38 = self.database.get_from_database("Price", self.SkuItem38)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName38, self.StockItem38, self.SkuItem38, self.PriceItem38], [self.DatabaseItemName38, self.DatabaseStockItem38, self.DatabaseSkuItem38, self.DatabasePriceItem38])

    # This will test item39 from books category
    def test_item39(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Pride and Prejudice", "link_text")
        self.ItemName39 = self.driver.find_text("h1", "tag_name")
        self.StockItem39 = self.driver.find_text("stock-availability-value-39", "id")
        self.SkuItem39 = self.driver.find_text("sku-39", "id")
        self.PriceItem39 = self.driver.getintprice(self.driver.find_text("price-value-39", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName39 = self.database.get_from_database("Name", self.SkuItem39)
        self.DatabaseStockItem39 = self.database.get_from_database("Availability", self.SkuItem39)
        self.DatabaseSkuItem39 = self.database.get_from_database("SKU", self.SkuItem39)
        self.DatabasePriceItem39 = self.database.get_from_database("Price", self.SkuItem39)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName39, self.StockItem39, self.SkuItem39, self.PriceItem39], [self.DatabaseItemName39, self.DatabaseStockItem39, self.DatabaseSkuItem39, self.DatabasePriceItem39])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name= "Test_Books", verbosity=2, combine_reports=True))