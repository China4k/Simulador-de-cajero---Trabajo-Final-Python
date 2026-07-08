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
        if inicio_usuario in total_usuarios and inicio_contraseña == total_usuarios[inicio_usuario][0]:
            print("\n   ¡Bienvenido!")
            return inicio_usuario
        else:
            intentos += 1
            print(f"\nUsuario o contraseña incorrectos. Te quedan {3 - intentos} intentos.")
    print("\nTarjeta bloqueada por motivos de seguridad.")
    return False

def extraccion_cajero(total_usuarios,usuario,limite_diario):
    saldo = int(total_usuarios[usuario][1])
    extraccion_exitosa = False
    while not extraccion_exitosa:
        try:
            extraccion = int(input(f"\nIngrese el monto que desea extraer (múltiplos de $1000): $"))
            if extraccion % 1000 != 0:
                print("\nError. Ingrese un monto múltiplo de $1000")
            elif extraccion <= 0:
                print("\nError. El monto debe ser positivo")
            elif extraccion > limite_diario:
                print(f"\nEl monto ingresado supera el límite de extracción diaria ${limite_diario}")
                extraccion_exitosa = True
            elif extraccion > saldo:
                print(f"\nSaldo insuficiente \nSu saldo es de ${saldo}")
                return total_usuarios, limite_diario
            else:
                total_usuarios[usuario][1] = str(saldo - extraccion) 
                limite_diario = limite_diario - extraccion
                print("\nExtracción realizada con éxito. Retire su dinero.")
                extraccion_exitosa = True
        except ValueError:
            print("\nError. Ingrese un valor numérico válido.")
    guardar(total_usuarios)
    return total_usuarios, limite_diario
    
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

def transferencia_cajero(total_usuarios, usuario):
    saldo = int(total_usuarios[usuario][1])
    cuenta_destino = input(f"\nIngrese el usuario de la cuenta destino: ")
    if cuenta_destino in total_usuarios.keys():
        # Si existe, recién ahí pide la plata
        try:
            monto_transferir = int(input(f"Ingrese el monto a transferir a {cuenta_destino}: $"))
            if total_usuarios[cuenta_destino] == total_usuarios[usuario] :
                print("\nError. No puede transferirse a si mismo")
            elif monto_transferir <= 0:
                print("\nError. El monto debe ser positivo")
            elif monto_transferir > saldo:
                print(f"\nSaldo insuficiente \nSu saldo es de ${saldo}")
            else:
                total_usuarios[cuenta_destino][1] = str(saldo + monto_transferir)
                total_usuarios[usuario][1] = str(saldo - monto_transferir)
                guardar(total_usuarios)
                print(f"\n¡Transferencia realizada con éxito a {cuenta_destino}!")
        except ValueError:
            print("\nError. Ingrese un valor numérico válido.")
    else:
        print("\nEl usuario de destino no existe.")
    return total_usuarios
    
def cajero(total_usuarios, usuario):
    limite_diario = 200000
    while True:
        print("\n1. Consultar saldo\n2. Extraer dinero\n3. Realizar un depósito\n4. Realizar transferencia\n5. Salir\n")
        opcion_cajero = input("Seleccione una opción: ")
        if opcion_cajero == "1":
            print(f"\nSu saldo disponible es de: ${str(total_usuarios[usuario][1])}")
        elif opcion_cajero == "2":
            total_usuarios, limite_diario = extraccion_cajero(total_usuarios, usuario, limite_diario)
        elif opcion_cajero == "3":
            total_usuarios = deposito_cajero(total_usuarios, usuario)
        elif opcion_cajero == "4":
            total_usuarios = transferencia_cajero(total_usuarios, usuario)
        elif opcion_cajero == "5":
            print("\nCerrando sesión...")
            break
        else:
            print("\nOpción inválida. Elija 1, 2, 3, 4 o 5 para salir.")
    return total_usuarios

while True:
    seleccion_menu = bienvenida() #muestra el menú y guarda la opción elegida
    if seleccion_menu == "1":
        usuario = login(total_usuarios) #para iniciar sesión
        if usuario != False:
            total_usuarios = cajero(total_usuarios, usuario)
            print("\n   Sesión Finalizada")
    elif seleccion_menu == "2":
        total_usuarios = registrar_usuario(total_usuarios)
    else:
        print("\n¡Hasta luego!") #3 es la opción para salir
        break
