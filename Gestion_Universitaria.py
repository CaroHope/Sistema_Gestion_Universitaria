'''
Descripción: Sistema de Gestión Universitaria que permite la visualización y Manipulación de
             los datos pertenecientes a los estudiantes, profesores, materias, carreras, etc.
             Este sistema permite una conexión con una base de datos MySQL. Puede guardar, editar,
             visualizar o modificar los datos de las tablas.

             Copiar y pegar comandos de Script_MySQL.txt en MYSQL Command Line Client para
             el correcto funcionamiento del Sistema de Gestión Universitaria.

Autor: Evelyn Carolina Jorge

Matricula: 20-0084

EXAMEN FINAL

'''

import time
import sys
import mysql.connector


#Conexión a la base de datos ==========
db = mysql.connector.connect(host ='localhost', user = 'root', password = 'Carowow7', database = 'gestion_universitaria')
mycursor = db.cursor()




def Login ():    
    y = 0
    intentos = 0
    print(" \n ")
    print("◣ ◥ ◣ ◥ ◤ ◢ ◤ ◢ ◣ ◥ ◣ ◥ ◤ ◢ ")
    print(". . . . . . . . . . .")
    print("< G E S T I Ó N \n    U N I V E R S I T A R I A >")
    print(". . . . . . . . . .")
    time.sleep(1)
    print(" ")
    print("\n┏━━━━━━━━━━━━━┓")
    print(" < L O G I N > ")
    print("┗━━━━━━━━━━━━━┛ ")

    while y == 0 and intentos<3:
        time.sleep(0.5)
        print("\nBienvenido!")
        usuario = input ("Ingrese su Nombre de Usuario: ")
        password = input("Ingrese su Contraseña:  ")

        #Buscar en tabla profesor ----
        Comando = 'SELECT usuario,password FROM profesor WHERE usuario = %s and password= %s order by 1'
        valores = (usuario,password)
        mycursor.execute(Comando,valores)
        
        for x in mycursor:
            if x == valores:
                y = y+1
                
        #Buscar en tabla estudiante ----
        Comando = 'SELECT usuario,password FROM estudiante WHERE usuario = %s and password= %s order by 1'
        valores = (usuario,password)
        mycursor.execute(Comando,valores)
        
        for x in mycursor:
            if x == valores:
                y = y+1
                
        if y == 0:
            print("Contraseña o nombre de Usuario incorrectos.")
            intentos = intentos +1

    if intentos == 3:
        time.sleep(1)
        print("\nHa superado los intentos de acceso. Inténtelo mas tarde.\n")

    
    if y > 0:
        MenuPrincipal()




def MenuPrincipal():

    print(" ")
    print("\n▁  ▂  ▄  ▅  ▆  ▇  █ ✧ █  ▇  ▆  ▅  ▄  ▂  ▁ ")
    print("< B I E N V E N I D O  A L  S I S T E M A >")

    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print("\n  MENU PRINCIPAL \n")
        print(" ¿Qué Área deseas Manipular? ")
        print("-Materias (1) ")
        print("-Carreras (2) ")
        print("-Estudiantes (3) ")
        print("-Profesores (4) ")
        print("-Materias por Carrera (5)")
        print("-Materias por Estudiante (6)")
        print("-Materias por Profesor (7)")
        print("-Salir (8) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6 or opci==7 or opci==8:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")


    # Opciones del Menú Principal
    if opci == 1:
        MateriasMenu()

    elif opci == 2:
        CarrerasMenu()

    elif opci == 3:
        EstudiantesMenu()
    
    elif opci == 4:
        ProfesoresMenu()
    
    elif opci == 5:
        MatexCarrera()

    elif opci == 6:
        MatexEstudiante()

    elif opci == 7:
        MatexProfesor()

    else:
        print("\nHasta Pronto!\n")
        time.sleep(0.3)
        sys.exit()



# //////////////  O P C I O N E S   D E L   M E N Ú   P R I N C I P A L  //////////////

