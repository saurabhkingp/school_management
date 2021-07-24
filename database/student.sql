-- phpMyAdmin SQL Dump
-- version 5.1.1
-- http://www.phpmyadmin.net
-- 
-- Host: localhost
-- Generation Time: Mar 04, 2021 at 03:47 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.21
-- 
-- Database: `student`
-- 
CREATE DATABASE `student` DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci;
USE `student`;

-- --------------------------------------------------------

-- 
-- Table structure for table `admission`
-- 

CREATE TABLE `admission` (
  `id` int(3) NOT NULL auto_increment,
  `name` varchar(30) collate latin1_general_ci NOT NULL,
  `standard` varchar(10) collate latin1_general_ci NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=2 ;

-- 
-- Dumping data for table `admission`
-- 

INSERT INTO `admission` VALUES (1, 'sankhat ravi', 'EIGHT');

-- --------------------------------------------------------

-- 
-- Table structure for table `staff`
-- 

CREATE TABLE `staff` (
  `id` int(3) NOT NULL auto_increment,
  `name` varchar(25) collate latin1_general_ci NOT NULL,
  `designation` varchar(10) collate latin1_general_ci NOT NULL,
  `qualification` varchar(15) collate latin1_general_ci NOT NULL,
  `experience` int(3) NOT NULL,
  `contact` varchar(10) collate latin1_general_ci NOT NULL,
  `email` varchar(35) collate latin1_general_ci NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=2 ;

-- 
-- Dumping data for table `staff`
-- 

INSERT INTO `staff` VALUES (1, 'sankhat devraj', 'teacher', 'b.a.b.ed', 2, '9723888910', 'devraj_sankhat34@yahoo.com');

-- --------------------------------------------------------

-- 
-- Table structure for table `standard`
-- 

CREATE TABLE `standard` (
  `id` int(3) NOT NULL auto_increment,
  `standard_name` varchar(30) collate latin1_general_ci NOT NULL,
  `intake` varchar(4) collate latin1_general_ci NOT NULL,
  `fees` varchar(5) collate latin1_general_ci NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=2 ;

-- 
-- Dumping data for table `standard`
-- 

INSERT INTO `standard` VALUES (1, 'one', '30', '3000');
INSERT INTO `standard` VALUES (2, 'two', '30', '4000');
