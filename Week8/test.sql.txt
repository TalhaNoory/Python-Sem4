-- MySQL dump 10.13  Distrib 8.0.17, for Linux (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Article2Imgs`
--

DROP TABLE IF EXISTS `Article2Imgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Article2Imgs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `initiatedDate` date NOT NULL,
  `article` int(11) NOT NULL,
  `image` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `article` (`article`),
  KEY `image` (`image`),
  CONSTRAINT `Article2Imgs_ibfk_1` FOREIGN KEY (`article`) REFERENCES `Articles` (`id`),
  CONSTRAINT `Article2Imgs_ibfk_2` FOREIGN KEY (`image`) REFERENCES `Images` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Article2Imgs`
--

LOCK TABLES `Article2Imgs` WRITE;
/*!40000 ALTER TABLE `Article2Imgs` DISABLE KEYS */;
INSERT INTO `Article2Imgs` VALUES (1,'2018-05-23',1,1),(2,'2018-05-23',2,2),(3,'2018-05-23',3,3),(4,'2018-05-23',4,4),(5,'2018-05-23',5,5),(6,'2018-05-23',6,6),(7,'2018-05-23',7,7),(8,'2018-05-23',8,8),(9,'2018-05-23',9,9);
/*!40000 ALTER TABLE `Article2Imgs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Articles`
--

DROP TABLE IF EXISTS `Articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `caption` varchar(200) NOT NULL,
  `text` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Articles`
--

LOCK TABLES `Articles` WRITE;
/*!40000 ALTER TABLE `Articles` DISABLE KEYS */;
INSERT INTO `Articles` VALUES (1,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(2,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(3,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(4,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(5,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(6,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(7,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(8,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf'),(9,'art1','cap1','ssdf sf sdf sdf s sdf gsf sdf sf');
/*!40000 ALTER TABLE `Articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CUSTOMER` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `ACCOUNT` double DEFAULT NULL,
  `ADDRESS` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
INSERT INTO `CUSTOMER` VALUES (1,90000,'Rolighedsvej 13','Henriette Halvorsen'),(2,43000,'Rolighedsvej 18','Halbert Hilleman');
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cities`
--

DROP TABLE IF EXISTS `Cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cities`
--

LOCK TABLES `Cities` WRITE;
/*!40000 ALTER TABLE `Cities` DISABLE KEYS */;
INSERT INTO `Cities` VALUES (1,'St. Petersburg'),(2,'Munich'),(3,'St. Petersburg'),(4,'Munich'),(5,'St. Petersburg'),(6,'Munich'),(7,'St. Petersburg'),(8,'Munich'),(9,'St. Petersburg'),(10,'Munich'),(11,'St. Petersburg'),(12,'Munich'),(13,'St. Petersburg'),(14,'Munich'),(15,'St. Petersburg'),(16,'Munich');
/*!40000 ALTER TABLE `Cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `city` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `city` (`city`),
  KEY `Customers_name` (`name`),
  CONSTRAINT `Customers_ibfk_1` FOREIGN KEY (`city`) REFERENCES `Cities` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'a',15,5),(2,'b',15,27),(3,'c',16,42);
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Images`
--

DROP TABLE IF EXISTS `Images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `path` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Images`
--

LOCK TABLES `Images` WRITE;
/*!40000 ALTER TABLE `Images` DISABLE KEYS */;
INSERT INTO `Images` VALUES (1,'img1','path1'),(2,'img1','path1'),(3,'img1','path1'),(4,'img1','path1'),(5,'img1','path1'),(6,'img1','path1'),(7,'img1','path1'),(8,'img1','path1'),(9,'img1','path1');
/*!40000 ALTER TABLE `Images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `shippingdate` timestamp NULL DEFAULT NULL,
  `Customers_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Orders_Customers1_idx` (`Customers_id`),
  CONSTRAINT `fk_Orders_Customers1` FOREIGN KEY (`Customers_id`) REFERENCES `Customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PERSON`
--

DROP TABLE IF EXISTS `PERSON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PERSON` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `CREATIONDATE` datetime DEFAULT NULL,
  `DATEOFBIRTH` date DEFAULT NULL,
  `HOBBIES` longblob,
  `MEDAL` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PERSON`
--

LOCK TABLES `PERSON` WRITE;
/*!40000 ALTER TABLE `PERSON` DISABLE KEYS */;
/*!40000 ALTER TABLE `PERSON` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PERSONCOMPLEX`
--

DROP TABLE IF EXISTS `PERSONCOMPLEX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PERSONCOMPLEX` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `CREATIONDATE` datetime DEFAULT NULL,
  `DATEOFBIRTH` date DEFAULT NULL,
  `MEDAL` varchar(255) DEFAULT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PERSONCOMPLEX`
--

LOCK TABLES `PERSONCOMPLEX` WRITE;
/*!40000 ALTER TABLE `PERSONCOMPLEX` DISABLE KEYS */;
/*!40000 ALTER TABLE `PERSONCOMPLEX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PersonComplex_HOBBIES`
--

DROP TABLE IF EXISTS `PersonComplex_HOBBIES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PersonComplex_HOBBIES` (
  `PersonComplex_ID` bigint(20) DEFAULT NULL,
  `HOBBIES` varchar(255) DEFAULT NULL,
  KEY `FK_PersonComplex_HOBBIES_PersonComplex_ID` (`PersonComplex_ID`),
  CONSTRAINT `FK_PersonComplex_HOBBIES_PersonComplex_ID` FOREIGN KEY (`PersonComplex_ID`) REFERENCES `PERSONCOMPLEX` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PersonComplex_HOBBIES`
--

LOCK TABLES `PersonComplex_HOBBIES` WRITE;
/*!40000 ALTER TABLE `PersonComplex_HOBBIES` DISABLE KEYS */;
/*!40000 ALTER TABLE `PersonComplex_HOBBIES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PersonComplex_PHONES`
--

DROP TABLE IF EXISTS `PersonComplex_PHONES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PersonComplex_PHONES` (
  `PersonComplex_ID` bigint(20) DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `PHONE` varchar(255) DEFAULT NULL,
  KEY `FK_PersonComplex_PHONES_PersonComplex_ID` (`PersonComplex_ID`),
  CONSTRAINT `FK_PersonComplex_PHONES_PersonComplex_ID` FOREIGN KEY (`PersonComplex_ID`) REFERENCES `PERSONCOMPLEX` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PersonComplex_PHONES`
--

LOCK TABLES `PersonComplex_PHONES` WRITE;
/*!40000 ALTER TABLE `PersonComplex_PHONES` DISABLE KEYS */;
/*!40000 ALTER TABLE `PersonComplex_PHONES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEQUENCE`
--

DROP TABLE IF EXISTS `SEQUENCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SEQUENCE` (
  `SEQ_NAME` varchar(50) NOT NULL,
  `SEQ_COUNT` decimal(38,0) DEFAULT NULL,
  PRIMARY KEY (`SEQ_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEQUENCE`
--

LOCK TABLES `SEQUENCE` WRITE;
/*!40000 ALTER TABLE `SEQUENCE` DISABLE KEYS */;
INSERT INTO `SEQUENCE` VALUES ('SEQ_GEN',150);
/*!40000 ALTER TABLE `SEQUENCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'demouser','test@mail.com','test123'),(2,'demouser','test@mail.com','test123'),(3,'demouser','test@mail.com','test123'),(4,'demouser','test@mail.com','test123'),(5,'demouser','test@mail.com','test123'),(6,'demouser','test@mail.com','test123'),(7,'demouser','test@mail.com','test123'),(8,'demouser','test@mail.com','test123'),(9,'demouser','test@mail.com','test123'),(10,'demouser','test@mail.com','test123');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `make` text,
  `model` text,
  `year` bigint(20) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES ('vw','up',2018,123000),('audi','a6',2011,85000),('citroen','c3',2019,143000);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `personId` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`personId`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (51,'Holger','Danske'),(101,'Henriette','Dellerup'),(102,'Kasandra','Black'),(103,'Kunta','Kinte');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone` (
  `phoneId` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `personId` int(11) NOT NULL,
  PRIMARY KEY (`phoneId`,`personId`),
  KEY `fk_phone_person_idx` (`personId`),
  CONSTRAINT `fk_phone_person` FOREIGN KEY (`personId`) REFERENCES `person` (`personId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pythondemo`
--

DROP TABLE IF EXISTS `pythondemo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pythondemo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `startdate` datetime DEFAULT NULL,
  `enddate` timestamp NULL DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pythondemo`
--

LOCK TABLES `pythondemo` WRITE;
/*!40000 ALTER TABLE `pythondemo` DISABLE KEYS */;
INSERT INTO `pythondemo` VALUES (1,'Henny','Petersen','2002-02-02 00:00:00','2002-02-03 23:00:00','23000'),(3,'Hassan','Hassani','2018-07-07 00:00:00','2020-11-12 23:00:00','43000'),(4,'Hanne','Hansen','2002-04-03 00:00:00',NULL,'94446'),(5,'Jesper','Fårekylling','2002-04-03 00:00:00','2018-07-06 22:00:00','23000'),(6,'Janni','Spiser','2011-05-23 00:00:00',NULL,'180149'),(7,'aa','bb','2003-04-04 00:00:00','2003-05-05 00:00:00','31400'),(9,'Helga','Juhlborg','2003-01-17 00:00:00','2004-04-11 00:00:00','34100'),(10,'Helga','Juhlborg','2003-01-17 00:00:00','2004-04-11 00:00:00','34100'),(11,'Helga','Juhlborg','2003-01-17 00:00:00','2004-04-11 00:00:00','34100'),(12,'Ulrik','Volborg','2003-03-03 00:00:00','2005-08-20 00:00:00','21000'),(13,'Ulla','Willman','2001-05-04 00:00:00','2005-12-24 00:00:00','32000'),(14,'Ulfred','Valberg','2001-01-04 00:00:00','2006-10-30 00:00:00','43000');
/*!40000 ALTER TABLE `pythondemo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-14  9:51:16
