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