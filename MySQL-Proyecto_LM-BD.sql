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
    CONSTRAINT fk_reflibro FOREIGN KEY (RefLibro_fk) REFERENCES Libros(RefLibro),
    
);


