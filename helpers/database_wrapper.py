import mysql.connector

"""
Database wrapper class is used to store all the actions related to the database then call them when required to get the expected results
"""

class DatabaseWrapper():
    # Try to establish a connection with the database, setting up the cursor for executing sql querries and categoryname which it's used to select the tablename from the database
    def __init__(self, CategoryName):
        self.CategoryName = CategoryName
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="demonopcommerce"
            )
            self.mycursor = self.mydb.cursor(buffered=True)
        except mysql.connector.Error as err:
            print(f"Error during the connection: {err}")
    
    # Get a specific single result from the database to be used in comparing with the result got from the webpage, it takes columnname and sku as arguments and returns the value
    def get_from_database(self, ColumnName, SKU):
        self.mycursor.execute(f"SELECT {ColumnName} FROM {self.CategoryName} WHERE SKU = '{SKU}'")
        self.myresult = self.mycursor.fetchone()
        if type(self.myresult[0]) == str:
            return self.myresult[0]
        # Here if the type of the result it's not ending with .0 it returns a float otherwise int, for example in case of the price being 27.55 it will return it as float and if 27.0 as int
        elif type(self.myresult[0]) == float:
            if str(self.myresult[0]).endswith(".0"):
                return int(self.myresult[0])
            else:
                return float(self.myresult[0])
        else:
            return int(self.myresult[0])
    
    # This will execute the store procedure to create a customer entry in the customers table using the arguments passed to it and save it
    def create_customer_entry(self, Name, Price, Rentable, Custom, DiscountForQuantity, Manufacturer, SKU, Quantity, Wrap):
        self.mycursor.execute(f"call CreateCustomerEntry('{Name}', '{Price}', '{Rentable}', '{Custom}', '{DiscountForQuantity}', '{Manufacturer}', '{SKU}', '{Quantity}', '{Wrap}')")
        self.mydb.commit()
        
    """
    This sql function will check if the last inserted values in the database have been properly saved
    compare them with the same input as used in the create_customer_entry method and return "Yes" if is the same otherwise "No"
    """
    def check_customer_entry(self, Name, Price, Rentable, Custom, DiscountForQuantity, Manufacturer, SKU, Quantity, Wrap):
        self.mycursor.execute(f"SELECT checklastcustomerinfo('{Name}', '{Price}', '{Rentable}', '{Custom}', '{DiscountForQuantity}', '{Manufacturer}', '{SKU}', '{Quantity}', '{Wrap}') from customers")
        self.customerentryresult = self.mycursor.fetchone()
        print(self.customerentryresult[0])
        return self.customerentryresult[0]
    
    # This will execute the store procedure to create an entry with the details about shipping in the customerinfo table using the arguments passed and save it
    def add_customer_details(self, fname, lname, email, Company, Country, city, Add1, Add2, postalcode, phone, fax, shipmethod, orderstatus, ordertotal, ordernumber):
        self.mycursor.execute(f"call AddCustomerDetails('{fname}', '{lname}', '{email}', '{Company}', '{Country}', '{city}', '{Add1}', '{Add2}', '{postalcode}', '{phone}', '{fax}', '{shipmethod}', '{orderstatus}', '{ordertotal}', '{ordernumber}')")
        self.mydb.commit()
    
    """
    This sql function will check if the last inserted values in the database have been properly saved
    compare them with the same input as used in the add_customer_details method and return "Yes" if is the same otherwise "No"
    """
    def check_customer_details(self, fname, lname, email, Company, Country, city, Add1, Add2, postalcode, phone, fax, shipmethod, orderstatus, ordertotal, ordernumber):
        self.mycursor.execute(f"SELECT checklastcustomeraddress('{fname}', '{lname}', '{email}', '{Company}', '{Country}', '{city}', '{Add1}', '{Add2}', '{postalcode}', '{phone}', '{fax}', '{shipmethod}', '{orderstatus}', '{ordertotal}', '{ordernumber}') from customerinfo")
        self.customerdetailsresult = self.mycursor.fetchone()
        print(self.customerdetailsresult[0])
        return self.customerdetailsresult[0]
        