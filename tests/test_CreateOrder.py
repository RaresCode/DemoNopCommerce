import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
from helpers.selenium_wrapper import SeleniumWrapper
from helpers.database_wrapper import DatabaseWrapper
import HtmlTestRunner

class Test_014_CreateOrder(unittest.TestCase):
    """
    This setupclass will be executed before any tests are run within this class, it will define the driver from seleniumwrapper, database from the databasewrapper,
    It will open the page specified in the seleniumwrapper, it will move the mouse to the category using actionchains from a method in seleniumwrapper and it will perform a click on it
    """ 
    @classmethod
    def setUpClass(cls):
        cls.driver = SeleniumWrapper("test_CreateOrder")
        cls.database = DatabaseWrapper("computers")
        cls.driver.openpage()
        cls.driver.move_mouse("Computers", "link_text")
        cls.driver.click("Software", "link_text")
    
    # This test will get info about the item, order it, input shipping details, set shipping method, payment info, method and and confirm the order
    def test_orderitem(self):
        # Adding an item to cart
        self.driver.click("Sound Forge Pro 11 (recurring)", "link_text")
        self.ItemName12 = self.driver.find_text("h1", "tag_name")
        self.Rentable = self.driver.find_if_elementAvailiable("rental-price", "class_name")
        self.DiscountForQuantity = self.driver.find_if_elementAvailiable("prices-table", "class_name")
        self.ManufacturerItem12 = self.driver.getmanufacturer(self.ItemName12, 2)
        self.StockItem12 = self.driver.find_text("stock-availability-value-12", "id")
        self.SkuItem12 = self.driver.find_text("sku-12", "id")
        self.PriceItem12 = self.driver.getintprice(self.driver.find_text("price-value-12", "class_name"))

        self.ModifyQuantity = self.driver.type_text("product_enteredQuantity_12", "id", "2")
        self.AddToCart = self.driver.click("add-to-cart-button-12", "id")
        
        # Ordering the item
        self.OpenCart = self.driver.click("shopping cart", "link_text")
        self.GiftWrap = self.driver.giftwrap("selected-checkout-attributes", "class_name")
        self.AcceptTerms = self.driver.click("termsofservice", "id")
        self.Checkout = self.driver.click("checkout", "id")
        self.CheckoutAsGuest = self.driver.click("body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.customer-blocks > div.new-wrapper.checkout-as-guest-or-register-block > div.buttons > button.button-1.checkout-as-guest-button", "css_selector")
        
        # Inputing Shipping Details
        self.firstname = self.driver.type_and_returntext("BillingNewAddress_FirstName", "id", "Andrei")
        self.lastname = self.driver.type_and_returntext("BillingNewAddress_LastName", "id", "Popescu")
        self.email = self.driver.type_and_returntext("BillingNewAddress_Email", "id", "fffff@gmail.com")
        self.company = self.driver.type_and_returntext("BillingNewAddress_Company", "id", "The Best Company")
        self.country = self.driver.select_and_returnfromdrp("BillingNewAddress_CountryId", "id", "Romania")
        self.city = self.driver.type_and_returntext("BillingNewAddress_City", "id", "Bucuresti")
        self.Address1 = self.driver.type_and_returntext("BillingNewAddress_Address1", "id", "Str Victoriei nr 25")
        self.Address2 = self.driver.type_and_returntext("BillingNewAddress_Address2", "id", "Str Victoriei nr 30")
        self.Zip = self.driver.type_and_returntext("BillingNewAddress_ZipPostalCode", "id", "45000")
        self.PhoneNumber = self.driver.type_and_returntext("BillingNewAddress_PhoneNumber", "id", "0700000000")
        self.continuebilling = self.driver.click("#billing-buttons-container > button.button-1.new-address-next-step-button", "css_selector")
        
        # Shipping Method
        self.shippingmethod = self.driver.click("shippingoption_1", "id")
        self.shippingmethodchoosed = self.driver.getshippingmethod(self.driver.find_text("#shipping-methods-form > ul > li:nth-child(2) > div.method-name > label", "css_selector"))
        self.continueshippingmethod = self.driver.click("#shipping-method-buttons-container > button", "css_selector")
        
        # Payment method
        self.paymethod = self.driver.click("paymentmethod_1", "id")
        self.continuepaymentmethod = self.driver.click("button-1 payment-method-next-step-button", "class_name")
        
        # Payment Informations
        self.Cardholder = self.driver.type_text("CardholderName", "id", "Andrei Popescu")
        self.CardNumber = self.driver.type_text("CardNumber", "id", "4465262311153726")
        self.ExpirationMonth = self.driver.select_fromdrp("ExpireMonth", "id", "5")
        self.ExpirationYear = self.driver.select_fromdrp("ExpireYear", "id", "2025")
        self.CardCode = self.driver.type_text("CardCode", "id", "3333")
        self.continuepaymentinformations = self.driver.click("#payment-info-buttons-container > button", "css_selector")

        # Confirm Order
        self.FinalQuantity = self.driver.getintquantity(self.driver.find_text("product-quantity", "class_name"))
        self.ConfirmOrder = self.driver.click("#confirm-order-buttons-container > button", "css_selector")
        self.OrderNumber = self.driver.getordernumber(self.driver.find_text("order-number", "class_name"))
        self.CompleteOrderContinue = self.driver.click("Click here", "partial_link_text")
        self.OrderStatus = self.driver.getorderstatus(self.driver.find_text("order-status", "class_name"))
        self.GettingTotal = self.driver.getintprice(self.driver.find_text("body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.section.totals > div.total-info > table > tbody > tr:nth-child(4) > td.cart-total-right > span > strong", "css_selector"))
        
        # create customer entry in the database using the following arguments: 
        # Name, Price, Rentable, Custom, DiscountForQuantity, Manufacturer, SKU, Quantity, Wrap
        self.database.create_customer_entry(self.ItemName12, self.PriceItem12, self.Rentable, "No", self.DiscountForQuantity, self.ManufacturerItem12, self.SkuItem12, self.FinalQuantity, self.GiftWrap)
        
        # Checking if the customer entry has been created in the database corectly using the same arguments as above
        self.checkcustomerentry = self.database.check_customer_entry(self.ItemName12, self.PriceItem12, self.Rentable, "No", self.DiscountForQuantity, self.ManufacturerItem12, self.SkuItem12, self.FinalQuantity, self.GiftWrap)
        
        # create customer shipping details in the database using the following arguments: 
        # fname, lname, email, Company, Country, city, Add1, Add2, postalcode, phone, fax, shipmethod, orderstatus, ordertotal, ordernumber
        self.database.add_customer_details(self.firstname, self.lastname, self.email, self.company, self.country, self.city, self.Address1, self.Address2, self.Zip, self.PhoneNumber, "", self.shippingmethodchoosed, self.OrderStatus, self.GettingTotal, self.OrderNumber)
        
        # Checking if the customer shipping details have been created in the database corectly using the same arguments as above
        self.checkcustomershipping = self.database.check_customer_details(self.firstname, self.lastname, self.email, self.company, self.country, self.city, self.Address1, self.Address2, self.Zip, self.PhoneNumber, "", self.shippingmethodchoosed, self.OrderStatus, self.GettingTotal, self.OrderNumber)
        
        # Test Validation Part to check if both checks on database worked as expected
        if self.checkcustomerentry == "No" and self.checkcustomershipping == "No":
            self.assertFalse(True, "Both customerentry and customershippingdetail checks failed")
        elif self.checkcustomerentry == "Yes" and self.checkcustomershipping == "No":
            self.assertFalse(True, "Customerentry passed the check but customershippingdetail has failed")
        elif self.checkcustomerentry == "No" and self.checkcustomershipping == "Yes":
            self.assertFalse(True, "Customerentry failed the check but customershippingdetail has passed")
        else:
            self.assertEqual(self.checkcustomerentry, self.checkcustomershipping, "Both CheckCustomerEntry and Checkcustomershipping informations have been checked and are present in the database")
        
    # TeardownClass will be used after all the tests in this class have been executed and quit the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.closebrowser()


if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\reports", report_name= "Test_CreateOrder", verbosity=2, combine_reports=True))
        