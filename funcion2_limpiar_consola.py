import os

def limpiar_consola():
    # Limpia la consola en Windows
    if os.name == 'nt':
        os.system('cls')
    """ # Limpia la consola en macOS y Linux
    else:
        os.system('clear')
 """
# Ejemplo de uso:
print("Este es un mensaje en la consola.")
input("Presiona Enter para limpiar la consola...")
limpiar_consola()
print("La consola está limpia.")



