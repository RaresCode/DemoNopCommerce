import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_012_Jewelry(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper and it will perform a click on the category
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Jewelry")
        cls.database = DatabaseWrapper("jewelry")
        cls.driver.openpage()
        cls.driver.click("Jewelry", "link_text")
        
    # This will test item40 from Jewelry category
    def test_item40(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Elegant Gemstone Necklace (rental)", "link_text")
        self.ItemName40 = self.driver.find_text("h1", "tag_name")
        self.StockItem40 = self.driver.find_text("stock-availability-value-40", "id")
        self.SkuItem40 = self.driver.find_text("sku-40", "id")
        self.PriceItem40 = self.driver.getintprice(self.driver.find_text("price-value-40", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName40 = self.database.get_from_database("Name", self.SkuItem40)
        self.DatabaseStockItem40 = self.database.get_from_database("Availability", self.SkuItem40)
        self.DatabaseSkuItem40 = self.database.get_from_database("SKU", self.SkuItem40)
        self.DatabasePriceItem40 = self.database.get_from_database("Price", self.SkuItem40)
                    
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName40, self.StockItem40, self.SkuItem40, self.PriceItem40], [self.DatabaseItemName40, self.DatabaseStockItem40, self.DatabaseSkuItem40, self.DatabasePriceItem40])

    # This will test item41 from Jewelry category
    def test_item41(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Flower Girl Bracelet", "link_text")
        self.ItemName41 = self.driver.find_text("h1", "tag_name")
        self.StockItem41 = self.driver.find_text("stock-availability-value-41", "id")
        self.SkuItem41 = self.driver.find_text("sku-41", "id")
        self.PriceItem41 = self.driver.getintprice(self.driver.find_text("price-value-41", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName41 = self.database.get_from_database("Name", self.SkuItem41)
        self.DatabaseStockItem41 = self.database.get_from_database("Availability", self.SkuItem41)
        self.DatabaseSkuItem41 = self.database.get_from_database("SKU", self.SkuItem41)
        self.DatabasePriceItem41 = self.database.get_from_database("Price", self.SkuItem41)

        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName41, self.StockItem41, self.SkuItem41, self.PriceItem41], [self.DatabaseItemName41, self.DatabaseStockItem41, self.DatabaseSkuItem41, self.DatabasePriceItem41])

    # This will test item42 from Jewelry category
    def test_item42(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Vintage Style Engagement Ring", "link_text")
        self.ItemName42 = self.driver.find_text("h1", "tag_name")
        self.StockItem42 = self.driver.find_text("stock-availability-value-42", "id")
        self.SkuItem42 = self.driver.find_text("sku-42", "id")
        self.PriceItem42 = self.driver.getintprice(self.driver.find_text("price-value-42", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName42 = self.database.get_from_database("Name", self.SkuItem42)
        self.DatabaseStockItem42 = self.database.get_from_database("Availability", self.SkuItem42)
        self.DatabaseSkuItem42 = self.database.get_from_database("SKU", self.SkuItem42)
        self.DatabasePriceItem42 = self.database.get_from_database("Price", self.SkuItem42)
                  
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName42, self.StockItem42, self.SkuItem42, self.PriceItem42], [self.DatabaseItemName42, self.DatabaseStockItem42, self.DatabaseSkuItem42, self.DatabasePriceItem42])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()


# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name= "Test_Jewelry", verbosity=2, combine_reports=True))