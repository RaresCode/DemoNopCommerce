CREATE DATABASE  IF NOT EXISTS `demonopcommerce` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `demonopcommerce`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: demonopcommerce
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `apparel`
--

DROP TABLE IF EXISTS `apparel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apparel` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Availability` enum('In stock','Out of stock','Available in 2-4 days') NOT NULL,
  `Price` float DEFAULT NULL,
  `Manufacturer` varchar(20) DEFAULT NULL,
  `SKU` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apparel`
--

LOCK TABLES `apparel` WRITE;
/*!40000 ALTER TABLE `apparel` DISABLE KEYS */;
INSERT INTO `apparel` VALUES (1,'Nike Floral Roshe Customized Running Shoes','In stock',40,'Nike','NK_FRC_RS'),(2,'adidas Consortium Campus 80s Running Shoes','In stock',27.56,'adidas','AD_C80_RS'),(3,'Nike SB Zoom Stefan Janoski \"Medium Mint\"','In stock',30,'Nike','NK_ZSJ_MM'),(4,'Nike Tailwind Loose Short-Sleeve Running Shirt','In stock',15,'Nike','NK_TLS_RS'),(5,'Oversized Women T-Shirt','In stock',24,NULL,'WM_OVR_TS'),(6,'Custom T-Shirt','In stock',15,NULL,'CS_TSHIRT'),(7,'Levi\'s 511 Jeans','In stock',43.5,'Levi\'s','LV_511_JN'),(8,'Obey Propaganda Hat','In stock',30,'Obey','OB_HAT_PR'),(9,'Reversible Horseferry Check Belt','Available in 2-4 days',45,NULL,'RH_CHK_BL'),(10,'Ray Ban Aviator Sunglasses','In stock',25,'Ray Ban','RB_AVR_SG');
/*!40000 ALTER TABLE `apparel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Availability` enum('In stock','Out of stock') NOT NULL,
  `Price` int NOT NULL,
  `SKU` varchar(30) NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Fahrenheit 451 by Ray Bradbury','In stock',27,'FR_451_RB'),(2,'First Prize Pies','In stock',51,'FIRST_PRP'),(3,'Pride and Prejudice','In stock',24,'PRIDE_PRJ');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `computers`
--

DROP TABLE IF EXISTS `computers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `computers` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Availability` enum('In stock','Out of stock') NOT NULL,
  `Price` float NOT NULL,
  `Manufacturer` varchar(30) DEFAULT NULL,
  `SKU` varchar(30) NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computers`
--

LOCK TABLES `computers` WRITE;
/*!40000 ALTER TABLE `computers` DISABLE KEYS */;
INSERT INTO `computers` VALUES (1,'Lenovo IdeaCentre 600 All-in-One PC','In stock',500,'Lenovo','LE_IC_600'),(2,'Digital Storm VANQUISH 3 Custom Performance PC','In stock',1259,'Digital Storm','DS_VA3_PC'),(3,'Build your own computer','In stock',1200,NULL,'COMP_CUST'),(4,'Apple MacBook Pro 13-inch','In stock',1800,'Apple','AP_MBP_13'),(5,'Asus N551JK-XO076H Laptop','In stock',1500,'Asus','AS_551_LP'),(6,'Samsung Series 9 NP900X4C Premium Ultrabook','In stock',1590,'Samsung','SM_900_PU'),(7,'HP Spectre XT Pro UltraBook','In stock',1350,'HP','HP_SPX_UB'),(8,'HP Envy 6-1180ca 15.6-Inch Sleekbook','In stock',1460,'HP','HP_ESB_15'),(9,'Lenovo Thinkpad X1 Carbon Laptop','In stock',1360,'Lenovo','LE_TX1_CL'),(10,'Adobe Photoshop CS4','Out of stock',75,'Adobe','AD_CS4_PH'),(11,'Windows 8 Pro','In stock',65,'Microsoft','MS_WIN_8P'),(12,'Sound Forge Pro 11 (recurring)','In stock',54.99,'Sound Forge','SF_PRO_11');
/*!40000 ALTER TABLE `computers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerinfo`
--

DROP TABLE IF EXISTS `customerinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customerinfo` (
  `TableID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Company` varchar(50) DEFAULT NULL,
  `Country` varchar(50) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Address1` varchar(50) NOT NULL,
  `Address2` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) NOT NULL,
  `PhoneNumber` varchar(50) NOT NULL,
  `FaxNumber` varchar(50) DEFAULT NULL,
  `ShippingMethod` enum('Ground','Next Day Air','2nd Day Air') DEFAULT NULL,
  `OrderStatus` enum('Shipped','Pending','canceled','delivered','returned') DEFAULT NULL,
  `OrderTotal` float NOT NULL,
  `OrderNumber` int NOT NULL,
  `CustomerID` int NOT NULL,
  PRIMARY KEY (`TableID`),
  KEY `Customerid_idx` (`CustomerID`),
  CONSTRAINT `customerid` FOREIGN KEY (`CustomerID`) REFERENCES `customers` (`ID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerinfo`
--

LOCK TABLES `customerinfo` WRITE;
/*!40000 ALTER TABLE `customerinfo` DISABLE KEYS */;
INSERT INTO `customerinfo` VALUES (1,'Andrei','Popescu','fffff@gmail.com','The Best Company','Romania','Bucuresti','Str Victoriei nr 25','Str Victoriei nr 30','45000','0700000000','','Next Day Air','Pending',109.98,1048,1);
/*!40000 ALTER TABLE `customerinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ItemName` varchar(100) NOT NULL,
  `ItemPrice` float NOT NULL,
  `ItemRentable` enum('Yes','No') DEFAULT NULL,
  `ItemCustom` enum('Yes','No') DEFAULT NULL,
  `ItemDiscountForQuantity` enum('Yes','No') DEFAULT NULL,
  `ItemManufacturer` varchar(30) DEFAULT NULL,
  `ItemSKU` varchar(30) NOT NULL,
  `ItemQuantity` int DEFAULT '1',
  `GiftWrap` enum('Yes','No') DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Sound Forge Pro 11 (recurring)',54.99,'No','No','No','Sound Forge','SF_PRO_11',2,'No');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `digitaldownloads`
--

DROP TABLE IF EXISTS `digitaldownloads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `digitaldownloads` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Price` float NOT NULL,
  `SKU` varchar(30) NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `digitaldownloads`
--

LOCK TABLES `digitaldownloads` WRITE;
/*!40000 ALTER TABLE `digitaldownloads` DISABLE KEYS */;
INSERT INTO `digitaldownloads` VALUES (1,'Night Visions',2.8,'NIGHT_VSN'),(4,'If You Wait (donation)',0.5,'IF_YOU_WT'),(5,'Science & Faith',0.5,'SCI_FAITH');
/*!40000 ALTER TABLE `digitaldownloads` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `electronics`
--

DROP TABLE IF EXISTS `electronics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `electronics` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Availability` enum('In stock','Out of stock') NOT NULL,
  `PRICE` float DEFAULT NULL,
  `Manufacturer` varchar(20) DEFAULT NULL,
  `SKU` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `electronics`
--

LOCK TABLES `electronics` WRITE;
/*!40000 ALTER TABLE `electronics` DISABLE KEYS */;
INSERT INTO `electronics` VALUES (1,'Nikon D5500 DSLR','Out of stock',NULL,'Nikon',NULL),(2,'Leica T Mirrorless Digital Camera','In stock',530,'Leica','LT_MIR_DC'),(3,'Apple iCam','Out of stock',1300,'Apple','APPLE_CAM'),(4,'HTC One M8 Android L 5.0 Lollipop','In stock',245,'HTC','M8_HTC_5L'),(5,'HTC One Mini Blue','In stock',100,'HTC','OM_HTC_BL'),(6,'Nokia Lumia 1020','In stock',349,'Nokia','N_1020_LU'),(7,'Beats Pill 2.0 Wireless Speaker','In stock',79.99,'Beats Pill','BP_20_WSP'),(8,'Universal 7-8 Inch Tablet Cover','In stock',39,NULL,'TC_78I_UN'),(9,'Portable Sound Speakers','In stock',37,NULL,'PT_SPK_SN'),(16,'Nikon D5500 DSLR - Black','In stock',670,'Nikon','N5500DS_B'),(17,'Nikon D5500 DSLR - Red','In stock',630,'Nikon','N5500DS_R');
/*!40000 ALTER TABLE `electronics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `giftcards`
--

DROP TABLE IF EXISTS `giftcards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `giftcards` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Price` int NOT NULL,
  `SKU` varchar(30) NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `giftcards`
--

LOCK TABLES `giftcards` WRITE;
/*!40000 ALTER TABLE `giftcards` DISABLE KEYS */;
INSERT INTO `giftcards` VALUES (1,'$25 Virtual Gift Card',25,'VG_CR_025'),(2,'$50 Physical Gift Card',50,'PG_CR_050'),(3,'$100 Physical Gift Card',100,'PG_CR_100');
/*!40000 ALTER TABLE `giftcards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jewelry`
--

DROP TABLE IF EXISTS `jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jewelry` (
  `ItemID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Availability` enum('In stock','Out of stock') NOT NULL,
  `Price` int NOT NULL,
  `Rentable` enum('Yes','No') DEFAULT NULL,
  `SKU` varchar(30) NOT NULL,
  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jewelry`
--

LOCK TABLES `jewelry` WRITE;
/*!40000 ALTER TABLE `jewelry` DISABLE KEYS */;
INSERT INTO `jewelry` VALUES (1,'Elegant Gemstone Necklace (rental)','In stock',30,'Yes','EG_GEM_NL'),(2,'Flower Girl Bracelet','In stock',360,'No','FL_GIRL_B'),(3,'Vintage Style Engagement Ring','In stock',2100,'No','VS_ENG_RN');
/*!40000 ALTER TABLE `jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'demonopcommerce'
--
/*!50003 DROP FUNCTION IF EXISTS `checklastcustomeraddress` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `checklastcustomeraddress`(
fname varchar(50),
lname varchar(50),
mail varchar(50),
Comp varchar(50), 
Countr varchar(50), 
cy varchar(100), 
Add1 varchar(50), 
Add2 varchar(50), 
postalcode varchar(50), 
phone varchar(50), 
fax varchar(50), 
shipmethod enum('Ground','Next Day Air','2nd Day Air'), 
status enum('Shipped','Pending','canceled','delivered','returned'), 
total float, 
number int) RETURNS varchar(20) CHARSET utf8mb4
    READS SQL DATA
begin
	DECLARE Result VARCHAR(20);
	DECLARE custid INT;
    DECLARE lastfName varchar(50);
    DECLARE lastlname varchar(50);
    DECLARE lastemail varchar(50);
    DECLARE lastcompany varchar(50);
    DECLARE lastcountry varchar(50);
    DECLARE lastcity varchar(100);
    DECLARE lastaddress1 varchar(50);
    DECLARE lastaddress2 varchar(50);
	DECLARE lastpostalcode varchar(50);
    DECLARE lastphonenumber varchar(50);
    DECLARE lastfax varchar(50);
    DECLARE lastshippingmethod enum('Ground','Next Day Air','2nd Day Air');
    DECLARE lastorderstatus enum('Shipped','Pending','canceled','delivered','returned');
    DECLARE lastordertotal float;
    DECLARE lastordernumber int;
	SET custid = 0;
	SELECT MAX(TableID) INTO custid FROM customerinfo;
	SELECT FirstName, LastName, Email, Company, Country, City, Address1, Address2, Zip, PhoneNumber, FaxNumber, ShippingMethod, OrderStatus, OrderTotal, OrderNumber INTO
    lastfName, lastlname, lastemail, lastcompany, lastcountry, lastcity, lastaddress1, lastaddress2, lastpostalcode, lastphonenumber, lastfax, lastshippingmethod, lastorderstatus, lastordertotal, lastordernumber
    FROM customerinfo WHERE TableID = custid;
    IF (fname=lastfName and lname=lastlname and mail=lastemail and Comp=lastcompany and Countr=lastcountry and cy=lastcity and Add1=lastaddress1 and Add2=lastaddress2
    and postalcode=lastpostalcode and phone=lastphonenumber and fax=lastfax and shipmethod=lastshippingmethod and status=lastorderstatus and total=lastordertotal
    and number=lastordernumber) THEN
		SET Result = 'Yes';
	ELSE
		SET Result = 'No';
	END IF;
	return Result;
    
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `checklastcustomerinfo` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `checklastcustomerinfo`(
Name varchar(100), 
Price float, 
Rentable enum('Yes','No'),
Custom enum('Yes','No'), 
DiscountForQuantity enum('Yes','No'), 
Manufacturer varchar(30),
SKU varchar(30), 
Quantity INT, 
Wrap enum('Yes','No')) RETURNS varchar(20) CHARSET utf8mb4
    READS SQL DATA
begin
	DECLARE Result VARCHAR(20);
	DECLARE customerid INT;
    DECLARE lastItemName Varchar(100);
    DECLARE lastItemPrice float;
    DECLARE lastItemRentable enum('Yes','No');
    DECLARE lastItemCustom enum('Yes','No');
    DECLARE lastItemDiscountForQuantity enum('Yes','No');
    DECLARE lastItemManufacturer varchar(30);
    DECLARE lastItemSKU varchar(30);
	DECLARE lastItemQuantity int;
    DECLARE lastGiftWrap enum('Yes','No');
    SET customerid = 0;
	SELECT MAX(ID) INTO customerid FROM customers;
	SELECT ItemName, ItemPrice, ItemRentable, ItemCustom, ItemDiscountForQuantity, ItemManufacturer, ItemSKU, ItemQuantity, GiftWrap INTO
    lastItemName, lastItemPrice, lastItemRentable, lastItemCustom, lastItemDiscountForQuantity, lastItemManufacturer, lastItemSKU, lastItemQuantity, lastGiftWrap
    FROM customers WHERE ID = customerid;
    IF (Name=lastItemName and Price=lastItemPrice and Rentable=lastItemRentable and Custom=lastItemCustom and DiscountForQuantity=lastItemDiscountForQuantity and Manufacturer=lastItemManufacturer
    and SKU=lastItemSKU and Quantity=lastItemQuantity and Wrap=lastGiftWrap) THEN
		SET Result = 'Yes';
	ELSE
		SET Result = 'No';
	END IF;
	return Result;
    
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `AddCustomerDetails` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddCustomerDetails`(
IN fname varchar(50),
IN lname varchar(50),
IN mail varchar(50),
IN Comp varchar(50), 
IN Countr varchar(50), 
IN cy varchar(100), 
IN Add1 varchar(50), 
IN Add2 varchar(50), 
IN postalcode varchar(50), 
IN phone varchar(50), 
IN fax varchar(50), 
IN shipmethod enum('Ground','Next Day Air','2nd Day Air'), 
IN status enum('Shipped','Pending','canceled','delivered','returned'), 
IN total float, 
IN number int)
begin
	DECLARE custid INT;
    SET custid = 0;
    SELECT MAX(ID) INTO custid FROM customers;
	INSERT INTO customerinfo (FirstName, LastName, Email, Company, Country, City, Address1, Address2, Zip, PhoneNumber, FaxNumber, ShippingMethod, OrderStatus, OrderTotal, OrderNumber, CustomerID)
    VALUES (fname, lname, mail, Comp, Countr, cy, Add1, Add2, postalcode, phone, fax, shipmethod, status, total, number, custid);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CreateCustomerEntry` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `CreateCustomerEntry`(IN Name varchar(100), IN Price float, IN Rentable enum('Yes','No'),
IN Custom enum('Yes','No'), IN DiscountForQuantity enum('Yes','No'), IN Manufacturer varchar(30),
IN SKU varchar(30), IN Quantity INT, IN Wrap enum('Yes','No'))
begin
	INSERT INTO customers (ItemName, ItemPrice, ItemRentable, ItemCustom, ItemDiscountForQuantity, ItemManufacturer, ItemSKU, ItemQuantity, GiftWrap)
    VALUES (Name, Price, Rentable, Custom, DiscountForQuantity, Manufacturer, SKU, Quantity, Wrap);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-28 23:08:53
