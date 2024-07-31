import random
import string
import os
from datetime import datetime
import re
#definiendo fecha de inicio
fecha_inicio = datetime(2024, 7, 29)
caracteres = string.ascii_letters + string.digits  # Lista que almacena caracteres para hacer la contraseña
regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # variable con la que se realizará la validación del email
admin = "Admin"
admin_password = "1234"  # Creación de las credenciales de acceso del Admin
# Moods para cada usuario manejados por booleanos
admin_mood = False
modo_registro = False
modo_ver_registrados = False
aprendiz_mood = False
invitado_mood = False
login_exitoso = False
recuperar = False
salir_registro = False
no_registrar = False
# Inicialización de variables enteras que se irán utilizando en el programa
aprendices = 20
raciones = 5
intentos_login = 3  
aprendiz_intento = 0
max_intentos = 3
# Aquí se almacenará la info de cada aprendiz, menus y otras listas
aprendices_info = []  
aprendices_bloqueados = []
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
raciones_tomadas = [0] * len(dias_semana)  # Contador de raciones tomadas para cada día
menu_actual = [
    "Sopa de Lentejas con Arroz, Arepa, y Ensalada",
    "Ajiaco Santafereño con Pollo y Guasca, acompañado de Arroz y Aguacate",
    "Bandeja Paisa: Arroz, Frijoles, Carne Molida, Chicharrón, Plátano, Arepa, y Huevo Frito",
    "Sancocho de Gallina con Papa, Yuca, y Plátano, acompañado de Arroz y Aguacate",
    "Cazuela de Mariscos con Arroz y Patacones"
]
#Se inicia un ciclo infinito mientras que sea no sea "4"
while True:
    os.system('cls')
    print("**Bienvenido al Sistema de Gestión de Entrega de Almuerzo SIGEA**")
    print("1. Administrador.")
    print("2. Aprendíz.")
    print("3. Invitado.")
    print("4. Salir.")
    interaccion = input("Digite un número para continuar: ")
    if interaccion == "4":
        print("\nHasta la próxima.")
        break
    # Ingreso del Admin
    elif interaccion == "1":  
        for admin_intento in range(3):
            os.system('cls')
            user = input("Ingrese su usuario de administrador:")
            password = input("Ingrese su contraseña:")
            if user == admin and password == admin_password:
                os.system('cls')
                print("***Bienvenido Admin***")
                print("\n" * 1)
                # Establecer admin_mood en True después de un inicio de sesión exitoso
                admin_mood = True  
                break  # Salir del bucle de inicio de sesión del administrador
            else:
                print("\nSu usuario o contraseña son inválidos")
                if admin_intento < 2:
                    print("Intente nuevamente")
                else:
                    print("Número de intentos limitados.")
                input("Presione Enter para continuar...")  # Agregar una pausa
        # Se comenzará a ejecutar la opciones del admin cuando las credenciales sean verdaderas para admin
        if admin_mood: 
            while True: # pero se mostraran las opciones utilizando un while true, o sea mientras sean verdad las credenciales
                print("**Opciones de Administrador**")
                print("1. Registrar Aprendíz") #LISTO
                print("2. Consultar Aprendices Registrados") #LISTO
                print("3. Modificar un registro") #LISTO
                print("4. Desbloquear usuario por ingreso erróneo")#listo
                print("5. Actualización de Menú")#LISTO
                print("6. Reasignación de Semanas")
                print("7. Eliminar Aprendíz")#LISTO
                print("8. Salir") #LISTO
                opcion_admin = input("Seleccione una opción:")
                os.system('cls')
                # Salir del modo administrador
                if opcion_admin == "8":
                    admin_mood = False
                    print("\nSaliendo del modo Administrador")
                    print("\n")
                    break  
                elif opcion_admin == "7":
                    print("\n**Eliminar Aprendíz**")
                    if len(aprendices_info) == 0:#si el tamaño de lo que hay dentro de la lista aprendices_info es 0, esto quiere decir que no hay a quien eliminar
                        print("\nNo hay aprendices para eliminar.")
                        input("\nPresione Enter para continuar...")
                        continue
                    print("\nEliminar Aprendiz:")
                    for i, aprendiz in enumerate(aprendices_info, 1):
                        print(f"{i}. ID: {aprendiz[2]}, Nombre: {aprendiz[0]} {aprendiz[1]}, Email: {aprendiz[4]}")
                        indice_valido = False #verifica que el siguiente while se ejecute mientras el indice sea falso
                    while not indice_valido: #mientras que no
                        indice_eliminar = input("\nIngrese el número del aprendiz a eliminar: ")
                        if indice_eliminar.isdigit():#lo convierte a digito
                            indice_eliminar = int(indice_eliminar) - 1#recordemos que se comienza a contar desde el indice 0
                            if 0 <= indice_eliminar < len(aprendices_info): #si zero es menor o igual que indice a eliminar y menor que el tamaño que se encuentra en aprendices_info
                                indice_valido = True
                                aprendiz_eliminado = aprendices_info.pop(indice_eliminar) #con la funcionalidad de pop elimino a la informacion del aprendiz por el indice que se está dando
                                print(f"Aprendiz '{aprendiz_eliminado[1]}' eliminado exitosamente.") #sucess
                            else:
                                print("Índice fuera de rango. Intente nuevamente.")
                        else:
                            print("Entrada inválida. Por favor, ingrese un número.")
                    input("\nPresione Enter para continuar...")
                    os.system('cls')
                elif opcion_admin == "6":
                    print("Reasignación de Semanas") #tengo que hacer esto
                #Actualización de MENU
                elif opcion_admin == "5":
                    os.system('cls')
                    print("\nActualización de Menú Semanal de Almuerzos")
                    print("=" * 40)
                    for i, plato in enumerate(menu_actual): #enumerate sirve para sacar el indice y algun dato de un iterable
                        print(f"{i+1}. {plato}")
                    opcion = input("\n¿Desea actualizar el menú? (si/no): ")
                    if opcion.lower() == "si":
                        for i in range(len(menu_actual)):#imprimirá el numero de elementos que haya en la lista
                            print("Si no desea cambiar el menú del día, solo presione Enter sin ingresar ningún valor")
                            nuevo_plato = input(f"Ingrese el nuevo plato para el día {i+1} (actual: {menu_actual[i]}): ")
                            if nuevo_plato:#se verifica que plato no está vacio
                                menu_actual[i] = nuevo_plato #reasignacion del nuevo plato en el indice, para la lista menu_actual
                        input("Pulse enter para continuar")
                        os.system('cls')
                elif opcion_admin == "4":
                    os.system('cls')
                    print("\nDesbloquear usuario por ingreso erróneo") #VGbOjYcXprint
                    print("**Lista de aprendices bloqueados**")
                    if aprendices_bloqueados:
                        for i, bloqueado in enumerate(aprendices_bloqueados, start=1):
                            print(f"{i}. {bloqueado}")
                        #El admin eligir´pa cual usuario se va a desbloquear
                        try:
                            seleccion = int(input("Ingrese el número del usuario que desea desbloquear: ")) - 1
                            if 0 <= seleccion < len(aprendices_bloqueados):
                                usuario_a_desbloquear = aprendices_bloqueados.pop(seleccion)
                                print(f"Usuario a desbloquear: {usuario_a_desbloquear}")
                                # Buscar el usuario en aprendices_info y restaurar su contraseña original si es necesario
                                for aprendiz in aprendices_info:
                                    if aprendiz[6] == usuario_a_desbloquear:
                                        documento = aprendiz[2]
                                        aprendiz[5] = documento  # Cambiar a la contraseña que quieras asignar por defecto
                                        desbloqueado = True
                                        print(f"El usuario {usuario_a_desbloquear} ha sido desbloqueado y su contraseña ha sido cambiada al número de documento.")
                                        break
                                else:
                                    print("El usuario no se ha encontrado en la lista de aprendices")
                            else:
                                print("Selección inválida.")
                        except ValueError:
                            print("Por favor, ingrese un número valido.")
                    else:                     
                        print("No hay aprendices bloqueados aun")
                    print("\n" * 3)
                    input("Enter para continuar")
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
                            print(f"Nombre: {datos_aprendiz[0]} {datos_aprendiz[1]}")
                            print(f"Apellido: {datos_aprendiz[2]}")
                            print(f"ID: {datos_aprendiz[3]}")
                            print(f"Programa: {datos_aprendiz[4]}")
                            print(f"Email: {datos_aprendiz[5]}")
                            print(f"Contraseña: {datos_aprendiz[6]}")
                            print(f"Usuario: {datos_aprendiz[7]}")
                            print(f"Semana de Alimentación: {datos_aprendiz[8]}")                 
                        input("\nPresione Enter para regresar al menú del administrador ")
                        os.system('cls')
                    else:
                        print("\nNo hay aprendices registrados.")
                        print("\n" * 3)
                elif opcion_admin == "1":
                    os.system('cls')
                    print("\nRegistrar Usuarios")
                    modo_registro = True
                    salir_modo_registro = False
                    while modo_registro and len(aprendices_info) < aprendices:
                        datos_aprendiz = []
                        datos_aprendiz.append(input("Ingrese primer nombre del aprendíz: "))
                        datos_aprendiz.append(input("Ingrese el segundo nombre del aprendiz: "))
                        datos_aprendiz.append(input("Ingrese el primer apellido del aprendíz: "))
                        datos_aprendiz.append(input("Ingrese el número de documento del aprendíz: "))
                        while True:
                            print("Seleccione el programa de formación del aprendiz: ")
                            print("1. ADSO")
                            print("2. Gestión Administrativa")
                            print("3. Cocina")
                            print("4. Animación 3D")
                            print("5. Multimedia")
                            print("6. Modistería")
                            print("7. Gestión Empresarial")
                            print("8. Ganadería")
                            try:
                                programa = int(input("Escriba el número del programa del aprendiz para continuar: "))
                                if 1 <= programa <= 8:
                                    datos_aprendiz.append(
                                        "ADSO" if programa == 1 else
                                        "Gestión Administrativa" if programa == 2 else
                                        "Cocina" if programa == 3 else
                                        "Animación 3D" if programa == 4 else
                                        "Multimedia" if programa == 5 else
                                        "Modistería" if programa == 6 else
                                        "Gestión Empresarial" if programa == 7 else
                                        "Ganadería"
                                    )
                                    break
                                else:
                                    print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
                            except ValueError:
                                print("Debe ingresar un número entero.")
                        while True:
                            correo = (input("Ingrese el correo electrónico del aprendíz: ")) 
                            if re.match(regex, correo):
                                datos_aprendiz.append(correo)
                                break
                            else:
                                print("Correo Invalido, por favor intente nuevamente")
                        contrasena = ''.join(random.sample(caracteres, 8))
                        datos_aprendiz.append(contrasena) 
                        primera_letra_primer_nombre = datos_aprendiz[0][0].lower()
                        primera_letra_segundo_nombre = datos_aprendiz[1][0].lower()
                        apellido = datos_aprendiz[2].lower()
                        usuario_formado = primera_letra_primer_nombre + primera_letra_segundo_nombre + "_" + apellido
                        usuario = usuario_formado
                        contador = 1
                        usuarios_creados = [aprendiz[6] for aprendiz in aprendices_info]
                        while usuario in usuarios_creados:
                            usuario = usuario_formado + str(contador)
                            contador += 1
                        datos_aprendiz.append(usuario)
                        aprendices_info.append(datos_aprendiz)
                        print(f"\n¡El aprendiz {datos_aprendiz[0]} {datos_aprendiz[2]} ha sido registrado exitosamente!")
                        print("\n" * 3)
                        if datos_aprendiz[4].lower() in ("adso", "gestión administrativa"):
                            semana_alimentacion = 1
                        elif datos_aprendiz[4].lower() in ("gestión empresarial", "animación 3d"):
                            semana_alimentacion = 2
                        elif datos_aprendiz[4].lower() in ("multimedia", "modistería"):
                            semana_alimentacion = 3
                        elif datos_aprendiz[4].lower() in ("cocina", "ganadería"):
                            semana_alimentacion = 4
                        else:
                            print("\nNo se ha encontrado una semana asignada")
                        datos_aprendiz.append(semana_alimentacion)
                        while True:
                            continuar_registro = input("Continuar registrando? (si/no): ").lower()
                            if continuar_registro == "si":
                                break
                            elif continuar_registro == "no":
                                modo_registro = False
                                salir_modo_registro = True
                                os.system('cls')
                                print("Saliendo de Registro...")
                                print("\n" * 1)
                                break
                            else:
                                print("Por favor ingrese una opción para continuar")
                        if salir_modo_registro:
                            break
                elif opcion_admin != ("1","2","3","4","5","6","7","8"):
                    print("Opción invalida")
                    print("Digite una opción valida entre los números 1 y 8")
                else:
                    print("ERROR: Digite por favor una opción para continuar")
    elif interaccion == "2":  # Ingreso del APRENDIZ
        os.system('cls')
        print("**Opciones del aprendiz**")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Ver y/o Recuperar Contraseña/Usuario")
        print("4. Cambiar Contraseña")
        print("5. Salir")
        interaccion_aprendiz = input("Escriba el número de la opción en que desea continuar: ") 
        if interaccion_aprendiz == "5":
            breakpoint
        elif interaccion_aprendiz == "4":
            os.system('cls')
            print("**Cambiar Contraseña**")
            id_aprendiz = input("Ingrese su documento: ")
            id_contrasena_antigua = input("Ingrese su antigua contraseña: ")
            encontrado = False
            for i in aprendices_info:
                if id_aprendiz == i[2]:
                    if id_contrasena_antigua == i[5]:
                        nueva_contrasena = input("Escriba su nueva contraseña: ")
                        i[5] = nueva_contrasena
                        print(f"Aprendiz: {i[0]} Su nueva contraseña es: {nueva_contrasena}")
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
                if id_aprendiz == i[2]:  
                    print(f"La contraseña para el documento {id_aprendiz} es: {i[5]}")
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
            if len(aprendices_info) <= 20:
                datos_aprendiz = []
                datos_aprendiz.append(input("Ingrese su primer nombre: "))
                datos_aprendiz.append(input("Ingrese su segundo nombre: "))
                datos_aprendiz.append(input("Ingrese su primer apellido: "))
                datos_aprendiz.append(input("Ingrese su número de documento: "))
                while True:
                        print("Seleccione el programa de formación del aprendiz: ")
                        print("1. ADSO")
                        print("2. Gestión Administrativa")
                        print("3. Cocina")
                        print("4. Animación 3D")
                        print("5. Multimedia")
                        print("6. Modistería")
                        print("7. Gestión Empresarial")
                        print("8. Ganadería")
                        try:
                            programa = int(input("Escriba el número de su programa para continuar: "))
                            if 1 <= programa <= 8:
                                datos_aprendiz.append(
                                    "ADSO" if programa == 1 else
                                    "Gestión Administrativa" if programa == 2 else
                                    "Cocina" if programa == 3 else
                                    "Animación 3D" if programa == 4 else
                                    "Multimedia" if programa == 5 else
                                    "Modistería" if programa == 6 else
                                    "Gestión Empresarial" if programa == 7 else
                                    "Ganadería"
                                )
                                break
                            else:
                                print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
                        except ValueError:
                            print("Debe ingresar un número entero.")
                while True:
                    correo = (input("Ingrese el correo electrónico del aprendíz: ")) 
                    if re.match(regex, correo):
                        datos_aprendiz.append(correo)
                        break
                    else:
                        print("**Correo Invalido, por favor intente nuevamente***")
                contrasena = ''.join(random.sample(caracteres, 8))  # Generación de la contraseña para el aprendiz registrado
                datos_aprendiz.append(contrasena)
                # Generador de usuario
                primera_letra_primer_nombre = datos_aprendiz[0][0].lower()
                primera_letra_segundo_nombre = datos_aprendiz[1][0].lower()
                apellido = datos_aprendiz[2].lower()
                usuario_formado = primera_letra_primer_nombre + primera_letra_segundo_nombre + "_" + apellido
                usuario = usuario_formado
                contador = 1
                usuarios_creados = [aprendiz[6] for aprendiz in aprendices_info]
                while usuario in usuarios_creados:
                    usuario = usuario_formado + str(contador)
                    contador += 1
                datos_aprendiz.append(usuario)
                # Determinar la semana de alimentación
                if datos_aprendiz[4].lower() in ("adso", "gestión administrativa"):
                    semana_alimentacion = 1
                elif datos_aprendiz[4].lower() in ("gestión empresarial", "animación 3d"):
                    semana_alimentacion = 2
                elif datos_aprendiz[4].lower() in ("multimedia", "modistería"):
                    semana_alimentacion = 3
                elif datos_aprendiz[4].lower() in ("cocina", "ganadería"):
                    semana_alimentacion = 4
                else:
                    semana_alimentacion = None
                datos_aprendiz.append(semana_alimentacion)
                aprendices_info.append(datos_aprendiz)
                print(f"\n¡{datos_aprendiz[0]} {datos_aprendiz[2]} ha sido registrado exitosamente!")
                print(f"Usuario: {datos_aprendiz[7]}")
                print(f"Contraseña: {datos_aprendiz[6]}")
            else:
                print("No hay cupo disponible para nuevos registros.")
            print("\n")
            input("Presione Enter para regresar al menú principal.")
            os.system('cls')      
        elif interaccion_aprendiz == "1":
            login_exitoso = False
            intentos_fallidos = 0
            for aprendiz_intento in range(3):
                os.system('cls')
                user = input("Ingrese su usuario de aprendíz: ")
                password = input("Ingrese su contraseña: ")
                
                for aprendiz_dato in aprendices_info:
                    if user == aprendiz_dato[6] and password == aprendiz_dato[5]:
                        os.system('cls')
                        print("Bienvenido Aprendíz.")
                        aprendiz_mood = True  # Se establece en true para saber que está entrando al modo aprendiz
                        login_exitoso = True
                        break  # Salir del bucle para el login del aprendiz
                if login_exitoso:
                    fecha_actual = datetime.now()
                    #ver la diferencia de los días
                    diferencia_dias = (fecha_actual - fecha_inicio).days
                    # Calcular el número de semana basado en la diferencia de días (7 días por semana)
                    semana_actual = (diferencia_dias // 7) + 1
                    semana_asignada = aprendiz_dato[7]
                    if semana_actual != semana_asignada:
                        print(f"Advertencia: No está en su semana asignada. Está en la semana {semana_asignada}, pero la semana actual es {semana_actual}.")
                        print("No puede reclamar el almuerzo en esta semana.")
                        break
                    # Mostrar información después del login exitoso
                    print(f"Señor(a) {aprendiz_dato[0]} {aprendiz_dato[1]}, su semana de alimentación es la semana no. {datos_aprendiz[7]} ")
                    print(f"El número de raciones que usted tiene disponibles es {raciones}")
                    print("\n")
                    print("Semana 1: alimentación para el programa de ADSO, GESTION ADMINISTRATIVA")
                    print("Semana 2: alimentación para el programa de GESTION EMPRESARIAL, ANIMACION 3D")
                    print("Semana 3: alimentación para el programa de MULTIMEDIA, MODISTERIA")
                    print("Semana 4: alimentación para el programa de COCINA, GANADERIA")
                    ver_menu = input("¿Desea ver el menú?: ")
                    if ver_menu.lower() == "no":
                        print("Continuando...")
                    elif ver_menu.lower() == "si":
                        print("\nMenú Semanal de Almuerzos")
                        print("=" * 40)
                        for i, plato in enumerate(menu_actual):
                            print(f"{dias_semana[i].capitalize()}: {plato}")
                        print("=" * 40)
                    # Gestión de raciones
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
                    break  # Salir del bucle principal si el login es exitoso
                else:
                    intentos_fallidos += 1
                    print("Usuario o contraseña incorrectos")
                    if aprendiz_intento < 2:
                        print("Intente nuevamente.")
                    else:
                        print("\nSus credenciales de acceso al sistema han sido bloqueadas")
                        aprendiz_bloqueado = user  # Utiliza el usuario ingresado
                        aprendices_bloqueados.append(aprendiz_bloqueado)
                        aprendiz_dato[5] = 0
                    input("Presione Enter para continuar")
                    os.system('cls')
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("Presione Enter para regresar al menú principal.")
            os.system('cls')
    elif interaccion == "3":
        os.system('cls')
        print("Semanas de Alimentación:")
        print("Semana 1: alimentación para el programa de ADSO, GESTION ADMINISTRATIVA")
        print("Semana 2: alimentación para el programa de GESTION EMPRESARIAL, ANIMACION 3D")
        print("Semana 3: alimentación para el programa de MULTIMEDIA, MODISTERIA")
        print("Semana 4: alimentación para el programa de COCINA, GANADERIA")
        print("\n")
        print("\nMenú Semanal de Almuerzos")
        print("=" * 40)
        for i, plato in enumerate(menu_actual):
            print(f"{dias_semana[i].capitalize()}: {plato}")
        print("=" * 40)
        input("\nPresione Enter para salir")