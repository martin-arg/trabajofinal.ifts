-- No existe DROP DATABASE ni CREATE DATABASE en SQLite, se usa un archivo .db
-- Simplemente se crea el archivo clubsocial-python.db y se ejecutan estas sentencias.

PRAGMA foreign_keys = ON;

CREATE TABLE usuarios (
  usuarioID INTEGER PRIMARY KEY AUTOINCREMENT,
  usuario TEXT NOT NULL,
  clave TEXT NOT NULL,
  rol TEXT NOT NULL,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL
);

CREATE TABLE actividades (
  actividadID INTEGER PRIMARY KEY AUTOINCREMENT,
  actividad TEXT NOT NULL,
  responsableID INTEGER NOT NULL,
  dias TEXT NOT NULL,
  horario TEXT NOT NULL,
  asistentesMax INTEGER NOT NULL,
  FOREIGN KEY (responsableID) REFERENCES usuarios (usuarioID)
);

CREATE TABLE socios (
  socioID INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  dni INTEGER NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE clases (
  actividadID INTEGER NOT NULL,
  socioID INTEGER NOT NULL,
  PRIMARY KEY (actividadID, socioID),
  FOREIGN KEY (actividadID) REFERENCES actividades (actividadID),
  FOREIGN KEY (socioID) REFERENCES socios (socioID)
);

-- Inserts

INSERT INTO usuarios (usuario, clave, rol, nombre, apellido) VALUES
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

INSERT INTO actividades (actividad, responsableID, dias, horario, asistentesMax) VALUES
  ("Canticuenticos",4,"Lunes","17",6),
  ("Espacio de Juegos",6,"Martes","17",10),
  ("Bingo",6,"Viernes","21",20),
  ("Karate",4,"Miercoles","18",12),
  ("Boxeo",4,"Jueves","18",8),
  ("Newcom",7,"Sabado","10",12),
  ("Streching",8,"Viernes","10",6),
  ("Yoga",8,"Domingo","9",6),
  ("Danza",6,"Viernes","18",16),
  ("Club de lectura",10,"Sabado","18",14),
  ("Pintura",9,"Martes","18",8),
  ("Manualidades",9,"Lunes","18",8);

INSERT INTO socios (name, dni, email) VALUES
  ("Stephen Fowler",42453943,"lacus.vestibulum@hotmail.edu"),
  ("Melanie French",79652472,"sed.hendrerit@protonmail.edu"),
  ("Keane Sharp",66274367,"laoreet@hotmail.com"),
  ("Baxter Hodges",12702492,"interdum.nunc.sollicitudin@google.org"),
  ("Aquila Nixon",31828544,"natoque@aol.couk"),
  ("Xantha Lynn",64061740,"sed@icloud.ca"),
  ("Jane Hunt",28616838,"eu.eleifend@outlook.com"),
  ("Hope Hanson",98865979,"arcu@yahoo.net"),
  ("Willa Washington",82299289,"pellentesque.ultricies@aol.com"),
  ("Abbot Keith",48534133,"torquent@protonmail.ca"),
  ("Cadman Short",36458824,"nisi.dictum.augue@outlook.ca"),
  ("Amanda Travis",62023807,"mauris.sit.amet@protonmail.com"),
  ("Herman Clayton",34591050,"nisi.mauris.nulla@protonmail.ca"),
  ("Dominic Barry",27867191,"arcu.iaculis.enim@google.net"),
  ("Zia Parrish",42655966,"mauris.rhoncus.id@google.ca"),
  ("Cassady Vaughn",87532217,"aenean.euismod@aol.net"),
  ("Cassady Hampton",1515859,"morbi.non@hotmail.com"),
  ("Riley Fisher",36813333,"nullam.velit@aol.edu"),
  ("Damian Pace",52278241,"fusce@icloud.ca"),
  ("Arden Raymond",47048951,"feugiat@protonmail.net");

INSERT INTO clases (actividadID, socioID) VALUES
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
