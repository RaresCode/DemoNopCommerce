import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_009_Accessories(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Accessories")
        cls.database = DatabaseWrapper("apparel")
        cls.driver.openpage()
        cls.driver.move_mouse("Apparel", "link_text")
        cls.driver.click("Accessories", "link_text")
        
    # This will test item31 in section accessories from apparel category  
    def test_item31(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Obey Propaganda Hat", "link_text")
        self.ItemName31 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem31 = self.driver.getmanufacturer(self.ItemName31, 1)
        self.StockItem31 = self.driver.find_text("stock-availability-value-31", "id")
        self.SkuItem31 = self.driver.find_text("sku-31", "id")
        self.PriceItem31 = self.driver.getintprice(self.driver.find_text("price-value-31", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName31 = self.database.get_from_database("Name", self.SkuItem31)
        self.DatabaseManufacturerItem31 = self.database.get_from_database("Manufacturer", self.SkuItem31)
        self.DatabaseStockItem31 = self.database.get_from_database("Availability", self.SkuItem31)
        self.DatabaseSkuItem31 = self.database.get_from_database("SKU", self.SkuItem31)
        self.DatabasePriceItem31 = self.database.get_from_database("Price", self.SkuItem31)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed         
        self.assertEqual([self.ItemName31, self.ManufacturerItem31, self.StockItem31, self.SkuItem31, self.PriceItem31], [self.DatabaseItemName31, self.DatabaseManufacturerItem31, self.DatabaseStockItem31, self.DatabaseSkuItem31, self.DatabasePriceItem31])

    # This will test item32 in section accessories from apparel category  
    def test_item32(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Reversible Horseferry Check Belt", "link_text")
        self.ItemName32 = self.driver.find_text("h1", "tag_name")
        self.StockItem32 = self.driver.find_text("stock-availability-value-32", "id")
        self.SkuItem32 = self.driver.find_text("sku-32", "id")
        self.PriceItem32 = self.driver.getintprice(self.driver.find_text("price-value-32", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName32 = self.database.get_from_database("Name", self.SkuItem32)
        self.DatabaseStockItem32 = self.database.get_from_database("Availability", self.SkuItem32)
        self.DatabaseSkuItem32 = self.database.get_from_database("SKU", self.SkuItem32)
        self.DatabasePriceItem32 = self.database.get_from_database("Price", self.SkuItem32)
               
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed         
        self.assertEqual([self.ItemName32, self.StockItem32, self.SkuItem32, self.PriceItem32], [self.DatabaseItemName32, self.DatabaseStockItem32, self.DatabaseSkuItem32, self.DatabasePriceItem32])

    # This will test item33 in section accessories from apparel category  
    def test_item33(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Ray Ban Aviator Sunglasses", "link_text")
        self.ItemName33 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem33 = self.driver.getmanufacturer(self.ItemName33, 2)
        self.StockItem33 = self.driver.find_text("stock-availability-value-33", "id")
        self.SkuItem33 = self.driver.find_text("sku-33", "id")
        self.PriceItem33 = self.driver.getintprice(self.driver.find_text("price-value-33", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName33 = self.database.get_from_database("Name", self.SkuItem33)
        self.DatabaseManufacturerItem33 = self.database.get_from_database("Manufacturer", self.SkuItem33)
        self.DatabaseStockItem33 = self.database.get_from_database("Availability", self.SkuItem33)
        self.DatabaseSkuItem33 = self.database.get_from_database("SKU", self.SkuItem33)
        self.DatabasePriceItem33 = self.database.get_from_database("Price", self.SkuItem33)
          
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed           
        self.assertEqual([self.ItemName33, self.ManufacturerItem33, self.StockItem33, self.SkuItem33, self.PriceItem33], [self.DatabaseItemName33, self.DatabaseManufacturerItem33, self.DatabaseStockItem33, self.DatabaseSkuItem33, self.DatabasePriceItem33])



    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()


# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Accessories", verbosity=2, combine_reports=True))