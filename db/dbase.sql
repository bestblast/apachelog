DROP DATABASE IF EXISTS apachelog;

CREATE DATABASE `apachelog` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE apachelog;

DROP TABLE IF EXISTS httpd;

CREATE TABLE `httpd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` INT UNSIGNED DEFAULT NULL,
  `l` varchar(100) DEFAULT NULL,
  `u` varchar(100) DEFAULT NULL,
  `time` varchar(28) DEFAULT NULL,
  `request` varchar(100) DEFAULT NULL,
  `status` INT(3) UNSIGNED,
  `b` varchar(100) DEFAULT NULL,
  `referer` varchar(100) DEFAULT NULL,
  `user_agent` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