#Opción 1
def MateriasMenu():
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n M A T E R I A S ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú MATERIAS:


    # Registrar (1)===================
    if opci == 1:

        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar una Nueva Materia! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_pensum = input("Número de Pensum:  ")
            if not nu_pensum or nu_pensum==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #estos campos sí pueden ir nulos.   
        nom_estudiante = input("Nombre de estudiante en materia: ")
        matricula = input("Matricula de estudiante:  ")

        while y ==7:
            facultad = input("Facultad de la materia:  ")
            if not facultad or facultad==" ":
                print("Ingrese un campo.")
            else:
                y= y+1


        #Insertar/Registar en tabla materia 
        
        Comando = 'INSERT INTO materia (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor, apellido_profesor, nombre_estudiante, matricula_estudiante, facultad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Materia Insertada")
        MateriasMenu()




    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte una Materia. ")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        cred = input("Escriba los créditos de la materia: ")

        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and creditos = %s'
        valores = (cod,cred)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias..")
                MateriasMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Materias Almacenadas: ")
        time.sleep(0.5)
        print(" ")
        mycursor.execute("SELECT * FROM materia")
        resultado = mycursor.fetchall()
        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias..")
                MateriasMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar una Materia ")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (cod,nom)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")
            MateriasMenu()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR esta Materia? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM materia WHERE codigo_materia= %s and nombre_materia = %s'
                    valores = (cod,nom)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nMateria Eliminada..")
                    time.sleep(0.5)
                    MateriasMenu()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Materias..")
                    time.sleep(1)
                    MateriasMenu()
                    lu==1
                else:
                    print("Ingrese una opción válida.")

        




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar una materia!")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia que quiere actualizar\n(Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (cod,nom)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Materia a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Materia no Encontrada.")
            MateriasMenu()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_pensum = input("Número de Pensum:  ")
            if not nu_pensum or nu_pensum==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #estos campos sí pueden ir nulos.   
        nom_estudiante = input("Nombre de estudiante en materia: ")
        matricula = input("Matricula de estudiante:  ")

        while y ==7:
            facultad = input("Facultad de la materia:  ")
            if not facultad or facultad==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #Actualizar en tabla materia 
        Comando = 'UPDATE materia SET codigo_materia = %s, nombre_materia = %s, creditos = %s, nu_pensum = %s, nu_sesion = %s, nombre_profesor = %s, apellido_profesor = %s, nombre_estudiante = %s, matricula_estudiante = %s, facultad = %s WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad, cod, nom)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nMateria Actualizada.")
        time.sleep(0.5)
        MateriasMenu()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()
        

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




#Opción 2
def CarrerasMenu():
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n C A R R E R A S ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú CARRERAS:


    # Registrar (1)===================
    if opci == 1:

        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar una Nueva Carrera! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
                
        while y ==0:
            nombre_carrera = input("Nombre de la Carrera:  ")
            if not nombre_carrera or nombre_carrera==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            nu_pensum = input("Número de Pensum:  ")
            if not nu_pensum or nu_pensum==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            facultad = input("Facultad de la Carrera:  ")
            if not facultad or facultad==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            departamento = input("Departamento de la Carrera:  ")
            if not departamento or departamento==" ":
                print("Ingrese un campo.")
            else:
                y= y+1


        #Insertar/Registar en tabla materia 
        
        Comando = 'INSERT INTO carrera (nombre_carrera, nu_pensum, facultad, departamento) VALUES (%s, %s, %s, %s)'
        valores = (nombre_carrera, nu_pensum, facultad, departamento)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Carrera Insertada")
        CarrerasMenu()




    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte una Carrera. ")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el nombre de la Carrera: ")
        fac = input("Escriba la Facultad de la Carrera: ")

        Comand = 'SELECT * FROM carrera WHERE nombre_carrera= %s and facultad = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Carrera no Encontrada.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Carreras? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Carreras..")
                CarrerasMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Carreras Almacenadas: ")
        time.sleep(0.5)
        print(" ")
        mycursor.execute("SELECT * FROM carrera")
        resultado = mycursor.fetchall()
        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Carreras? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Carreras..")
                CarrerasMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar una Carrera ")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el nombre de la Carrera: ")
        fac = input("Escriba la Facultad de la Carrera: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM carrera WHERE nombre_carrera = %s and facultad = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Carrera no Encontrada.")
            CarrerasMenu()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR esta carrera? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM carrera WHERE nombre_carrera = %s and facultad = %s'
                    valores = (nom, fac)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nCarrera Eliminada..")
                    time.sleep(0.5)
                    CarrerasMenu()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Carreras..")
                    time.sleep(1)
                    CarrerasMenu()
                    lu==1
                else:
                    print("Ingrese una opción válida.")

        




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar una Carrera!")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el nombre de la Carrera a Actualizar: ")
        fac = input("Escriba la Facultad de la Carrera: ")
        print(" ")

        #Buscar carrera primero
        Comand = 'SELECT * FROM carrera WHERE nombre_carrera= %s and facultad = %s'
        valores = (nom, fac)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Carrera a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Carrera no Encontrada.")
            CarrerasMenu()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            nombre_carrera = input("Nombre de la Carrera:  ")
            if not nombre_carrera or nombre_carrera==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            nu_pensum = input("Número de Pensum:  ")
            if not nu_pensum or nu_pensum==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            facultad = input("Facultad de la Carrera:  ")
            if not facultad or facultad==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            departamento = input("Departamento de la Carrera:  ")
            if not departamento or departamento==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #Actualizar en tabla carrera
        Comando = 'UPDATE carrera SET nombre_carrera = %s, nu_pensum = %s, facultad = %s, departamento = %s WHERE nombre_carrera= %s and facultad = %s'
        valores = (nombre_carrera, nu_pensum, facultad, departamento, nom, fac)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nCarrera Actualizada.")
        time.sleep(0.5)
        CarrerasMenu()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




