-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 07, 2024 at 09:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `news`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(255) NOT NULL,
  `admin_email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `admin_email`, `password`) VALUES
(1, 'Jaskaran@gmail.com', 'jas123456');

-- --------------------------------------------------------

--
-- Table structure for table `news`
--

CREATE TABLE `news` (
  `id` int(12) NOT NULL,
  `user_id` int(12) NOT NULL,
  `news_img` varchar(100) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `author_name` text NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `news`
--

INSERT INTO `news` (`id`, `user_id`, `news_img`, `title`, `content`, `author_name`, `date`) VALUES
(1, 1, 'https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/5_mon/img_1722835909477_200.jpg?', 'SC upholds L-G\'s power to appoint MCD aldermen without Delhi govt\'s aid', 'The Supreme Court on Monday ruled that Delhi\'s Lieutenant Governor can nominate aldermen in civic body MCD without Delhi government\'s aid and advice. This is a statutory power, not an executive power, the bench stated. It upheld Lieutenant Governor VK Saxena\'s move to nominate 10 aldermen without the AAP-led government\'s aid. The MCD has 250 elected and 10 nominated members.', 'Nidhi Sinha', 'Monday, 05 August, 2024'),
(2, 2, 'https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/5_mon/img_1722835909477_200.jpg?', 'SC upholds L-G\'s power to appoint MCD aldermen without Delhi govt\'s aid', 'The Supreme Court on Monday ruled that Delhi\'s Lieutenant Governor can nominate aldermen in civic body MCD without Delhi government\'s aid and advice. This is a statutory power, not an executive power, the bench stated. It upheld Lieutenant Governor VK Saxena\'s move to nominate 10 aldermen without the AAP-led government\'s aid. The MCD has 250 elected and 10 nominated members.', 'Nidhi Sinha', 'Monday, 05 August, 2024'),
(3, 1, 'https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/5_mon/img_1722836007889_561.jpg?', 'Weather was out of control: Shooter Moudgil on missing medal round', 'Speaking about not reaching medal round in women\'s 50m Rifle 3 Positions event in ongoing Paris Olympics, India shooter Anjum Moudgil said that weather was a \"bit out of control\". She stated sunlight and darkness don\'t cause any issues and \"mainly, it is about the wind\". Moudgil\'s total score was 584(26x), five points short required to qualify for medal round.', 'Bhuvnesh Ojha', 'Monday, 05 August, 2024'),
(4, 1, 'https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/6_tue/img_1722934352926_667.jpg?', 'People steal undergarments, blouses from Sheikh Hasina\'s official residence in Bangladesh', 'Protestors were seen stealing undergarments and blouses from former Bangladesh PM Sheikh Hasina\'s official residence after they stormed the building. Hasina, who left the country and landed in India, is reportedly headed to the United Kingdom. She resigned after fresh violence in the country which erupted after weeks of protests against a government job quota system.', 'Ankush Verma', 'Tuesday, 06 August, 2024'),
(5, 2, 'https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/6_tue/img_1722928168812_802.jpg?', 'What have been Neeraj Chopra\'s top 3 throws of 2024?', 'Defending Olympic and world champion Neeraj Chopra will take part in men\'s javelin throw event qualification round at Paris Olympics today (Tuesday). His best throw in 2024 came on May 10 when he recorded a throw of 88.36 metres at Doha Diamond League. He recorded a throw of 85.97 metres at Paavo Nurmi Games and 82.27 metres at Federation Cup.', 'Anmol Sharma', 'Tuesday, 06 August, 2024');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `number` bigint(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `mail`, `password`, `number`) VALUES
(1, 'jask', 'Jask@gmail.com', 'Jask@1234', 987653210),
(2, 'jaskaran ', 'jaskaran@gmail.com', '1234', 7938747983),
(3, 'jaskaran', 'jjW@.gmail', 'l;khsoihcl', 7308973970),
(4, 'jaskaran12345', 'karan@123', 'karan1234', 99451362732),
(5, 'John', 'john@123234', 'john767676', 9945628731),
(6, 'vishal', 'vishal@1234', 'vishal12345', 9947251368),
(7, 'jaskaran', 'kk@1223', 'ldhouhdubkjbvd', 9944115289);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `news`
--
ALTER TABLE `news`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
