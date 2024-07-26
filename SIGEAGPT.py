admin = "Admin"
admin_password = "1234"  # Creación de las credenciales de acceso del Admin

admin_mood = False
register_mood = False
aprendiz_mood = False
raciones = 5
salir_registro = False
no_registrar = False
intentos_login = 3  # Inicialización de variables que se irán utilizando en el programa

usernames = []
lastnames = []
nids = []
programs = []  # Simplificación (Se han creado 4 listas vacías que luego se utilizarán para guardar la información)

print(".:Bienvenido al Sistema de Gestión de Entrega de Almuerzo SIGEA:.")
print("1. Administrador.")
print("2. Aprendiz.")
print("3. Invitado.")
print("4. Salir.")
interaccion = input("Digite su tipo de usuario para continuar:")

while interaccion != "4":
    if interaccion == "1":  # Ingreso del Admin
        for admin_intento in range(3):
            print("\n" * 30)
            user = input("Ingrese su usuario de administrador:")
            password = input("Ingrese su contraseña:")
            print("\n" * 5)
            if user == admin and password == admin_password:
                print("\n" * 20)
                print("Bienvenido Admin.")
                print("\n" * 1)
                admin_mood = True  # Establecer admin_mood en True después de un inicio de sesión exitoso
                break  # Salir del bucle de inicio de sesión del administrador
            elif (user != admin or password != admin_password):  # Si la contraseña o el usuario son iconrrectos se mostrará el mensaje de error
                print("\n" * 1)
                print("Su usuario o contraseña son inválidos")
                if admin_intento < 2:
                    print("Intente nuevamente")
                else:
                    print("Número de intentos limitados.")
            elif (user == "" and password == ""):
                print("No ha ingresado ningún valor")
            else:
                print("Error: Vuelva a intentarlo.")

        if admin_mood: # Se comenzará a ejecutar la opciones del admin cuando las credenciales sean verdaderas para admin
            while True: # pero se mostraran las opciones utilizando un while true, o sea mientras sean verdad las credenciales
                print("Opciones del Administrador:")
                print("1. Registrar Usuarios")
                print("2. Consultar Usuarios")
                print("3. Modificar Usuarios")
                print("4. Desbloquear usuario por ingreso erróneo")
                print("5. Actualización de Menú")
                print("6. Reasignación de Semanas")
                print("7. Salir")
                opcion_admin = input("Seleccione una opción:")
                if opcion_admin == "7":
                    admin_mood = False
                    break  # Salir del modo administrador
                elif opcion_admin == "6":
                    print("Reasignación de Semanas")
                elif opcion_admin == "5":
                    print("Actualización de Menú")
                elif opcion_admin == "4":
                    print("Desbloquear usuario por ingreso erróneo")
                elif opcion_admin == "3":
                    print("Modificar Usuarios")
                elif opcion_admin == "2":
                    print("Consultar Usuarios")
                elif opcion_admin == "1":
                    print("Registrar Usuarios")
                    print("\n")
                elif opcion_admin != ("1","2","3","4","5","6","7"):
                    print("Opción invalida")
                    print("Digite una opción valida entre los números 1 y 7")
                else:
                    print("Digite por favor una opción")
                        
print("Gracias por usar el Sistema de Gestión de Entrega de Almuerzo SIGEA.")
