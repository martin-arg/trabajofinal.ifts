DROP DATABASE `clubsocial`;
CREATE DATABASE `clubsocial`;
USE `clubsocial`;

CREATE TABLE `usuarios` (
  `usuarioID` mediumint(8) PRIMARY KEY AUTO_INCREMENT,
  `usuario` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `rol` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL
) AUTO_INCREMENT=1;

CREATE TABLE `actividades` (
  `actividadID`  mediumint(8) PRIMARY KEY AUTO_INCREMENT,
  `actividad` varchar(255) NOT NULL,
  `responsableID` mediumint(8) NOT NULL ,
  `dias` varchar(255)  NOT NULL,
  `horario` varchar(255)  NOT NULL,
  `asistentesMax` tinyint  NOT NULL,
  FOREIGN KEY (`responsableID`) REFERENCES `usuarios` (`usuarioID`)
) AUTO_INCREMENT=1;


CREATE TABLE `socios` (
  `socioID`  mediumint(8) PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `dni` INT(8) NOT NULL,
  `email` varchar(255) NOT NULL
--  `actividadesID` mediumint(8) NOT NULL,
--  FOREIGN KEY (`actividadesID`) REFERENCES `actividades` (`actividadID`)
) AUTO_INCREMENT=1;

CREATE TABLE `clases` (
`actividadID`  mediumint(8),
`socioID`  mediumint(8),
PRIMARY KEY (`actividadID`, `socioID`),
FOREIGN KEY (`actividadID`) REFERENCES `actividades` (`actividadID`),
FOREIGN KEY (`socioID`) REFERENCES `socios` (`socioID`)
);

-- Inserta values

INSERT INTO `usuarios` (`usuario`,`clave`,`rol`,`nombre`,`apellido`)
VALUES
  ("1@2.com","1234","Administrador","Martin","Gigli"),
  ("mattis@google.edu","WYQ91BLF3NR","Administrativo","Heather","Langley"),
  ("in.lobortis@aol.edu","HZE27NZO0KZ","Administrativo","Odysseus","Levy"),
  ("enim.sit@outlook.net","IFJ76POG3XI","Docente","Alec","Morris"),
  ("dictum@yahoo.com","YNO33TIY6CN","Docente","Omar","Hess"),
  ("eu.neque@icloud.couk","SPG76EHG9UI","Docente","Fiona","Guy"),
  ("natoque.penatibus.et@google.ca","WIL83GHO5PE","Docente","Mira","Witt"),
  ("nec.orci.donec@google.com","VPU31QBF0FD","Docente","Ulric","Mclaughlin"),
  ("est.arcu@aol.com","PEQ21QPU7FD","Docente","Libby","Shields"),
  ("consequat.nec@icloud.ca","EPD51RVI6XB","Docente","Callie","Sheppard");

INSERT INTO `actividades` (`actividad`,`responsableID`,`dias`,`horario`,`asistentesMax`)
VALUES
  ("Canticuenticos",4,"Lunes",17,6),
  ("Espacio de Juegos",6,"Martes",17,10),
  ("Bingo",6,"Viernes",21,20),
  ("Karate",4,"Miercoles",18,12),
  ("Boxeo",4,"Jueves",18,8),
  ("Newcom",7,"Sabado",10,12),
  ("Streching",8,"Viernes",10,6),
  ("Yoga",8,"Domingo",9,6),
  ("Danza",6,"Viernes",18,16),
  ("Club de lectura",10,"Sabado",18,14),
  ("Pintura",9,"Martes",18,8),
  ("Manualidades",9,"Lunes",18,8);


INSERT INTO `socios` (`name`,`dni`,`email`)
VALUES
  ("Stephen Fowler","42453943","lacus.vestibulum@hotmail.edu"),
  ("Melanie French","79652472","sed.hendrerit@protonmail.edu"),
  ("Keane Sharp","66274367","laoreet@hotmail.com"),
  ("Baxter Hodges","12702492","interdum.nunc.sollicitudin@google.org"),
  ("Aquila Nixon","31828544","natoque@aol.couk"),
  ("Xantha Lynn","64061740","sed@icloud.ca"),
  ("Jane Hunt","28616838","eu.eleifend@outlook.com"),
  ("Hope Hanson","98865979","arcu@yahoo.net"),
  ("Willa Washington","82299289","pellentesque.ultricies@aol.com"),
  ("Abbot Keith","48534133","torquent@protonmail.ca");
INSERT INTO `socios` (`name`,`dni`,`email`)
VALUES
  ("Cadman Short","36458824","nisi.dictum.augue@outlook.ca"),
  ("Amanda Travis","62023807","mauris.sit.amet@protonmail.com"),
  ("Herman Clayton","34591050","nisi.mauris.nulla@protonmail.ca"),
  ("Dominic Barry","27867191","arcu.iaculis.enim@google.net"),
  ("Zia Parrish","42655966","mauris.rhoncus.id@google.ca"),
  ("Cassady Vaughn","87532217","aenean.euismod@aol.net"),
  ("Cassady Hampton","01515859","morbi.non@hotmail.com"),
  ("Riley Fisher","36813333","nullam.velit@aol.edu"),
  ("Damian Pace","52278241","fusce@icloud.ca"),
  ("Arden Raymond","47048951","feugiat@protonmail.net");

INSERT INTO `clases` (`actividadID`, `socioID`)
VALUES
 (1,2),
 (1,4),
 (1,6),
 (1,9),
 (2,10),
 (2,6),
 (2,5),
 (2,19),
 (3,1),
 (3,5),
 (3,16),
 (3,7),
 (3,6),
 (4,6),
 (4,3),
 (4,12),
 (4,4),
 (5,15),
 (5,14),
 (5,3),
 (6,17),
 (6,6),
 (6,3),
 (7,1),
 (7,2),
 (7,3),
 (8,4),
 (8,5),
 (8,6),
 (9,7),
 (9,8),
 (9,9),
 (10,10),
 (10,11),
 (10,12),
 (11,13),
 (11,14),
 (11,15),
 (12,16),
 (12,17);