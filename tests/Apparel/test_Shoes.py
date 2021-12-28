import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_007_Shoes(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Shoes")
        cls.database = DatabaseWrapper("apparel")
        cls.driver.openpage()
        cls.driver.move_mouse("Apparel", "link_text")
        cls.driver.click("Shoes", "link_text")
    
    # This will test item24 in section shoes from apparel category 
    def test_item24(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Nike Floral Roshe", "partial_link_text")
        self.ItemName24 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem24 = self.driver.find_text("Nike", "link_text")
        self.StockItem24 = self.driver.find_text("stock-availability-value-24", "id")
        self.SkuItem24 = self.driver.find_text("sku-24", "id")
        self.PriceItem24 = self.driver.getintprice(self.driver.find_text("price-value-24", "class_name"))
        self.driver.prev_page()

        # The following code is used to get the info from the database
        self.DatabaseItemName24 = self.database.get_from_database("Name", self.SkuItem24)
        self.DatabaseManufacturerItem24 = self.database.get_from_database("Manufacturer", self.SkuItem24)
        self.DatabaseStockItem24 = self.database.get_from_database("Availability", self.SkuItem24)
        self.DatabaseSkuItem24 = self.database.get_from_database("SKU", self.SkuItem24)
        self.DatabasePriceItem24 = self.database.get_from_database("Price", self.SkuItem24)
          
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed       
        self.assertEqual([self.ItemName24, self.ManufacturerItem24, self.StockItem24, self.SkuItem24, self.PriceItem24], [self.DatabaseItemName24, self.DatabaseManufacturerItem24, self.DatabaseStockItem24, self.DatabaseSkuItem24, self.DatabasePriceItem24])

    # This will test item25 in section shoes from apparel category 
    def test_item25(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("adidas Consortium Campus 80s", "partial_link_text")
        self.ItemName25 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem25 = self.driver.getmanufacturer(self.ItemName25, 1)
        self.StockItem25 = self.driver.find_text("stock-availability-value-25", "id")
        self.SkuItem25 = self.driver.find_text("sku-25", "id")
        self.PriceItem25 = self.driver.getintprice(self.driver.find_text("price-value-25", "class_name"))
        self.driver.prev_page()

        # The following code is used to get the info from the database
        self.DatabaseItemName25 = self.database.get_from_database("Name", self.SkuItem25)
        self.DatabaseManufacturerItem25 = self.database.get_from_database("Manufacturer", self.SkuItem25)
        self.DatabaseStockItem25 = self.database.get_from_database("Availability", self.SkuItem25)
        self.DatabaseSkuItem25 = self.database.get_from_database("SKU", self.SkuItem25)
        self.DatabasePriceItem25 = self.database.get_from_database("Price", self.SkuItem25)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed             
        self.assertEqual([self.ItemName25, self.ManufacturerItem25, self.StockItem25, self.SkuItem25, self.PriceItem25], [self.DatabaseItemName25, self.DatabaseManufacturerItem25, self.DatabaseStockItem25, self.DatabaseSkuItem25, self.DatabasePriceItem25])

    # This will test item26 in section shoes from apparel category 
    def test_item26(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Nike SB Zoom Stefan Janoski", "partial_link_text")
        self.ItemName26 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem26 = self.driver.find_text("Nike", "link_text")
        self.StockItem26 = self.driver.find_text("stock-availability-value-26", "id")
        self.SkuItem26 = self.driver.find_text("sku-26", "id")
        self.PriceItem26 = self.driver.getintprice(self.driver.find_text("price-value-26", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName26 = self.database.get_from_database("Name", self.SkuItem26)
        self.DatabaseManufacturerItem26 = self.database.get_from_database("Manufacturer", self.SkuItem26)
        self.DatabaseStockItem26 = self.database.get_from_database("Availability", self.SkuItem26)
        self.DatabaseSkuItem26 = self.database.get_from_database("SKU", self.SkuItem26)
        self.DatabasePriceItem26 = self.database.get_from_database("Price", self.SkuItem26)
         
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed               
        self.assertEqual([self.ItemName26, self.ManufacturerItem26, self.StockItem26, self.SkuItem26, self.PriceItem26], [self.DatabaseItemName26, self.DatabaseManufacturerItem26, self.DatabaseStockItem26, self.DatabaseSkuItem26, self.DatabasePriceItem26])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()


# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Shoes", verbosity=2, combine_reports=True))