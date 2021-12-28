import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_010_DigitalDownloads(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper and it will perform a click on the category
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_DigitalDownloads")
        cls.database = DatabaseWrapper("digitaldownloads")
        cls.driver.openpage()
        cls.driver.click("Digital downloads", "link_text")
        
    # This will test item34 from digitaldownloads category
    def test_item34(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("Night Visions", "link_text")
        self.ItemName34 = self.driver.find_text("h1", "tag_name")
        self.SkuItem34 = self.driver.find_text("sku-34", "id")
        self.PriceItem34 = self.driver.getintprice(self.driver.find_text("price-value-34", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName34 = self.database.get_from_database("Name", self.SkuItem34)
        self.DatabaseSkuItem34 = self.database.get_from_database("SKU", self.SkuItem34)
        self.DatabasePriceItem34 = self.database.get_from_database("Price", self.SkuItem34)
                     
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed    
        self.assertEqual([self.ItemName34, self.SkuItem34, self.PriceItem34], [self.DatabaseItemName34, self.DatabaseSkuItem34, self.DatabasePriceItem34])

    # This will test item35 from digitaldownloads category
    def test_item35(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("If You Wait (donation)", "link_text")
        self.ItemName35 = self.driver.find_text("h1", "tag_name")
        self.SkuItem35 = self.driver.find_text("sku-35", "id")
        self.PriceItem35 = 0.5
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName35 = self.database.get_from_database("Name", self.SkuItem35)
        self.DatabaseSkuItem35 = self.database.get_from_database("SKU", self.SkuItem35)
        self.DatabasePriceItem35 = self.database.get_from_database("Price", self.SkuItem35)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed    
        self.assertEqual([self.ItemName35, self.SkuItem35, self.PriceItem35], [self.DatabaseItemName35, self.DatabaseSkuItem35, self.DatabasePriceItem35])

    # This will test item36 from digitaldownloads category
    def test_item36(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, sku, price and compare it with the database ones
        self.driver.click("Science & Faith", "link_text")
        self.ItemName36 = self.driver.find_text("h1", "tag_name")
        self.SkuItem36 = self.driver.find_text("sku-36", "id")
        self.PriceItem36 = 0.5
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName36 = self.database.get_from_database("Name", self.SkuItem36)
        self.DatabaseSkuItem36 = self.database.get_from_database("SKU", self.SkuItem36)
        self.DatabasePriceItem36 = self.database.get_from_database("Price", self.SkuItem36)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed    
        self.assertEqual([self.ItemName36, self.SkuItem36, self.PriceItem36], [self.DatabaseItemName36, self.DatabaseSkuItem36, self.DatabasePriceItem36])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()


# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name= "Test_DigitalDownloads", verbosity=2, combine_reports=True))