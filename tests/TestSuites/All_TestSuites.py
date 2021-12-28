import sys
import os
directory = os.path.abspath("..\\")
sys.path.append(directory)
import unittest
import HtmlTestRunner
from Computers.test_Desktops import Test_001_Desktops as Test_Desktops
from Computers.test_Notebooks import Test_002_Notebooks as Test_Notebooks
from Computers.test_Software import Test_003_Software as Test_Software
from Electronics.test_Camera import Test_004_Camera as Test_Camera
from Electronics.test_CellPhones import Test_005_CellPhones as Test_CellPhones
from Electronics.test_Others import Test_006_Others as Test_Others
from Apparel.test_Shoes import Test_007_Shoes as Test_Shoes
from Apparel.test_Clothing import Test_008_Clothing as Test_Clothing
from Apparel.test_Accessories import Test_009_Accessories as Test_Accessories
from test_DigitalDownloads import Test_010_DigitalDownloads as Test_DigitalDownloads
from test_Books import Test_011_Books as Test_Books
from test_Jewelry import Test_012_Jewelry as Test_Jewelry
from test_GiftCards import Test_013_GiftCards as Test_GiftCards
from test_CreateOrder import Test_014_CreateOrder as Test_CreateOrder

# Getting all the test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Desktops)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_Notebooks)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_Software)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Test_Camera)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Test_CellPhones)
tc6 = unittest.TestLoader().loadTestsFromTestCase(Test_Others)
tc7 = unittest.TestLoader().loadTestsFromTestCase(Test_Shoes)
tc8 = unittest.TestLoader().loadTestsFromTestCase(Test_Clothing)
tc9 = unittest.TestLoader().loadTestsFromTestCase(Test_Accessories)
tc10 = unittest.TestLoader().loadTestsFromTestCase(Test_DigitalDownloads)
tc11 = unittest.TestLoader().loadTestsFromTestCase(Test_Books)
tc12 = unittest.TestLoader().loadTestsFromTestCase(Test_Jewelry)
tc13 = unittest.TestLoader().loadTestsFromTestCase(Test_GiftCards)
tc14 = unittest.TestLoader().loadTestsFromTestCase(Test_CreateOrder)

# Run all test cases
suite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, tc11, tc12, tc13, tc14])
# unittest.TextTestRunner().run(all_tests)

testRunner = HtmlTestRunner.HTMLTestRunner(output="..\\..\\reports", report_name= "Report", verbosity=2, combine_reports=True)
testRunner.run(suite)
