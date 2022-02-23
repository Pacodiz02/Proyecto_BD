CREATE TABLE Socios(
    
    DNI VARCHAR2(10),
    Nombre VARCHAR2(20),
    Direccion VARCHAR2(20),
    Penalizaciones NUMBER(2) DEFAULT 0,
    CONSTRAINT pk_DNI PRIMARY KEY (DNI)
);

CREATE TABLE Libros(
    
    RefLibro VARCHAR2(10),
    Nombre VARCHAR2(30),
    Autor VARCHAR2(20),
    Genero VARCHAR2(10),
    AnoPublicacion NUMBER,
    Editorial VARCHAR2 (10),
    CONSTRAINT pk_RefLibro PRIMARY KEY (RefLibro)
);


CREATE TABLE Prestamos(

    DNI_fk VARCHAR2(10),
    RefLibro_fk VARCHAR2(10),
    FechaPrestamo DATE,
    Duracion NUMBER(2) DEFAULT 24,
    CONSTRAINT pk_prestamos PRIMARY KEY (DNI_fk,RefLibro_fk,FechaPrestamo),
    CONSTRAINT fk_dni FOREIGN KEY (DNI_fk) REFERENCES Socios(DNI),
    CONSTRAINT fk_reflibro FOREIGN KEY (RefLibro_fk) REFERENCES Libros(RefLibro),
    
);


