import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_013_GiftCards(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper and it will perform a click on the category
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_GiftCards")
        cls.database = DatabaseWrapper("giftcards")
        cls.driver.openpage()
        cls.driver.click("Gift Cards", "link_text")
       
    # This will test item43 from GiftCards category
    def test_item43(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("$25 Virtual Gift Card", "link_text")
        self.ItemName43 = self.driver.find_text("h1", "tag_name")
        self.SkuItem43 = self.driver.find_text("sku-43", "id")
        self.PriceItem43 = self.driver.getintprice(self.driver.find_text("price-value-43", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName43 = self.database.get_from_database("Name", self.SkuItem43)
        self.DatabaseSkuItem43 = self.database.get_from_database("SKU", self.SkuItem43)
        self.DatabasePriceItem43 = self.database.get_from_database("Price", self.SkuItem43)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName43, self.SkuItem43, self.PriceItem43], [self.DatabaseItemName43, self.DatabaseSkuItem43, self.DatabasePriceItem43])
        
    # This will test item44 from GiftCards category
    def test_item44(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("$50 Physical Gift Card", "link_text")
        self.ItemName44 = self.driver.find_text("h1", "tag_name")
        self.SkuItem44 = self.driver.find_text("sku-44", "id")
        self.PriceItem44 = self.driver.getintprice(self.driver.find_text("price-value-44", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName44 = self.database.get_from_database("Name", self.SkuItem44)
        self.DatabaseSkuItem44 = self.database.get_from_database("SKU", self.SkuItem44)
        self.DatabasePriceItem44 = self.database.get_from_database("Price", self.SkuItem44)
                
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed  
        self.assertEqual([self.ItemName44, self.SkuItem44, self.PriceItem44], [self.DatabaseItemName44, self.DatabaseSkuItem44, self.DatabasePriceItem44])

    # This will test item45 from GiftCards category
    def test_item45(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("$100 Physical Gift Card", "link_text")
        self.ItemName45 = self.driver.find_text("h1", "tag_name")
        self.SkuItem45 = self.driver.find_text("sku-45", "id")
        self.PriceItem45 = self.driver.getintprice(self.driver.find_text("price-value-45", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName45 = self.database.get_from_database("Name", self.SkuItem45)
        self.DatabaseSkuItem45 = self.database.get_from_database("SKU", self.SkuItem45)
        self.DatabasePriceItem45 = self.database.get_from_database("Price", self.SkuItem45)

        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed       
        self.assertEqual([self.ItemName45, self.SkuItem45, self.PriceItem45], [self.DatabaseItemName45, self.DatabaseSkuItem45, self.DatabasePriceItem45])

    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()
        
# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name= "Test_GiftCards", verbosity=2, combine_reports=True))