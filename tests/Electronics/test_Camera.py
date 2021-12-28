import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_004_Camera(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Camera")
        cls.database = DatabaseWrapper("electronics")
        cls.driver.openpage()
        cls.driver.move_mouse("Electronics", "link_text")
        cls.driver.click("Camera & photo", "link_text")
        
    # This will test item14 in section camera from electronics category  
    def test_item14(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Nikon D5500 DSLR", "link_text")
        # Nikon D5500 DSLR - Black
        self.ItemName14 = self.driver.find_text("#product-details-form > div:nth-child(2) > div.product-collateral > div.product-variant-list > div:nth-child(1) > div.variant-overview > div.variant-name", "css_selector")
        self.ManufacturerItem14 = self.driver.getmanufacturer(self.ItemName14, 1)
        self.StockItem14 = self.driver.find_text("stock-availability-value-14", "id")
        self.SkuItem14 = self.driver.find_text("sku-14", "id")
        self.PriceItem14 = self.driver.getintprice(self.driver.find_text("price-value-14", "class_name"))
        
        # The following code is used to get the info from the database
        self.DatabaseItemName14 = self.database.get_from_database("Name", self.SkuItem14)
        self.DatabaseManufacturerItem14 = self.database.get_from_database("Manufacturer", self.SkuItem14)
        self.DatabaseStockItem14 = self.database.get_from_database("Availability", self.SkuItem14)
        self.DatabaseSkuItem14 = self.database.get_from_database("SKU", self.SkuItem14)
        self.DatabasePriceItem14 = self.database.get_from_database("Price", self.SkuItem14)
                
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed                   
        self.assertEqual([self.ItemName14, self.ManufacturerItem14, self.StockItem14, self.SkuItem14, self.PriceItem14], [self.DatabaseItemName14, self.DatabaseManufacturerItem14, self.DatabaseStockItem14, self.DatabaseSkuItem14, self.DatabasePriceItem14])

    # This will test item15 in section camera from electronics category 
    def test_item15(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        # Nikon D5500 DSLR - Red
        self.ItemName15 = self.driver.find_text("#product-details-form > div:nth-child(2) > div.product-collateral > div.product-variant-list > div:nth-child(2) > div.variant-overview > div.variant-name", "css_selector")
        self.ManufacturerItem15 = self.driver.getmanufacturer(self.ItemName15, 1)
        self.StockItem15 = self.driver.find_text("stock-availability-value-15", "id")
        self.SkuItem15 = self.driver.find_text("sku-15", "id")
        self.PriceItem15 = self.driver.getintprice(self.driver.find_text("price-value-15", "class_name"))
        self.driver.prev_page()
    
        # The following code is used to get the info from the database
        self.DatabaseItemName15 = self.database.get_from_database("Name", self.SkuItem15)
        self.DatabaseManufacturerItem15 = self.database.get_from_database("Manufacturer", self.SkuItem15)
        self.DatabaseStockItem15 = self.database.get_from_database("Availability", self.SkuItem15)
        self.DatabaseSkuItem15 = self.database.get_from_database("SKU", self.SkuItem15)
        self.DatabasePriceItem15 = self.database.get_from_database("Price", self.SkuItem15)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed                  
        self.assertEqual([self.ItemName15, self.ManufacturerItem15, self.StockItem15, self.SkuItem15, self.PriceItem15], [self.DatabaseItemName15, self.DatabaseManufacturerItem15, self.DatabaseStockItem15, self.DatabaseSkuItem15, self.DatabasePriceItem15])

    # This will test item16 in section camera from electronics category 
    def test_item16(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Leica T Mirrorless", "partial_link_text")
        self.ItemName16 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem16 = self.driver.getmanufacturer(self.ItemName16, 1)
        self.StockItem16 = self.driver.find_text("stock-availability-value-16", "id")
        self.SkuItem16 = self.driver.find_text("sku-16", "id")
        self.PriceItem16 = self.driver.getintprice(self.driver.find_text("price-value-16", "class_name"))
        self.driver.prev_page()

        # The following code is used to get the info from the database
        self.DatabaseItemName16 = self.database.get_from_database("Name", self.SkuItem16)
        self.DatabaseManufacturerItem16 = self.database.get_from_database("Manufacturer", self.SkuItem16)
        self.DatabaseStockItem16 = self.database.get_from_database("Availability", self.SkuItem16)
        self.DatabaseSkuItem16 = self.database.get_from_database("SKU", self.SkuItem16)
        self.DatabasePriceItem16 = self.database.get_from_database("Price", self.SkuItem16)
               
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed                   
        self.assertEqual([self.ItemName16, self.ManufacturerItem16, self.StockItem16, self.SkuItem16, self.PriceItem16], [self.DatabaseItemName16, self.DatabaseManufacturerItem16, self.DatabaseStockItem16, self.DatabaseSkuItem16, self.DatabasePriceItem16])

    # This will test item17 in section camera from electronics category 
    def test_item17(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Apple iCam", "link_text")
        self.ItemName17 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem17 = self.driver.find_text("Apple", "link_text")
        self.StockItem17 = self.driver.find_text("stock-availability-value-17", "id")
        self.SkuItem17 = self.driver.find_text("sku-17", "id")
        self.PriceItem17 = self.driver.getintprice(self.driver.find_text("price-value-17", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName17 = self.database.get_from_database("Name", self.SkuItem17)
        self.DatabaseManufacturerItem17 = self.database.get_from_database("Manufacturer", self.SkuItem17)
        self.DatabaseStockItem17 = self.database.get_from_database("Availability", self.SkuItem17)
        self.DatabaseSkuItem17 = self.database.get_from_database("SKU", self.SkuItem17)
        self.DatabasePriceItem17 = self.database.get_from_database("Price", self.SkuItem17)
                
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed                  
        self.assertEqual([self.ItemName17, self.ManufacturerItem17, self.StockItem17, self.SkuItem17, self.PriceItem17], [self.DatabaseItemName17, self.DatabaseManufacturerItem17, self.DatabaseStockItem17, self.DatabaseSkuItem17, self.DatabasePriceItem17])


    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Camera", verbosity=2, combine_reports=True))