import os

ARCHIVO = "Usuarios_Registrados.txt"

if not os.path.exists(ARCHIVO):
    #si el archivo 'Usuarios_Registrados' no existe creamos un usuario admin para que el archivo exista.
    with open(ARCHIVO, "w") as usuarios_inicial: #se crea y se escribe con 'w'
        usuarios_inicial.write("admin,1234,0\n")
with open(ARCHIVO,"r") as archivo_usuarios:
    total_usuarios = {}
    for linea in archivo_usuarios:
        usuario = linea.strip().split(",")
        #El valor 0 referencia al usuario, el 1 a la contraseña y el 2 al saldo.
        total_usuarios[usuario[0]] = [usuario[1], usuario[2]] 

def bienvenida():
    print("\n   ¡Bienvenido! \n1. Iniciar sesión \n2. Crear cuenta nueva \n3. Salir\n")
    opcion_menu = input("Seleccione una opción para comenzar: ")
    while opcion_menu not in ["1", "2", "3"]:
        print("\nOpción inválida. Elija 1, 2 o 3 para salir\n")
        opcion_menu = input("Seleccione una opción para comenzar: ")
    return opcion_menu

def guardar(total_usuarios):
    with open(ARCHIVO, "w") as archivo:
        for usuario in total_usuarios.keys():
            archivo.write(f"{usuario},{total_usuarios[usuario][0]},{total_usuarios[usuario][1]}\n")
            
def registrar_usuario(total_usuarios):
    #Crea un usuario nuevo y lo guarda en el archivo de texto "usuarios".
    print("\n REGISTRO DE NUEVO USUARIO \n")
    usuario = input("Ingrese nuevo nombre de usuario: ")
    if not usuario in total_usuarios.keys():
        contraseña = input("Ingrese una contraseña de 4 dígitos: ")
        saldo = 2000000
        while len(contraseña) != 4 or not contraseña.isdigit():
            print("\nError la contraseña debe tener 4 dígitos númericos: ")
            contraseña = input("\nIngrese contraseña válida: ")
        total_usuarios[usuario] = [contraseña, saldo]
        print("\n¡Usuario registrado!")
        guardar(total_usuarios)
    else:
        print("\nEl usuario ya existe")
    return(total_usuarios)

def login(total_usuarios):
    #Valida el acceso leyendo desde el Usuarios_Registrados.txt.
    print("\n INICIO DE SESIÓN \n")
    intentos = 0  # contador para intentos

    while intentos < 3:
        inicio_usuario = input("Ingrese su usuario: ")
        inicio_contraseña = input("Ingrese su contraseña: ")
        try:
            if inicio_contraseña == total_usuarios[inicio_usuario][0]:
                print("\n   ¡Bienvenido!")
                return inicio_usuario
        except KeyError:
            intentos += 1
            print(f"\nUsuario o contraseña incorrectos. Te quedan {3 - intentos} intentos.")
    print("\nTarjeta bloqueada por motivos de seguridad.")
    return False

    
 def deposito_cajero(total_usuarios,usuario):
    saldo = int(total_usuarios[usuario][1])
    deposito_exitoso = False
    while not deposito_exitoso:
        try:
            deposito = int(input(f"\nIngrese el monto que desea depositar: $"))
            if deposito <= 0:
                print("\nError. El monto debe ser positivo")
            else:
                total_usuarios[usuario][1] = str(saldo + deposito)
                print("\nDepósito realizado con éxito.")
                deposito_exitoso = True
        except ValueError:
            print("\nError. Ingrese un valor numérico válido.")
    guardar(total_usuarios)
    return total_usuarios
