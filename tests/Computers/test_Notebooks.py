import sys
import os
directory = os.path.abspath("..\\..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_002_Notebooks(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_Notebooks")
        cls.database = DatabaseWrapper("computers")
        cls.driver.openpage()
        cls.driver.move_mouse("Computers", "link_text")
        cls.driver.click("Notebooks", "link_text")
        
    # This will test item4 in section notebooks from computers category    
    def test_item4(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Apple MacBook Pro 13-inch", "link_text")
        self.ItemName4 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem4 = self.driver.find_text("Apple", "link_text")
        self.StockItem4 = self.driver.find_text("stock-availability-value-4", "id")
        self.SkuItem4 = self.driver.find_text("sku-4", "id")
        self.PriceItem4 = self.driver.getintprice(self.driver.find_text("price-value-4", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName4 = self.database.get_from_database("Name", self.SkuItem4)
        self.DatabaseManufacturerItem4 = self.database.get_from_database("Manufacturer", self.SkuItem4)
        self.DatabaseStockItem4 = self.database.get_from_database("Availability", self.SkuItem4)
        self.DatabaseSkuItem4 = self.database.get_from_database("SKU", self.SkuItem4)
        self.DatabasePriceItem4 = self.database.get_from_database("Price", self.SkuItem4)
                
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName4, self.ManufacturerItem4, self.StockItem4, self.SkuItem4, self.PriceItem4], [self.DatabaseItemName4, self.DatabaseManufacturerItem4, self.DatabaseStockItem4, self.DatabaseSkuItem4, self.DatabasePriceItem4])

    # This will test item5 in section notebooks from computers category            
    def test_item5(self): 
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Asus N551JK-XO076H Laptop", "link_text")
        self.ItemName5 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem5 = self.driver.getmanufacturer(self.ItemName5, 1)
        self.StockItem5 = self.driver.find_text("stock-availability-value-5", "id")
        self.SkuItem5 = self.driver.find_text("sku-5", "id")
        self.PriceItem5 = self.driver.getintprice(self.driver.find_text("price-value-5", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName5 = self.database.get_from_database("Name", self.SkuItem5)
        self.DatabaseManufacturerItem5 = self.database.get_from_database("Manufacturer", self.SkuItem5)
        self.DatabaseStockItem5 = self.database.get_from_database("Availability", self.SkuItem5)
        self.DatabaseSkuItem5 = self.database.get_from_database("SKU", self.SkuItem5)
        self.DatabasePriceItem5 = self.database.get_from_database("Price", self.SkuItem5)
        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName5, self.ManufacturerItem5, self.StockItem5, self.SkuItem5, self.PriceItem5], [self.DatabaseItemName5, self.DatabaseManufacturerItem5, self.DatabaseStockItem5, self.DatabaseSkuItem5, self.DatabasePriceItem5])

    # This will test item6 in section notebooks from computers category            
    def test_item6(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Samsung Series 9 NP900X4C", "partial_link_text")
        self.ItemName6 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem6 = self.driver.getmanufacturer(self.ItemName6, 1)
        self.StockItem6 = self.driver.find_text("stock-availability-value-6", "id")
        self.SkuItem6 = self.driver.find_text("sku-6", "id")
        self.PriceItem6 = self.driver.getintprice(self.driver.find_text("price-value-6", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName6 = self.database.get_from_database("Name", self.SkuItem6)
        self.DatabaseManufacturerItem6 = self.database.get_from_database("Manufacturer", self.SkuItem6)
        self.DatabaseStockItem6 = self.database.get_from_database("Availability", self.SkuItem6)
        self.DatabaseSkuItem6 = self.database.get_from_database("SKU", self.SkuItem6)
        self.DatabasePriceItem6 = self.database.get_from_database("Price", self.SkuItem6)
                   
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed      
        self.assertEqual([self.ItemName6, self.ManufacturerItem6, self.StockItem6, self.SkuItem6, self.PriceItem6], [self.DatabaseItemName6, self.DatabaseManufacturerItem6, self.DatabaseStockItem6, self.DatabaseSkuItem6, self.DatabasePriceItem6])

    # This will test item7 in section notebooks from computers category    
    def test_item7(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("HP Spectre XT Pro UltraBook", "link_text")
        self.ItemName7 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem7 = self.driver.find_text("HP", "link_text")
        self.StockItem7 = self.driver.find_text("stock-availability-value-7", "id")
        self.SkuItem7 = self.driver.find_text("sku-7", "id")
        self.PriceItem7 = self.driver.getintprice(self.driver.find_text("price-value-7", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName7 = self.database.get_from_database("Name", self.SkuItem7)
        self.DatabaseManufacturerItem7 = self.database.get_from_database("Manufacturer", self.SkuItem7)
        self.DatabaseStockItem7 = self.database.get_from_database("Availability", self.SkuItem7)
        self.DatabaseSkuItem7 = self.database.get_from_database("SKU", self.SkuItem7)
        self.DatabasePriceItem7 = self.database.get_from_database("Price", self.SkuItem7)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName7, self.ManufacturerItem7, self.StockItem7, self.SkuItem7, self.PriceItem7], [self.DatabaseItemName7, self.DatabaseManufacturerItem7, self.DatabaseStockItem7, self.DatabaseSkuItem7, self.DatabasePriceItem7])

    # This will test item8 in section notebooks from computers category       
    def test_item8(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("HP Envy 6-1180ca 15.6-Inch", "partial_link_text")
        self.ItemName8 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem8 = self.driver.find_text("HP", "link_text")
        self.StockItem8 = self.driver.find_text("stock-availability-value-8", "id")
        self.SkuItem8 = self.driver.find_text("sku-8", "id")
        self.PriceItem8 = self.driver.getintprice(self.driver.find_text("price-value-8", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName8 = self.database.get_from_database("Name", self.SkuItem8)
        self.DatabaseManufacturerItem8 = self.database.get_from_database("Manufacturer", self.SkuItem8)
        self.DatabaseStockItem8 = self.database.get_from_database("Availability", self.SkuItem8)
        self.DatabaseSkuItem8 = self.database.get_from_database("SKU", self.SkuItem8)
        self.DatabasePriceItem8 = self.database.get_from_database("Price", self.SkuItem8)
                       
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed  
        self.assertEqual([self.ItemName8, self.ManufacturerItem8, self.StockItem8, self.SkuItem8, self.PriceItem8], [self.DatabaseItemName8, self.DatabaseManufacturerItem8, self.DatabaseStockItem8, self.DatabaseSkuItem8, self.DatabasePriceItem8])

    # This will test item9 in section notebooks from computers category    
    def test_item9(self):
        # The following code is used to get the info from the webpage, it gets the item details such as name, stock, sku, price, manufacturer if availiable and compare it with the database ones
        self.driver.click("Lenovo Thinkpad X1 Carbon Laptop", "link_text")
        self.ItemName9 = self.driver.find_text("h1", "tag_name")
        self.ManufacturerItem9 = self.driver.getmanufacturer(self.ItemName9, 1)
        self.StockItem9 = self.driver.find_text("stock-availability-value-9", "id")
        self.SkuItem9 = self.driver.find_text("sku-9", "id")
        self.PriceItem9 = self.driver.getintprice(self.driver.find_text("price-value-9", "class_name"))
        self.driver.prev_page()
        
        # The following code is used to get the info from the database
        self.DatabaseItemName9 = self.database.get_from_database("Name", self.SkuItem9)
        self.DatabaseManufacturerItem9 = self.database.get_from_database("Manufacturer", self.SkuItem9)
        self.DatabaseStockItem9 = self.database.get_from_database("Availability", self.SkuItem9)
        self.DatabaseSkuItem9 = self.database.get_from_database("SKU", self.SkuItem9)
        self.DatabasePriceItem9 = self.database.get_from_database("Price", self.SkuItem9)
                        
        # This is run to check if the results from webpage are the same as in the database and if it is it will mark the test as passed 
        self.assertEqual([self.ItemName9, self.ManufacturerItem9, self.StockItem9, self.SkuItem9, self.PriceItem9], [self.DatabaseItemName9, self.DatabaseManufacturerItem9, self.DatabaseStockItem9, self.DatabaseSkuItem9, self.DatabasePriceItem9])

        
    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()

# Due to a bug in HtmlTestRunner combine_reports=True is required to be able to set a proper name for the test report
if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Test_Notebooks", verbosity=2, combine_reports=True))