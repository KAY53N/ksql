/*
SQLyog Ultimate v11.27 (32 bit)
MySQL - 10.1.13-MariaDB : Database - test
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`test` /*!40100 DEFAULT CHARACTER SET utf8 */;

/*Table structure for table `ksql_article` */

DROP TABLE IF EXISTS `ksql_article`;

CREATE TABLE `ksql_article` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `created` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `ksql_article` */

LOCK TABLES `ksql_article` WRITE;

insert  into `ksql_article`(`id`,`title`,`content`,`created`) values (1,'很赞！给iOS信息应用的界面换一个效果吧','<p align=\"center\"><img src=\"//images2015.cnblogs.com/news/66372/201702/66372-20170220131226335-311554195.jpg\" alt=\"\"></p>\r\n<p><br>　　如果你经常使用 iPhone 预装的信息应用，那么你是否想过给这款应用的聊天界面换一个效果。如果你想尝试的话，越狱社区最近上架的 TranslucentMessages 插件或许能满足你的要求。</p>\r\n<p>　　TranslucentMessages 插件不会更改信息应用中的任何功能，只是改变它的整体视觉效果，将背景改成半透明的效果。安装这款插件之后，信息应用的对话列表、对话框乃至详细信息面板的背景都会变成半透明的效果。</p>\r\n<p>　　如果你怕这种效果会影响到界面上的文字和信息的可读性，那么你大可放心，TranslucentMessages 并不会对这些有任何影响。如果因为某些原因你需要关闭半透明效果，那么你只要在设置应用该插件的相应面板添加该插件即可。</p>\r\n<p>　　本月早些时候，越狱社区推出了一款能给信息应用增加暗黑主题的插件——DarkMessages，新的 TranslucentMessages 插件可与这款插件兼容。如果你同时安装这两款插件的话，那么你就会得到一个比较黑暗的半透明效果，如下图。你是否喜欢这款插件带来的效果？</p>\r\n<p align=\"center\"><img src=\"//images2015.cnblogs.com/news/66372/201702/66372-20170220131225616-1515736414.jpg\" alt=\"\"></p>\r\n',0);

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