#Opción 3
def EstudiantesMenu():
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n E S T U D I A N T E S ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú ESTUDIANTES:


    # Registrar (1)===================
    if opci == 1:

        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar un Nuev@ Estudiante! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
                
        while y ==0:
            nombre = input("Nombre del estudiante:  ")
            if not nombre or nombre==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            apellido = input("Apellido del estudiante:  ")
            if not apellido or apellido==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            usuario = input("Nombre de usuario  ")
            if not usuario or usuario==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            password = input("Contraseña:  ")
            if not password or password==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            correo_electronico = input("Correo Electronico:  ")
            if not correo_electronico or correo_electronico==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            carrera = input("Carrera del estudiante:  ")
            if not carrera or carrera==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
        print("Se le asignará una matrícula.")


        #Insertar/Registar en tabla estudiante 
        Comando = 'INSERT INTO estudiante (nombre, apellido, usuario, password, correo_electronico, carrera) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (nombre, apellido, usuario, password, correo_electronico, carrera)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Estudiante Insertado")
        EstudiantesMenu()




    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte un Estudiante. ")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba la matricula del Estudiante: ")
        fac = input("Escriba el Nombre: ")

        Comand = 'SELECT * FROM estudiante WHERE matricula= %s and nombre = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Estudiante no Encontrado.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Estudiantes? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Estudiantes..")
                EstudiantesMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Estudiantes Almacenados: ")
        time.sleep(0.5)
        print(" ")
        mycursor.execute("SELECT * FROM estudiante")
        resultado = mycursor.fetchall()
        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Estudiantes? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Estudiantes..")
                EstudiantesMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar un Estudiante ")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba la matricula del Estudiante: ")
        fac = input("Escriba el Nombre del Estudiante: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM estudiante WHERE matricula = %s and nombre = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Estudiante no Encontrado.")
            EstudiantesMenu()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR este estudiante? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM estudiante WHERE matricula = %s and nombre = %s'
                    valores = (nom, fac)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nEstudiante Eliminado..")
                    time.sleep(0.5)
                    EstudiantesMenu()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Estudiantes..")
                    time.sleep(1)
                    EstudiantesMenu()
                    lu==1
                else:
                    print("Ingrese una opción válida.")

        




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar un Estudiante")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba la matricula del Estudiante: ")
        fac = input("Escriba el Nombre del Estudiante: ")
        print(" ")

        #Buscar Estudiante primero
        Comand = 'SELECT * FROM estudiante WHERE matricula= %s and nombre = %s'
        valores = (nom, fac)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Estudiante a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Estudiante no Encontrado.")
            EstudiantesMenu()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            nombre = input("Nombre del estudiante:  ")
            if not nombre or nombre==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            apellido = input("Apellido del estudiante:  ")
            if not apellido or apellido==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            usuario = input("Nombre de usuario  ")
            if not usuario or usuario==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            password = input("Contraseña:  ")
            if not password or password==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            correo_electronico = input("Correo Electronico:  ")
            if not correo_electronico or correo_electronico==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            carrera = input("Carrera del estudiante:  ")
            if not carrera or carrera==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #Actualizar en tabla carrera
        Comando = 'UPDATE estudiante SET nombre = %s, apellido = %s, usuario = %s, password = %s, correo_electronico = %s, carrera = %s WHERE matricula= %s and nombre = %s'
        valores = (nombre, apellido, usuario, password, correo_electronico, carrera, nom, fac)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nEstudiante Actualizado.")
        time.sleep(0.5)
        EstudiantesMenu()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def ProfesoresMenu():
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n P R O F E S O R E S ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú PROFESORES:


    # Registrar (1)===================
    if opci == 1:

        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar un Nuevo Profesor! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
                
        while y ==0:
            nombre = input("Nombre del Profesor:  ")
            if not nombre or nombre==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            apellido = input("Apellido del profesor:  ")
            if not apellido or apellido==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            usuario = input("Nombre de usuario  ")
            if not usuario or usuario==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            password = input("Contraseña:  ")
            if not password or password==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            telefono = input("Telefono:  ")
            if not telefono or telefono == " ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            cedula = input("Cedula:  ")
            if not cedula or cedula==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            correo_electronico = input("Correo Electronico:  ")
            if not correo_electronico or correo_electronico==" ":
                print("Ingrese un campo.")
            else:
                y= y+1


        #Insertar/Registar en tabla profesor
        Comando = 'INSERT INTO profesor (nombre, apellido, usuario, password, telefono, cedula, correo_electronico) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores = (nombre, apellido, usuario, password, telefono, cedula, correo_electronico)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Profesor Insertado")
        ProfesoresMenu()




    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte un profesor. ")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el id del profesor: ")
        fac = input("Escriba el Nombre del profesor: ")

        Comand = 'SELECT * FROM profesor WHERE id_profesor= %s and nombre = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Profesor no Encontrado.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Profesor? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Profesor..")
                ProfesoresMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Profesores Almacenados: ")
        time.sleep(0.5)
        print(" ")
        mycursor.execute("SELECT * FROM profesor")
        resultado = mycursor.fetchall()
        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Profesores? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Profesores..")
                ProfesoresMenu()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar un Profesor")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el id del profesor: ")
        fac = input("Escriba el Nombre del profesor: ")
        print(" ")

        #Buscar profesor primero
        Comand = 'SELECT * FROM profesor WHERE id_profesor = %s and nombre = %s'
        valores = (nom,fac)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Profesor no Encontrado.")
            ProfesoresMenu()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR este Profesor? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM profesor WHERE id_profesor= %s and nombre = %s'
                    valores = (nom, fac)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nProfesor Eliminado..")
                    time.sleep(0.5)
                    ProfesoresMenu()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Profesores..")
                    time.sleep(1)
                    ProfesoresMenu()
                    lu==1
                else:
                    print("Ingrese una opción válida.")

        




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar un Profesor")
        print(" ")
        time.sleep(0.5)
        nom = input("Escriba el id del profesor: ")
        fac = input("Escriba el Nombre del profesor: ")
        print(" ")

        #Buscar Profesor primero
        Comand = 'SELECT * FROM profesor WHERE id_profesor= %s and nombre = %s'
        valores = (nom, fac)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Profesor a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Profesor no Encontrado.")
            ProfesoresMenu()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            nombre = input("Nombre del Profesor:  ")
            if not nombre or nombre==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==1:
            apellido = input("Apellido del profesor:  ")
            if not apellido or apellido==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            usuario = input("Nombre de usuario  ")
            if not usuario or usuario==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            password = input("Contraseña:  ")
            if not password or password==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            telefono = input("Telefono:  ")
            if not telefono or telefono == " ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            cedula = input("Cedula:  ")
            if not cedula or cedula==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            correo_electronico = input("Correo Electronico:  ")
            if not correo_electronico or correo_electronico==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #Actualizar en tabla profesor
        Comando = 'UPDATE profesor SET nombre = %s, apellido = %s, usuario = %s, password = %s, telefono = %s, cedula = %s, correo_electronico = %s WHERE id_profesor= %s and nombre = %s'
        valores = (nombre, apellido, usuario, password, telefono, cedula, correo_electronico, nom, fac)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nProfesor Actualizado.")
        time.sleep(0.5)
        ProfesoresMenu()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def MatexCarrera():
    time.sleep(0.5)
    print("\n-- MATERIAS (secciones) POR CARRERA --")
    print("\n Ingresa los siguientes datos de la Carrera:")
    print(" ")
    time.sleep(0.5)
    clave1 = input("Escriba el numero de Pensum: ")
    clave2 = input("Escriba la Facultad de la carrera: ")
    print(" ")

    #Buscar carrera primero 
    Comand = 'SELECT * FROM carrera WHERE nu_pensum = %s and facultad = %s'
    valores = (clave1, clave2)
    mycursor.execute(Comand,valores)
    Val =0
    for x in mycursor:
        print("Carrera:")
        print(x)
        Val = Val+1
    if Val == 0:
        print("Carrera no Encontrada.")
        MenuPrincipal()
        
        
    # Menu de opciones
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n MATERIAS POR CARRERA ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú Materias x Carrera:


    # Registrar (1)===================
    if opci == 1:
        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar una Nueva Materia! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #estos campos sí pueden ir nulos.   
        nom_estudiante = input("Nombre de estudiante en materia: ")
        matricula = input("Matricula de estudiante:  ")

        nu_pensum = clave1
        facultad = clave2

        #Insertar/Registar en tabla materia 
        
        Comando = 'INSERT INTO materia (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor, apellido_profesor, nombre_estudiante, matricula_estudiante, facultad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Materia x Carrera Insertada")
        MatexCarrera()
        



    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte una Materia. ")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        cred = input("Escriba los créditos de la materia: ")

        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and creditos = %s and nu_pensum =%s and facultad = %s'
        valores = (cod,cred,clave1,clave2)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias por Carrera? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias Carrera..")
                MatexCarrera()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Materias por Carrera Almacenadas: ")
        time.sleep(0.5)
        print(" ")
        Comand = 'SELECT * FROM materia WHERE nu_pensum = %s and facultad = %s'
        valores = (clave1, clave2)
        mycursor.execute(Comand,valores)
        resultado = mycursor.fetchall()

        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias x Carrera? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias x Carrera..")
                MatexCarrera()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar una Materia por Carrera")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nu_pensum = %s and facultad = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")
            MatexCarrera()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR esta Materia? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nu_pensum = %s and facultad = %s'
                    valores = (cod,nom,clave1,clave2)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nMateria por Carrera Eliminada..")
                    time.sleep(0.5)
                    MatexCarrera()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Materias por Carrera..")
                    time.sleep(1)
                    MatexCarrera()
                    lu==1
                else:
                    print("Ingrese una opción válida.")




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar una materia por carrera!")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia que quiere actualizar\n(Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nu_pensum = %s and facultad = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Materia a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Materia no Encontrada.")
            MatexCarrera()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        #estos campos sí pueden ir nulos.   
        nom_estudiante = input("Nombre de estudiante en materia: ")
        matricula = input("Matricula de estudiante:  ")

        nu_pensum = clave1
        facultad = clave2

        #Actualizar en tabla materia 
        Comando = 'UPDATE materia SET codigo_materia = %s, nombre_materia = %s, creditos = %s, nu_pensum = %s, nu_sesion = %s, nombre_profesor = %s, apellido_profesor = %s, nombre_estudiante = %s, matricula_estudiante = %s, facultad = %s WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad, cod, nom)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nMateria Actualizada.")
        time.sleep(0.5)
        MatexCarrera()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def MatexEstudiante():
    time.sleep(0.5)
    print("\n-- MATERIAS (secciones) POR ESTUDIANTE --")
    print("\n Ingresa los siguientes datos del Estudiante:")
    print(" ")
    time.sleep(0.5)
    clave1 = input("Escriba el Nombre del Estudiante: ")
    clave2 = input("Escriba la Matricula: ")
    print(" ")

    #Buscar carrera primero 
    Comand = 'SELECT * FROM estudiante WHERE nombre = %s and matricula = %s'
    valores = (clave1, clave2)
    mycursor.execute(Comand,valores)
    Val =0
    for x in mycursor:
        print("Estudiante:")
        print(x)
        Val = Val+1
    if Val == 0:
        print("Estudiante no Encontrado.")
        MenuPrincipal()
        
        
    # Menu de opciones
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n MATERIAS POR ESTUDIANTE ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú Materias x Estudiante:


    # Registrar (1)===================
    if opci == 1:
        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar una Nueva Materia! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            nu_pensum = input ("Numero de Pensum: ")
            if not nu_pensum or nu_pensum ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==7:
            facultad = input ("Facultad: ")
            if not facultad or facultad ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
        
        nom_estudiante = clave1
        matricula = clave2

        #Insertar/Registar en tabla materia 
        
        Comando = 'INSERT INTO materia (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor, apellido_profesor, nombre_estudiante, matricula_estudiante, facultad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Materia x Estudiante Insertada")
        MatexEstudiante()
        



    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte una Materia. ")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        cred = input("Escriba los créditos de la materia: ")

        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and creditos = %s and nombre_estudiante =%s and matricula_estudiante = %s'
        valores = (cod,cred,clave1,clave2)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias por Estudiante? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias por Estudiante..")
                MatexEstudiante()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Materias por Estudiante Almacenadas: ")
        time.sleep(0.5)
        print(" ")
        Comand = 'SELECT * FROM materia WHERE nombre_estudiante = %s and matricula_estudiante = %s'
        valores = (clave1, clave2)
        mycursor.execute(Comand,valores)
        resultado = mycursor.fetchall()

        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias x Estudiante? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias x Estudiante..")
                MatexEstudiante()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar una Materia por Estudiante")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_estudiante = %s and matricula_estudiante = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")
            MatexEstudiante()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR esta Materia? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_estudiante = %s and matricula_estudiante = %s'
                    valores = (cod,nom,clave1,clave2)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nMateria por Estudiante Eliminada..")
                    time.sleep(0.5)
                    MatexEstudiante()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Materias por Estudiante..")
                    time.sleep(1)
                    MatexEstudiante()
                    lu==1
                else:
                    print("Ingrese una opción válida.")




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar una materia por estudiante!")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia que quiere actualizar\n(Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_estudiante = %s and matricula_estudiante = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Materia a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Materia no Encontrada.")
            MatexEstudiante()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nombre_profesor = input ("Nombre del profesor: ")
            if not nombre_profesor or nombre_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            apellido_profesor = input ("Apellido del profesor: ")
            if not apellido_profesor or apellido_profesor==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            nu_pensum = input ("Numero de Pensum: ")
            if not nu_pensum or nu_pensum ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==7:
            facultad = input ("Facultad: ")
            if not facultad or facultad ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
        
        nom_estudiante = clave1
        matricula = clave2

        #Actualizar en tabla materia 
        Comando = 'UPDATE materia SET codigo_materia = %s, nombre_materia = %s, creditos = %s, nu_pensum = %s, nu_sesion = %s, nombre_profesor = %s, apellido_profesor = %s, nombre_estudiante = %s, matricula_estudiante = %s, facultad = %s WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad, cod, nom)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nMateria Actualizada.")
        time.sleep(0.5)
        MatexEstudiante()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




