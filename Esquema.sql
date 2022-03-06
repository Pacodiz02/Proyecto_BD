mysql -u root -p

CREATE DATABASE ProyectoBD;

CREATE USER PDiz;

GRANT ALL ON ProyectoBD.* TO PDiz IDENTIFIED BY 'asdasd';
FLUSH PRIVILEGES;

exit;

mysql -u PDiz -p ProyectoBD


CREATE TABLE Socios(
    
    DNI VARCHAR(10),
    Nombre VARCHAR(20),
    Direccion VARCHAR(20),
    Penalizaciones INT(2) DEFAULT 0,
    CONSTRAINT pk_DNI PRIMARY KEY (DNI)
);

CREATE TABLE Libros(
    
    RefLibro VARCHAR(10),
    Nombre VARCHAR(30),
    Autor VARCHAR(20),
    Genero VARCHAR(10),
    AnoPublicacion INT,
    Editorial VARCHAR (10),
    CONSTRAINT pk_RefLibro PRIMARY KEY (RefLibro)
);


CREATE TABLE Prestamos(

    DNI_fk VARCHAR(10),
    RefLibro_fk VARCHAR(10),
    FechaPrestamo DATE,
    Duracion INT(2) DEFAULT 24,
    CONSTRAINT pk_prestamos PRIMARY KEY (DNI_fk,RefLibro_fk,FechaPrestamo),
    CONSTRAINT fk_dni FOREIGN KEY (DNI_fk) REFERENCES Socios(DNI),
    CONSTRAINT fk_reflibro FOREIGN KEY (RefLibro_fk) REFERENCES Libros(RefLibro)
    
);



INSERT INTO Socios VALUES ('111-A','David','Sevilla Este',2);
INSERT INTO Socios VALUES ('222-B','Mariano','Los Remedios',3);
INSERT INTO Socios(DNI,Nombre,Direccion) VALUES ('333-C','Raul','Triana');
INSERT INTO Socios(DNI,Nombre,Direccion) VALUES ('444-D','Rocío','La Oliva');
INSERT INTO Socios VALUES ('555-E','Mariló','Triana',2);
INSERT INTO Socios VALUES ('666-F','Benjamín','Montequinto',5);
INSERT INTO Socios(DNI,Nombre,Direccion) VALUES ('777-G','Carlos','Los Remedios');
INSERT INTO Socios VALUES ('888-H','Manolo','Montequinto',2);



INSERT INTO Libros VALUES ('E-1','El valor de educar','Savater','Ensayo',1994,'Alfaguara');
INSERT INTO Libros VALUES ('N-1','El Quijote','Cervantes','Novela',1602,'Anagrama');
INSERT INTO Libros VALUES ('E-2','La República','Platón','Ensayo',-230,'Anagrama');
INSERT INTO Libros VALUES ('N-2','Tombuctú','Auster','Novela',1998,'Planeta');
INSERT INTO Libros VALUES ('N-3','Todos los nombres','Saramago','Novela',1995,'Planeta');
INSERT INTO Libros VALUES ('E-3','Etica para Amador','Savater','Ensayo',1991,'Alfaguara');
INSERT INTO Libros VALUES ('P-1','Rimas y Leyendas','Becquer','Poesía',1837,'Anagrama');
INSERT INTO Libros VALUES ('P-2','Las flores del mal','BaudelaireBaudelaire','Poesía',1853,'Anagrama');
INSERT INTO Libros VALUES ('P-3','El fulgor','Valente','Poesía',1998,'Alfaguara');
INSERT INTO Libros VALUES ('N-4','Lolita','Nabokov','Novela',1965,'Planeta');
INSERT INTO Libros VALUES ('C-1','En salvaje compañía','Rivas','Cuento',2001,'Alfaguara');



INSERT INTO Prestamos VALUES ('111-A','E-1','2000/12/17',24);
INSERT INTO Prestamos VALUES ('333-C','C-1','2005/12/15',48);
INSERT INTO Prestamos VALUES ('111-A','N-1','2006/12/17',24);
INSERT INTO Prestamos VALUES ('444-D','E-1','2007/12/17',48);
INSERT INTO Prestamos VALUES ('111-A','N-3','2002/12/17',72);
INSERT INTO Prestamos(DNI_fk,RefLibro_fk,FechaPrestamo) VALUES ('777-G','N-1','2008/12/07');
INSERT INTO Prestamos VALUES ('888-H','N-2','2009/12/16',48);

