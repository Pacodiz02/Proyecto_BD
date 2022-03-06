# Programa principal

from Funciones import *

db = Conectar_BD("localhost","PDiz","asdasd","ProyectoBD")

opcion=MostrarMenu()

while opcion!=0:

    if opcion == 1:
        Mostrar_nombre_autor_cuantos(db)
        

    elif opcion==2:
        print()
        mostrar_anio_libro_prestado(db)
        print("\n")
        anio=int(input("Introduce un año: "))
        filtrar_libros_anio(db,anio)
        

    elif opcion==3:
        buscar_socios_prestamos(db)


    elif opcion==4:
        libronuevo=input("¿Ha llegado algún libro nuevo?(s/n) ")
        if libronuevo=="s":
            libro={}
            libro["RefLibro"]=input("Referencia del libro(Ej:N-1): ")
            libro["Nombre"]=input("Nombre: ")
            libro["Autor"]=input("Autor: ")
            libro["Genero"]=input("Genero: ")
            libro["AnoPublicacion"]=int(input("Ano de su publicacion: "))
            libro["Editorial"]=input("Editorial: ")
            insertar_libro(db,libro)

            print()
            print("***INSERTANDO DATOS EN LA TABLA SOCIOS***")
            print()
            socio={}
            socio["DNI"]=input("DNI(Ej: 111-A): ")
            socio["Nombre"]=input("Nombre: ")
            socio["Direccion"]=input("Dirección: ")
            socio["Penalizaciones"]=int(input("Penalizaciones: "))
            insertar_socios(db,socio)
    
            print()
            print("***INSERTANDO DATOS EN LA TABLA PRESTAMOS***")
            print()
            prestamo={}
            prestamo["DNI_fk"] = socio["DNI"]
            print()
            mostrar_todos_libros(db)
            print()
            prestamo["RefLibro_fk"]=input("Referia Libro: ")
            prestamo["FechaPrestamo"]=input("Fecha del prestamo(YYYY/MM/DD): ")
            prestamo["Duracion"]=int(input("Duración: "))
            insertar_prestamos(db,prestamo)
    
            print("\n")
            print("***RESULTADO DE LA TABLA SOCIOS***")
            print()
            mostrar_todos_socios(db)
    
            print("\n")
            print("***RESULTADO DE LA TABLA PRESTAMOS***")
            print()
            mostrar_todos_prestamos(db)

        if libronuevo=="n":
            print()
            print("***INSERTANDO DATOS EN LA TABLA SOCIOS***")
            print()
            socio={}
            socio["DNI"]=input("DNI(Ej: 111-A): ")
            socio["Nombre"]=input("Nombre: ")
            socio["Direccion"]=input("Dirección: ")
            socio["Penalizaciones"]=int(input("Penalizaciones: "))
            insertar_socios(db,socio)

            print()
            print("***INSERTANDO DATOS EN LA TABLA PRESTAMOS***")
            print()
            prestamo={}
            prestamo["DNI_fk"] = socio["DNI"]
            print()
            mostrar_todos_libros(db)
            print()
            prestamo["RefLibro_fk"]=input("Referia Libro: ")
            prestamo["FechaPrestamo"]=input("Fecha del prestamo(YYYY/MM/DD): ")
            prestamo["Duracion"]=int(input("Duración: "))
            insertar_prestamos(db,prestamo)

            print("\n")
            print("***RESULTADO DE LA TABLA SOCIOS***")
            print()
            mostrar_todos_socios(db)

            print("\n")
            print("***RESULTADO DE LA TABLA PRESTAMOS***")
            print()
            mostrar_todos_prestamos(db)


    elif opcion==5:
        print("\n")
        print("Estos son todos los socios actuales: ")
        print()
        mostrar_nombres_socios(db)
        print("\n")
        sociopedido=input("Intoduce el nombre del socio que deseas eliminar: ")
        borrar_socio(db,sociopedido)


    elif opcion==6:
        print("\n")
        print("Estos son los socios que existen actualmente: ")
        print()
        mostrar_nombres_socios(db)
        print("\n")
        nombresocio=input("Introduce el nombre del socio: ")
        print()
        mostrar_fechapresYduracion_socio(db,nombresocio)
        print("\n")
        fechpres=input("Introduce una nueva fecha de prestamo:(YYYY/MM/DD) ")
        actualizar_fechaPrestamo(db,nombresocio,fechpres)
        print("\n")
        
        pregunta2=input("¿Quieres modificar tambien la duración del mismo?(s/n) ")
        print()
        if pregunta2=="s":
            duracion=int(input("Introduce la nueva duración del prestamo: "))
            print("\n")
            actualizar_duracion_prestamo(db,nombresocio,duracion)
            print("***RESULTADO DEL CAMBIO***")
            print()
            mostrar_fechapresYduracion_socio(db,nombresocio)
        if pregunta2=="n":
            print()
            mostrar_fechapres_socio(db,nombresocio)
        print()
        print("***RESULTADO TABLA PRESTAMOS***")
        print()
        mostrar_todos_prestamos(db)

    else:
        print("Opción incorrecta.")
    
    print()
    print("+---------------------------------------------------------------+")
    opcion=MostrarMenu()

Desconectar_BD(db)