def MatexProfesor():

    time.sleep(0.5)
    print("\n-- MATERIAS (secciones) POR PROFESOR --")
    print("\n Ingresa los siguientes datos del profesor:")
    print(" ")
    time.sleep(0.5)
    clave1 = input("Escriba el Nombre del Profesor: ")
    clave2 = input("Escriba el Apellido: ")
    print(" ")

    #Buscar carrera primero 
    Comand = 'SELECT * FROM profesor WHERE nombre = %s and apellido = %s'
    valores = (clave1, clave2)
    mycursor.execute(Comand,valores)
    Val =0
    for x in mycursor:
        print("Profesor:")
        print(x)
        Val = Val+1
    if Val == 0:
        print("Profesor no Encontrado.")
        MenuPrincipal()
        
        
    # Menu de opciones
    z = 0
    opci = 0

    while z == 0:
        time.sleep(1)
        print(" ")
        print("\n MATERIAS POR PROFESOR ")
        print(" ¿Qué Deseas Hacer? ")
        print("-Registrar (1) ")
        print("-Consultar (2) ")
        print("-Listar (3) ")
        print("-Eliminar (4) ")
        print("-Actualizar (5) ")
        print("-Ir al Menú Principal (6) ")
        opci = input("Selecciona una opción: ")
        try:
            opci = int(opci)
        except ValueError:
            opci = str(opci)
            time.sleep(0.5)
            print(" ")
            print("ERROR:")
            print("Ingrese un numero Entero")
            time.sleep(0.5)      


        if opci ==1 or opci ==2 or opci ==3 or opci ==4 or opci ==5 or opci ==6:
            z = z + 1 
        else:
            print("----")
            print("ingrese un número de opción válido.")
            print("----")




    # Opciones del menú Materias x Profesor:


    # Registrar (1)===================
    if opci == 1:
        y = 0
        time.sleep(0.5)
        print("\n Vamos a Registrar una Nueva Materia! ")
        time.sleep(0.5)
        print(" ")
        print("- Ingrese los siguientes Datos -")

        #While's para verificar que no sean Nulos
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nom_estudiante = input ("Nombre de un Estudiante: ")
            if not nom_estudiante or nom_estudiante==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            matricula = input ("Matricula del estudiante: ")
            if not matricula or matricula==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            nu_pensum = input ("Numero de Pensum: ")
            if not nu_pensum or nu_pensum ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==7:
            facultad = input ("Facultad: ")
            if not facultad or facultad ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
        
        nombre_profesor = clave1
        apellido_profesor = clave2

        #Insertar/Registar en tabla materia 
        
        Comando = 'INSERT INTO materia (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor, apellido_profesor, nombre_estudiante, matricula_estudiante, facultad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("Materia x Profesor Insertada")
        MatexProfesor()
        



    # Consultar (2)=======================
    elif opci == 2:
        time.sleep(0.5)
        Val = 0

        print("\n Consulte una Materia por Profesor. ")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        cred = input("Escriba los créditos de la materia: ")

        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and creditos = %s and nombre_profesor =%s and apellido_profesor = %s'
        valores = (cod,cred,clave1,clave2)
        mycursor.execute(Comand,valores)

        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")

        lu=0
        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias por Profesor? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias por Profesor..")
                MatexProfesor()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Listar (3)========================
    elif opci == 3:

        time.sleep(0.5)
        print("\n Listado de Materias por Profesor Almacenadas: ")
        time.sleep(0.5)
        print(" ")
        Comand = 'SELECT * FROM materia WHERE nombre_profesor = %s and apellido_profesor = %s'
        valores = (clave1, clave2)
        mycursor.execute(Comand,valores)
        resultado = mycursor.fetchall()

        for x in resultado:
            print(x)
            print(" ")
        
        lu=0

        while lu ==0:
            time.sleep(0.5)
            Res = input("Desea ir al Menú Materias x Profesor? (y/n): ")
            if Res == "y" or Res == "Y" or Res == "yes":
                print("De vuelta al Menú Materias x Profesor..")
                MatexProfesor()
                lu==1
            elif Res =="n" or Res == "N" or Res == "no":
                print("Finalizando Programa")
                sys.exit()
                lu==1
            else:
                print("Ingrese una opción válida.")




    # Eliminar (4)==============
    elif opci == 4:
        
        time.sleep(0.5)
        print("\nEliminar una Materia por Profesor")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia (Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_profesor = %s and apellido_profesor = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)

        Val =0
        for x in mycursor:
            print(x)
            Val = Val+1

        if Val == 0:
            print("Materia no Encontrada.")
            MatexProfesor()

        if Val > 0:
            lu = 0
            while lu ==0:
                time.sleep(0.5)
                Res = input("\n¿Seguro que desea ELIMINAR esta Materia? (y/n): ")
                if Res == "y" or Res == "Y" or Res == "yes":
                    #Eliminando
                    Comand = 'DELETE FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_profesor = %s and apellido_profesor = %s'
                    valores = (cod,nom,clave1,clave2)
                    mycursor.execute(Comand,valores)

                    db.commit()  #Guardar permanentemente
                    print("\nMateria por Profesor Eliminada..")
                    time.sleep(0.5)
                    MatexProfesor()
                    lu==1

                elif Res =="n" or Res == "N" or Res == "no":
                    print("\nDe vuelta al Menú Materias por Profesor..")
                    time.sleep(1)
                    MatexProfesor()
                    lu==1
                else:
                    print("Ingrese una opción válida.")




    #Actualizar (5) ================
    elif opci ==5:
        time.sleep(0.5)
        print("\nVamos a actualizar una materia por profesor!")
        print(" ")
        time.sleep(0.5)
        cod = input("Escriba el código de la Materia que quiere actualizar\n(Con número de sección): ")
        nom = input("Escriba el nombre de la materia: ")
        print(" ")

        #Buscar materia primero
        Comand = 'SELECT * FROM materia WHERE codigo_materia= %s and nombre_materia = %s and nombre_profesor = %s and apellido_profesor = %s'
        valores = (cod,nom,clave1,clave2)
        mycursor.execute(Comand,valores)
        Val =0
        for x in mycursor:
            print("Materia a Actualizar:")
            print(x)
            Val = Val+1
        if Val == 0:
            print("Materia no Encontrada.")
            MatexProfesor()
        

        time.sleep(0.1)
        print("\n- Ingrese los siguientes Datos -")
        
        y=0
        while y ==0:
            codigo_materia = input ("Código (incluyendo numero de sección): ")
            if not codigo_materia or codigo_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
                
        while y ==1:
            nombre_materia = input("Nombre de la Materia:  ")
            if not nombre_materia or nombre_materia==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==2:
            creditos = input ("Cantidad de Créditos: ")
            if not creditos or creditos==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==3:
            nu_sesion = input ("Sección: ")
            if not nu_sesion or nu_sesion==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==4:
            nom_estudiante = input ("Nombre de un Estudiante: ")
            if not nom_estudiante or nom_estudiante==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==5:
            matricula = input ("Matricula del estudiante: ")
            if not matricula or matricula==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==6:
            nu_pensum = input ("Numero de Pensum: ")
            if not nu_pensum or nu_pensum ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1

        while y ==7:
            facultad = input ("Facultad: ")
            if not facultad or facultad ==" ":
                print("Ingrese un campo.")
            else:
                y= y+1
        
        nombre_profesor = clave1
        apellido_profesor = clave2

        #Actualizar en tabla materia 
        Comando = 'UPDATE materia SET codigo_materia = %s, nombre_materia = %s, creditos = %s, nu_pensum = %s, nu_sesion = %s, nombre_profesor = %s, apellido_profesor = %s, nombre_estudiante = %s, matricula_estudiante = %s, facultad = %s WHERE codigo_materia= %s and nombre_materia = %s'
        valores = (codigo_materia, nombre_materia, creditos, nu_pensum, nu_sesion, nombre_profesor,apellido_profesor, nom_estudiante, matricula, facultad, cod, nom)
        mycursor.execute(Comando,valores)

        db.commit()  #Guardar permanentemente
        print("\nMateria Actualizada.")
        time.sleep(0.5)
        MatexProfesor()
        

    else:
        time.sleep(0.5)
        print("De vuelta al menú principal")
        MenuPrincipal()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




#Llamada al Sistema
Login()




'''

      <  F i n  >
Autor: Evelyn Carolina Jorge
Matricula: 20-0084
EXAMEN FINAL

'''