import os

def limpiar_consola():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')

# Tu código aquí...
nombre = input("Nombre: \n")
edad = input("Dime edad: \n")

# Llama a la función para limpiar la consola
limpiar_consola()
