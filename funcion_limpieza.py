import os
#cdigo para ejecutar en forma limpia la salida del codigo en consola

def limpiar_consola():
    if os.name == 'nt':  # Windows NT
        os.system('cls')
    # else:  # Unix/Linux
    #     os.system('clear')

# Tu código aquí...
nombre = input("Nombre: \n")
edad = input("Dime edad: \n")

# Llama a la función para limpiar la consola
limpiar_consola()
print(f"tu nombre es {nombre} y tu edad son {edad} años")
