import random
import string
import os

admin = "Admin"
admin_password = "1234"  # Creación de las credenciales de acceso del Admin

#moods para cada usuario manejados por booleanos
admin_mood = False
modo_registro = False
modo_ver_registrados = False
aprendiz_mood = False
invitado_mood = False 
login_exitoso = False
recuperar = False

caracteres = string.ascii_letters + string.digits #lista que almacena caracteres para hacer la contraseña

aprendices = 20
raciones = 5
salir_registro = False
no_registrar = False
intentos_login = 3  # Inicialización de variables que se irán utilizando en el programa

aprendices_info = [] #aquí se almacenará la info de cada aprendiz, nested list
aprendices_bloqueados = []
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
raciones_tomadas = [0] * len(dias_semana)  # Contador de raciones tomadas para cada día


while True:
    os.system('cls')
    print("**Bienvenido al Sistema de Gestión de Entrega de Almuerzo SIGEA**")
    print("1. Administrador.")
    print("2. Aprendíz.")
    print("3. Invitado.")
    print("4. Salir.")
    interaccion = input("Digite su tipo de usuario para continuar:")

    if interaccion == "4":
        print("\nHasta la próxima.")
        break
    elif interaccion == "1":  # Ingreso del Admin
        for admin_intento in range(3):
            os.system('cls')
            user = input("Ingrese su usuario de administrador:")
            password = input("Ingrese su contraseña:")
            if user == admin and password == admin_password:
                os.system('cls')
                print("Bienvenido Admin.")
                print("\n" * 1)
                admin_mood = True  # Establecer admin_mood en True después de un inicio de sesión exitoso
                break  # Salir del bucle de inicio de sesión del administrador
            else:
                print("\nSu usuario o contraseña son inválidos")
                if admin_intento < 2:
                    print("Intente nuevamente")
                else:
                    print("Número de intentos limitados.")
        if admin_mood: # Se comenzará a ejecutar la opciones del admin cuando las credenciales sean verdaderas para admin
            while True: # pero se mostraran las opciones utilizando un while true, o sea mientras sean verdad las credenciales
                print("**Opciones de Administrador**")
                print("1. Registrar Aprendíz") #LISTO
                print("2. Consultar Aprendices Registrados") #LISTO
                print("3. Modificar un registro") #LISTO
                print("4. Desbloquear usuario por ingreso erróneo")
                print("5. Actualización de Menú")
                print("6. Reasignación de Semanas")
                print("7. Eliminar Aprendíz")
                print("8. Salir") #LISTO
                opcion_admin = input("Seleccione una opción:")
                if opcion_admin == "8":
                    admin_mood = False
                    print("\nSaliendo del modo Administrador")
                    print("\n")
                    break  # Salir del modo administrador
                elif opcion_admin == "7":
                    print("\nEliminar Aprendíz")
                    #Ahorita hago ese codigo 
                elif opcion_admin == "6":
                    print("Reasignación de Semanas")
                elif opcion_admin == "5":
                    print("Actualización de Menú")
                elif opcion_admin == "4":
                    print("\n" * 5)
                    print("Desbloquear usuario por ingreso erróneo") #VGbOjYcX
                    if aprendices_bloqueados:
                        for bloqueado in aprendices_bloqueados:
                            print(aprendiz_bloqueado)
                        else:
                            print("No se ha encontrados ningún usuario bloqueado")
                    os.system('cls')
                    
                elif opcion_admin == "3":
                    os.system('cls')
                    print("Modificar Usuario")
                    print("\n" * 1)
                    indice = int(input("Ingrese el índice del usuario a modificar (1-20):"))
                    if 1 <= indice <= len(aprendices_info):#devuelve la contidad de usuarios registrados 
                        datos_aprendiz =aprendices_info[indice - 1]
                        print(f"Usuario seleccionado: {datos_aprendiz[0]} {datos_aprendiz[1]}")
                        print("Ingrese los nuevos datos (deje en blanco si desea mantener el dato actual): ")
                        datos_aprendiz[0] = input(f"Nuevo nombre ({datos_aprendiz[0]}): ").strip() or datos_aprendiz[0]
                        datos_aprendiz[1] = input(f"Nuevo apellido ({datos_aprendiz[1]}): ").strip() or datos_aprendiz[1]
                        datos_aprendiz[2] = input(f"Nuevo ID ({datos_aprendiz[2]}): ").strip() or datos_aprendiz[2]
                        datos_aprendiz[3] = input(f"Nuevo programa ({datos_aprendiz[3]}): ").strip().lower() or datos_aprendiz[3].lower()
                        while datos_aprendiz[3] not in ["adso", "cocina", "multimedia", "gestión empresarial", "modistería", "animación 3d", "ganadería", "gestión administrativa"]:
                            print("Por favor ingrese uno de los programas permitidos (ADSO, COCINA, MULTIMEDIA, GESTIÓN EMPRESARIAL, ANIMACIÓN 3D, GANADERÍA, MODISTERÍA O GESTIÓN EMPRESARIAL).")
                            datos_aprendiz[3] = input("Vuelva a intentarlo: ").strip().lower()
                        datos_aprendiz[4] = input(f"Nuevo Correo Electrónico ({datos_aprendiz[4]}): ").strip() or datos_aprendiz[4]
                        print(f"\n¡Datos actualizados correctamente para {datos_aprendiz[0]} {datos_aprendiz[1]}!")
                        print("\n")
                    else:
                        print("Índice inválido. Intente nuevamente.")
                elif opcion_admin == "2":
                    os.system('cls')
                    print("Consultar Usuarios")
                    if aprendices_info:  # Aquí se chequea que haya aprendices registrados
                        print("\n**Listado de Aprendices Registrados:**")
                        for aprendiz_numero, datos_aprendiz in enumerate(aprendices_info, 1):
                            print(f"\n**Aprendiz {aprendiz_numero}:**")
                            print(f"Nombre: {datos_aprendiz[0]}")
                            print(f"Apellido: {datos_aprendiz[1]}")
                            print(f"ID: {datos_aprendiz[2]}")
                            print(f"Programa: {datos_aprendiz[3]}")
                            print(f"Email: {datos_aprendiz[4]}")
                            print(f"Contraseña: {datos_aprendiz[5]}")
                            print(f"Usuario: {datos_aprendiz[6]}")
                            print(f"Semana de Alimentación: {datos_aprendiz[7]}")                 
                        input("\nPresione Enter para regresar al menú del administrador ")
                        os.system('cls')
                    else:
                        print("\nNo hay aprendices registrados.")
                elif opcion_admin == "1":
                    os.system('cls')
                    print("\nRegistrar Usuarios")
                    modo_registro = True #trabajar con modo ayuda a que el momento de querer salir de x o y función el ciclo en el que se esté se cierre y no hayan repeticiones
                    salir_modo_registro = False
                    for aprendiz_numero in range(1, aprendices + 1):
                        while modo_registro and len(aprendices_info) < aprendices:
                            datos_aprendiz = [] #Se iran almacenando los datos de cada aprendiz
                            datos_aprendiz.append(input("Ingrese primer y segundo nombre del aprendiz: "))  #Yy6NHQcI
                            datos_aprendiz.append(input("Ingrese el primer apellido del aprendíz: "))
                            datos_aprendiz.append(input(f"Ingrese el número de documento del aprendíz: "))
                            datos_aprendiz.append(input(f"Ingrese el programa de formación del aprendíz (ADSO, GESTIÓN ADMINISTRATIVA, COCINA, ANIMACIÓN 3D, MULTIMEDIA, GESTIÓN EMPRESARIAL O MODISTERÍA): "))
                            while datos_aprendiz[-1].lower() not in ["adso", "cocina", "multimedia", "gestión empresarial", "modistería", "animación 3d","ganadería", "gestión administrativa"]:
                                print("\n")
                                print("Por favor ingrese uno de los programas permitidos (ADSO, COCINA, MULTIMEDIA, GESTIÓN EMPRESARIAL, ANIMACIÓN 3D, GANADERÍA, MODISTERÍA O GESTIÓN EMPRESARIAL).")
                                print("Vuelva a intentarlo.")
                                print("\n")
                                datos_aprendiz[-1] = input(f"Ingrese el programa de formación del aprendíz (ADSO, GESTIÓN ADMINISTRATIVA, COCINA, ANIMACIÓN 3D, MULTIMEDIA, MODISTARÍA, GESTIÓN EMPRESARIAL O MODISTERÍA): ")
                            datos_aprendiz.append(input("Ingrese el correo electrónico del aprendíz: ")) 
                            contrasena = ''.join(random.sample(caracteres, 8)) #generación de la contraseña para el aprendiz registrado
                            datos_aprendiz.append(contrasena) 
                            
                            partes_nombre = datos_aprendiz[0].split()
                            primera_letra_primer_nombre = partes_nombre[0][0].lower()
                            primera_letra_segundo_nombre = partes_nombre[1][0].lower()
                            apellido = datos_aprendiz[1].lower()
                            usuario_formado = primera_letra_primer_nombre + primera_letra_segundo_nombre + "_" + apellido
                            usuario = usuario_formado
                            contador = 1
                            usuarios_creados = [aprendiz[6] for aprendiz in aprendices_info] #1rJTxS4W
                            while usuario in usuarios_creados:
                                usuario = usuario_formado + str(contador)
                                contador += 1
                            datos_aprendiz.append(usuario)
                            aprendices_info.append(datos_aprendiz) #agregando la informacion (que se guardó en datos_aprendiz) a aprendices_infor <<lista anidada
                            exito = print(f"\n¡El aprendiz {datos_aprendiz[0]} {datos_aprendiz[1]} ha sido registrado exitosamente!")   
                            print("\n" * 3)
                            if datos_aprendiz[3].lower() in ("adso", "gestión administrativa"):
                                semana_alimentacion = 1
                            elif datos_aprendiz[3].lower() in ("gestión empresarial", "animación 3d"):
                                semana_alimentacion = 2
                            elif datos_aprendiz[3].lower() in ("multimedia", "modistería"):
                                semana_alimentacion = 3
                            elif datos_aprendiz[3].lower() in ("cocina", "ganadería"):
                                semana_alimentacion = 4
                            else:
                                print("\nNo se ha encontrado una semana asignada")
                            datos_aprendiz.append(semana_alimentacion)
                            continuar_registro = input("Continuar registrando? (si/no): ")
                            if continuar_registro.lower() == "si":
                                no_continuar = False
                                print("\n" * 1)
                            elif continuar_registro.lower() == "no":
                                modo_registro = False
                                salir_modo_registro = True
                                os.system('cls')
                                print("Saliendo de Registro...")
                                print("\n" * 1)
                                break
                            else:
                                print("Por favor ingrese una opción para continuar")
                elif opcion_admin != ("1","2","3","4","5","6","7"):
                    print("Opción invalida")
                    print("Digite una opción valida entre los números 1 y 7")
                else:
                    print("ERROR: Digite por favor una opción para continuar")
    elif interaccion == "2":  # Ingreso del APRENDIZ
        os.system('cls')
        print("**Opciones del aprendíz**")
        print("1. Iniciar Sesión") #LISTO
        print("2. Registrarse")
        print("3. Ver y/o Recuperar Contraseña/Usuario") #LISTO
        print("4. Cambiar Contraseña") #LISTO
        interaccion_aprendiz = input("Escriba el número la opción en que desea continuar: ") 
        if interaccion_aprendiz == "4":
            os.system('cls')
            print("**Cambiar Contraseña**")
            id_aprendiz = input("Ingrese su documento: ")
            id_contrasena_antigua = input("Ingrese su antigua contraseña: ")
            encontrado = False
            print("\nCambiando contraseña:")
            for i in aprendices_info:
                if id_aprendiz == i[2]:
                    if id_contrasena_antigua == i[5]:
                        nueva_contrasena = input("Escriba su nueva contraseña: ") #EsiGfvZQ
                        i[5] = nueva_contrasena
                        print(f"Aprendíz: {i[0]} Su nueva contraseña es: {nueva_contrasena}")
                        encontrado = True
                    else:
                        print("Contraseña antigua incorrecta.")
                    break
            if not encontrado:
                print("Documento no encontrado.")
            input("Presione Enter para regresar al menú principal.")
            os.system('cls')
        elif interaccion_aprendiz == "3":
            os.system('cls')
            print("**Ver y/o Recuperar Contraseña/Usuario**")
            id_aprendiz = input("Ingrese su documento: ")
            encontrado = False
            for i in aprendices_info:
                print(f"Documento registrado: {i[2]}")
                if id_aprendiz == i[2]:  
                    print(f"La contraseña para el documento {id_aprendiz} es: {i[5]}") #i[5] vendría siendo la contraseña, i es la variable que está iterando los datos en aprendices_info
                    print(f"El usuario es {i[6]}.")
                    encontrado = True
                    break
            if not encontrado:
                print("Documento no encontrado.")
            input("Presione Enter para regresar al menú principal.")
            os.system('cls')
            
        elif interaccion_aprendiz == "2":
            os.system('cls')
            print("**Registrarse**")
            if len(aprendices_info) < 20:
                datos_aprendiz = []
                datos_aprendiz.append(input("Ingrese su primer y segundo nombre: "))
                datos_aprendiz.append(input("Ingrese su primer apellido: "))
                datos_aprendiz.append(input(f"Ingrese su número de documento: "))
                datos_aprendiz.append(input(f"Ingrese el programa de formación del aprendiz (ADSO, GESTIÓN ADMINISTRATIVA, COCINA, ANIMACIÓN 3D, MULTIMEDIA, GESTIÓN EMPRESARIAL O MODISTERÍA): "))
                while datos_aprendiz[-1].lower() not in ["adso", "cocina", "multimedia", "gestión empresarial", "modistería", "animación 3d", "ganadería", "gestión administrativa"]:
                    print("\n")
                    print("Por favor ingrese uno de los programas permitidos (ADSO, COCINA, MULTIMEDIA, GESTIÓN EMPRESARIAL, ANIMACIÓN 3D, GANADERÍA, MODISTERÍA O GESTIÓN EMPRESARIAL).")
                    print("Vuelva a intentarlo.")
                    print("\n")
                    datos_aprendiz[-1] = input(f"Ingrese el programa de formación del aprendiz (ADSO, GESTIÓN ADMINISTRATIVA, COCINA, ANIMACIÓN 3D, MULTIMEDIA, MODISTERÍA, GESTIÓN EMPRESARIAL O MODISTERÍA): ")
                datos_aprendiz.append(input("Ingrese el correo electrónico del aprendiz: "))
                contrasena = ''.join(random.sample(caracteres, 8))  # Generación de la contraseña para el aprendiz registrado
                datos_aprendiz.append(contrasena)
                
                partes_nombre = datos_aprendiz[0].split()
                primera_letra_primer_nombre = partes_nombre[0][0].lower()
                primera_letra_segundo_nombre = partes_nombre[1][0].lower()
                apellido = datos_aprendiz[1].lower()
                usuario_formado = primera_letra_primer_nombre + primera_letra_segundo_nombre + "_" + apellido
                usuario = usuario_formado
                contador = 1
                usuarios_creados = [aprendiz[6] for aprendiz in aprendices_info]
                while usuario in usuarios_creados:
                    usuario = usuario_formado + str(contador)
                    contador += 1
                datos_aprendiz.append(usuario)
                
                # Determinar la semana de alimentación según el programa
                if datos_aprendiz[3].lower() in ("adso", "gestión administrativa"):
                    semana_alimentacion = 1
                elif datos_aprendiz[3].lower() in ("gestión empresarial", "animación 3d"):
                    semana_alimentacion = 2
                elif datos_aprendiz[3].lower() in ("multimedia", "modistería"):
                    semana_alimentacion = 3
                elif datos_aprendiz[3].lower() in ("cocina", "ganadería"):
                    semana_alimentacion = 4
                else:
                    print("\nNo se ha encontrado una semana asignada")
                    semana_alimentacion = None  # Puedes ajustar esto según sea necesario
                
                datos_aprendiz.append(semana_alimentacion)
                aprendices_info.append(datos_aprendiz)  # Asegurarse de agregar los datos del aprendiz a la lista
                
                print(f"\n¡El aprendiz {datos_aprendiz[0]} {datos_aprendiz[1]} ha sido registrado exitosamente!")
                input("Presione Enter para regresar al menú principal.")
                os.system('cls')
            else:
                print("No hay cupo disponible para nuevos registros.")
                input("Presione Enter para regresar al menú principal.")
                os.system('cls')      
        elif interaccion_aprendiz == "1":
            login_exitoso = False
            for aprendiz_intento in range(3):
                os.system('cls')
                user = input("Ingrese su usuario de aprendíz:")
                password = input("Ingrese su contraseña:")
                for aprendiz_dato in aprendices_info:
                    if user == aprendiz_dato[6] and password == aprendiz_dato[5]: 
                        os.system('cls')
                        print("Bienvenido Aprendíz.")
                        print("\n" * 1)
                        aprendiz_mood = True #Se establece en true para saber que está entrando al modo aprendiz
                        login_exitoso = True
                        break #esto sirve para salir de ciclo para el logeo del aprendiz
                if login_exitoso:
                    break
                else:
                    print("\nSu usuario o contraseña son inválidos")
                    if aprendiz_intento < 2:
                        print("Intente nuevamente")
                    else:
                        print("\nSus credenciales de acceso al sistema han sido bloqueadas")
                        aprendiz_bloqueado = f"{aprendiz_dato[0]} {aprendiz_dato[1]}"
                        aprendices_bloqueados.append(aprendiz_bloqueado)
                        input("Presione Enter para regresar al menú principal.")
                        os.system('cls')
            if login_exitoso:
                print(f"\nSeñor(a) {aprendiz_dato[0]} {aprendiz_dato[1]}, su semana de alimentación es la semana no. {aprendiz_dato[7]} ")
                print(f"El número de raciones que usted tiene disponibles es {raciones}")
                print("\n")
                print("Semana 1: alimentación para el programa de ADSO, GESTION ADMINISTRATIVA")  #i7eWEXI9
                print("Semana 2: alimentación para el programa de GESTION EMPRESARIAL, ANIMACION 3D")
                print("Semana 3: alimentación para el programa de MULTIMEDIA, MODISTERIA")
                print("Semana 4: alimentación para el programa de COCINA, GANADERIA")
                print("\n")
                ver_menu = input("¿Desea ver el menú?: ")
                if ver_menu.lower() == "no":
                    print("Continuando...")
                elif ver_menu.lower() == "si":
                    print("\nMenú Semanal de Almuerzos")
                    print("=" * 40)
                    print("Lunes: Sopa de Lentejas con Arroz, Arepa, y Ensalada")
                    print("Martes: Ajiaco Santafereño con Pollo y Guasca, acompañado de Arroz y Aguacate")
                    print("Miércoles: Bandeja Paisa: Arroz, Frijoles, Carne Molida, Chicharrón, Plátano, Arepa, y Huevo Frito")
                    print("Jueves: Sancocho de Gallina con Papa, Yuca, y Plátano, acompañado de Arroz y Aguacate")
                    print("Viernes: Cazuela de Mariscos con Arroz y Patacones")
                    print("=" * 40)
                for dia in range(len(dias_semana)):
                    dia_semana = dias_semana[dia]
                    respuesta = input(f"¿Desea tomar su ración de almuerzo para el {dia_semana.capitalize()}? (si/no): ")
                    if respuesta.lower() == "si":
                        raciones_tomadas[dia] += 1
                        raciones -= 1
                        os.system('cls')
                        print(f"\nSus raciones restantes son {raciones}.")
                        print(f"Puede pasar a reclamar su almuerzo para el {dia_semana.capitalize()}.")
                    elif respuesta.lower() == "no":
                        raciones_tomadas[dia] += 1
                        raciones -= 1
                        print(f"\nSus raciones restantes son {raciones}.")
                        print(f"Como no tomó su almuerzo el día de hoy {dia_semana.capitalize()}, su ración será reasignada.")
                        # Reasignar ración a otro aprendiz
                        reasignada = False
                        print("Hasta el próximo almuerzo")
                    else:
                        print("Por favor ingrese 'si' o 'no'.")
    
                    input("\nPresione Enter para continuar al siguiente día.")
                    if raciones == 0:
                        break
                    os.system('cls')   