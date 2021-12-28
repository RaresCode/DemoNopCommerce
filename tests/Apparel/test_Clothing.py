import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_008_Clothing(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Clothing")
        cls.database = DatabaseWrapper("apparel")
        cls.driver.openpage()
        cls.driver.move_mouse("Apparel", "link_text")
        cls.driver.click("Clothing", "link_text")
    
    # This will test item27 in section clothing from apparel category   
    def test_item27(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Nike Tailwind Loose", "partial_link_text")
        self.ItemName27 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem27 = self.driver.find_text("Nike", "link_text")
        self.StockItem27 = self.driver.find_text("stock-availability-value-27", "id")
        self.SkuItem27 = self.driver.find_text("sku-27", "id")
        self.PriceItem27 = self.driver.getintprice(self.driver.find_text("price-value-27", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName27 = self.database.get_from_database("Name", self.SkuItem27)
        self.DatabaseManufacturerItem27 = self.database.get_from_database("Manufacturer", self.SkuItem27)
        self.DatabaseStockItem27 = self.database.get_from_database("Availability", self.SkuItem27)
        self.DatabaseSkuItem27 = self.database.get_from_database("SKU", self.SkuItem27)
        self.DatabasePriceItem27 = self.database.get_from_database("Price", self.SkuItem27)
                      
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName27, self.ManufacturerItem27, self.StockItem27, self.SkuItem27, self.PriceItem27], [self.DatabaseItemName27, self.DatabaseManufacturerItem27, self.DatabaseStockItem27, self.DatabaseSkuItem27, self.DatabasePriceItem27])

    # This will test item28 in section clothing from apparel category   
    def test_item28(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Oversized Women T-Shirt", "link_text")
        self.ItemName28 = self.driver.find_text("h1", "tag_name")
        self.StockItem28 = self.driver.find_text("stock-availability-value-28", "id")
        self.SkuItem28 = self.driver.find_text("sku-28", "id")
        self.PriceItem28 = self.driver.getintprice(self.driver.find_text("price-value-28", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName28 = self.database.get_from_database("Name", self.SkuItem28)
        self.DatabaseStockItem28 = self.database.get_from_database("Availability", self.SkuItem28)
        self.DatabaseSkuItem28 = self.database.get_from_database("SKU", self.SkuItem28)
        self.DatabasePriceItem28 = self.database.get_from_database("Price", self.SkuItem28)
               
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed        
        self.assertEqual([self.ItemName28, self.StockItem28, self.SkuItem28, self.PriceItem28], [self.DatabaseItemName28, self.DatabaseStockItem28, self.DatabaseSkuItem28, self.DatabasePriceItem28])

    # This will test item29 in section clothing from apparel category   
    def test_item29(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Custom T-Shirt", "link_text")
        self.ItemName29 = self.driver.find_text("h1", "tag_name")
        self.StockItem29 = self.driver.find_text("stock-availability-value-29", "id")
        self.SkuItem29 = self.driver.find_text("sku-29", "id")
        self.PriceItem29 = self.driver.getintprice(self.driver.find_text("price-value-29", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName29 = self.database.get_from_database("Name", self.SkuItem29)
        self.DatabaseStockItem29 = self.database.get_from_database("Availability", self.SkuItem29)
        self.DatabaseSkuItem29 = self.database.get_from_database("SKU", self.SkuItem29)
        self.DatabasePriceItem29 = self.database.get_from_database("Price", self.SkuItem29)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName29, self.StockItem29, self.SkuItem29, self.PriceItem29], [self.DatabaseItemName29, self.DatabaseStockItem29, self.DatabaseSkuItem29, self.DatabasePriceItem29])

    # This will test item30 in section clothing from apparel category   
    def test_item30(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("body > div.master-wrapper-page > div.master-wrapper-content > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(4) > div > div.details > h2 > a", "css_selector")
        self.ItemName30 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem30 = self.driver.getmanufacturer(self.ItemName30, 1)
        self.StockItem30 = self.driver.find_text("stock-availability-value-30", "id")
        self.SkuItem30 = self.driver.find_text("sku-30", "id")
        self.PriceItem30 = self.driver.getintprice(self.driver.find_text("price-value-30", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName30 = self.database.get_from_database("Name", self.SkuItem30)
        self.DatabaseManufacturerItem30 = self.database.get_from_database("Manufacturer", self.SkuItem30)
        self.DatabaseStockItem30 = self.database.get_from_database("Availability", self.SkuItem30)
        self.DatabaseSkuItem30 = self.database.get_from_database("SKU", self.SkuItem30)
        self.DatabasePriceItem30 = self.database.get_from_database("Price", self.SkuItem30)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed   
        self.assertEqual([self.ItemName30, self.ManufacturerItem30, self.StockItem30, self.SkuItem30, self.PriceItem30], [self.DatabaseItemName30, self.DatabaseManufacturerItem30, self.DatabaseStockItem30, self.DatabaseSkuItem30, self.DatabasePriceItem30])

        
    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Clothing", verbosity=2, combine_reports=True))