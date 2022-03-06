# Fichero de funciones

import sys
import MySQLdb

#Función para conectarnos a la Base de Datos.

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

#Función para desconectarnos de la Base de Datos.

def Desconectar_BD(db):
    db.close()


##Función para mostrar el menú del programa.

def MostrarMenu():
    menu='''
    1. Mostrar todos los nombres de los libros con su respectivo autor y cuantos hay.
    2. Filtrar por los libros prestados en un año concreto.
    3. Buscar los nombres de los socios tengan al menos un prestamo a fecha de hoy.
    4. Insertar los datos de un nuevo socio junto con el prestamo de un libro.
    5. Pedir por teclado el nombre de un socio y eliminarlo.
    6. Actualizar la fecha del prestamo y/o la duración.
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción: "))
            print()
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")


#Función para mostrar nombre, autor y cuantos libros hay.

def Mostrar_nombre_autor_cuantos(db):
    sql="SELECT Nombre, Autor FROM Libros"
    sql1="SELECT count(RefLibro) as 'Total Libros' FROM Libros"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("Nombre: ",registro["Nombre"],"--  Autor: ",registro["Autor"])

    except:
        print("Error en la consulta")
        
    try:
        cursor.execute(sql1)
        registros = cursor.fetchall()
        for registro in registros:
            print("")
            print("El total de libros es: ",registro["Total Libros"])

    except:
        print("Error en la consulta")


# Función para filtrar por año los nombres de los libros prestados en dicho año.

def filtrar_libros_anio(db,anio):
    sql="SELECT Nombre FROM Libros WHERE RefLibro IN (SELECT RefLibro_fk FROM Prestamos WHERE EXTRACT(YEAR FROM FechaPrestamo) =%d)" %anio
    cursor= db.cursor(MySQLdb.cursors.DictCursor)
    
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No hay libros en ese año.")
        
        else:
            registros = cursor.fetchall()
            for registro in registros:
                print("Los libros prestados son: ",registro["Nombre"])

    except:
        print("Error en la consulta")


# Función para mostrar todos los años_libros_prestados.

def mostrar_anio_libro_prestado(db):
    sql="SELECT EXTRACT(YEAR FROM FechaPrestamo) as 'Años' FROM Prestamos"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("Años: ")
        print()
        for registro in registros:
            print(registro["Años"])

    except:
        print("Error en la consulta")


# Función para buscar socios con prestamos a fecha de hoy.

def buscar_socios_prestamos(db):
    sql="SELECT Nombre FROM Socios WHERE DNI IN (SELECT DNI_fk FROM Prestamos WHERE FechaPrestamo = CURDATE())"
    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No hay prestamos a fecha de hoy.")

        else:
            registros = cursor.fetchall()
            print("Nombre de los socios con prestamos a fecha de hoy: ")
            print()
            for registro in registros:
                print(registro["Nombre"])
    
    except:
        print("Error en la consulta")


# Función para Insertar datos en la Tabla Socios.

def insertar_socios(db,socio):
    sql="INSERT INTO Socios VALUES ('%s', '%s', '%s', %d )" % (socio["DNI"],socio["Nombre"],socio["Direccion"],socio["Penalizaciones"])
    cursor = db.cursor()
    
    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error al insertar el socio.")
        db.rollback()


# Función para Insertar datos en la Tabla Prestamos.

def insertar_prestamos(db,prestamo):
    sql="INSERT INTO Prestamos VALUES ('%s', '%s', '%s', %d )" % (prestamo["DNI_fk"],prestamo["RefLibro_fk"],prestamo["FechaPrestamo"],prestamo["Duracion"])
    cursor = db.cursor()
    
    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error al insertar datos.")
        db.rollback()

#Función para Insertar datos en la Tabla Libros.

def insertar_libro(db,libro):
    sql="INSERT INTO Libros VALUES ('%s', '%s', '%s', '%s', %d, '%s' )" % (libro["RefLibro"],libro["Nombre"],libro["Autor"],libro["Genero"],libro["AnoPublicacion"],libro["Editorial"])
    cursor = db.cursor()
    
    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error al insertar el libro.")
        db.rollback()


# Función para mostrar todos los libros junto a su referencia.

def mostrar_todos_libros(db):
    sql="SELECT Nombre, RefLibro FROM Libros"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print("Nombre: ",registro["Nombre"],"--  Referencia del libro: ",registro["RefLibro"])

    except:
        print("Error en la consulta")
        

# Función para mostrar todos los datos de los socios.

def mostrar_todos_socios(db):
    sql="SELECT * FROM Socios"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

    except:
        print("Error en la consulta")


# Función para mostrar todos los datos de los prestamos.

def mostrar_todos_prestamos(db):
    sql="SELECT * FROM Prestamos"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

    except:
        print("Error en la consulta")


# Función para borrar un libro a partir de un socio introducido.

def borrar_socio(db,sociopedido):
    sql="DELETE FROM Prestamos WHERE DNI_fk = (SELECT DNI FROM Socios WHERE Nombre='%s')" % sociopedido
    sql1="DELETE FROM Socios WHERE Nombre='%s'" % sociopedido
    cursor=db.cursor()
    pregunta=input("¿Seguro que quieres borrarlo?:(s/n) ")

    if pregunta == "s":
        try:
            cursor.execute(sql)
            cursor.execute(sql1)
            db.commit()
            if cursor.rowcount==0:
                print()
                print("No existe ningún socio con ese nombre.")
            else:
                print()
                print("El socio ha sido eliminado.")
                print()
                print("***RESULTADO DE LA TABLA SOCIOS***")
                print()
                mostrar_todos_socios(db)
        except:
            print("Error al eliminar al socio")
            db.rollback()
    if pregunta == "n":
        print()
        print("El socio no ha sido eliminado")
 
# Función para actualizar la fecha de prestamo.

def actualizar_fechaPrestamo(db,nombresocio,fechpres):
    sql="UPDATE Prestamos SET FechaPrestamo = '%s' WHERE DNI_fk = (SELECT DNI FROM Socios WHERE Nombre = '%s')" % (fechpres,nombresocio)

    cursor= db.cursor()

    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error en la consulta")
        db.rollback()

# Función para actualizar la duración.

def actualizar_duracion_prestamo(db,nombresocio,duracion):
    sql="UPDATE Prestamos SET Duracion = '%s' WHERE DNI_fk = (SELECT DNI FROM Socios WHERE Nombre = '%s')" % (duracion,nombresocio)

    cursor= db.cursor()

    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error en la consulta")
        db.rollback()


# Función para mostrar los nombres de los socios.

def mostrar_nombres_socios(db):
    sql="SELECT Nombre FROM Socios"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro["Nombre"])

    except:
        print("Error en la consulta")


# Función para mostrar la fecha de prestamo y la duración de un determinado socio.

def mostrar_fechapresYduracion_socio(db,nombresocio):
    sql="SELECT FechaPrestamo as 'Fecha Prestamo', Duracion as 'Duración' FROM Prestamos WHERE DNI_fk = (SELECT DNI FROM Socios WHERE Nombre = '%s')" % (nombresocio)

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

    except:
        print("Error en la consulta")


# Función para mostrar la fecha de prestamo de un determinado socio.

def mostrar_fechapres_socio(db,nombresocio):
    sql="SELECT FechaPrestamo as 'Fecha Prestamo' FROM Prestamos WHERE DNI_fk = (SELECT DNI FROM Socios WHERE Nombre = '%s')" % (nombresocio)

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

    except:
        print("Error en la consulta")


# Función para mostrar todos los datos de la tabla Libros.

def mostrar_todos_libros_datos(db):
    sql="SELECT * FROM Libros"

    cursor= db.cursor(MySQLdb.cursors.DictCursor)

    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

    except:
        print("Error en la consulta")