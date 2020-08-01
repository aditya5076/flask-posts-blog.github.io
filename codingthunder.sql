-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2020 at 12:03 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `srno` int(15) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`srno`, `name`, `email`, `phone_number`, `message`, `date`) VALUES
(1, 'hash', 'hash@hashgamil.com', '1231234561', 'this is first post throught phpmyadmin', '2020-07-30 13:22:26'),
(2, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'ab mat aa yar', '2020-07-30 13:50:20'),
(3, 'ash', 'ash@gmail.com', '6766767689', 'this', '2020-07-30 14:42:55'),
(4, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'ljdl', '2020-07-30 14:45:38'),
(5, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'jd;d', '2020-07-30 14:46:58'),
(6, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'jd;d', '2020-07-30 14:58:07'),
(7, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'jd;d', '2020-07-30 15:00:59'),
(8, 'Aditya Narveker', 'adinarvekar8454@gmail.com', '09136399610', 'jlj;k\'', '2020-07-30 15:01:21'),
(9, 'k;sk;', 'billu@gmail.com', '1234123412', 'this is us', '2020-07-30 15:05:28'),
(10, 'k;sk;', 'billu@gmail.com', '1234123412', 'this is us', '2020-07-30 15:24:52');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `srno` int(15) NOT NULL,
  `title` varchar(25) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `tag_line` text NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`srno`, `title`, `slug`, `tag_line`, `content`, `img_file`, `date`) VALUES
(1, 'this is my post', 'am excited', '            Lorem ipsum dolor sit amet consectetur adipisicing elit. Totam, excepturi.', 'am excited', 'about-bg.jpg', '2020-07-30 15:10:46'),
(3, 'stocks', 'moneycontrol', 'Agri Weekly Report: Motilal Oswal\r\nAccording to Motilal Oswal, NCDEX Soya bean ', 'Agri Weekly Report: Motilal Oswal\r\nAccording to Motilal Oswal, NCDEX Soya bean has been trading in consolidation zone at the moment and a break below Rs.3740 level is likely to result in the continuation of previous trend (Bearish).', 'home-bg.jpg', '2020-07-31 15:11:08'),
(4, 'covid-19', 'covid', '\r\nMost people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.', 'The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces.\r\nYou can be infected by breathing', 'about-bg.jpg', '2020-07-31 15:12:54'),
(5, 'pagination', 'page', 'What is pagination?', 'This module helps dividing large lists of items into pages. The user is shown one page at a time and\r\ncan navigate to other pages. Imagine you are offering a company phonebook and let the user search\r\nthe entries. If the search result contains 23 entries ', 'about-bg.jpg', '2020-07-31 15:20:42');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `srno` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `srno` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
