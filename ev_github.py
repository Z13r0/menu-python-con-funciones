# Este es un archivo python es un menú simple (Sencillo) para demostrar tu nivel en:
# Def, While, If and others....

def saludar():
    print("Hola! Bienvenido al Menú" \
    "\n Espermos que disfrutes tu instacia en este Menu")

def despedirse():
    print("Esperamos que te haya gustado al menu" \
    "\n Hasta Luego!!")


def mostrar_menu():
    print("\n -------- Menú principal --------" \
    "\n Escoge una de las siguientes opciones:" \
    "\n 1. Saludar" \
    "\n 2. Despedirse" \
    "\n 3. Salir" \
    "\n ----------------")

def main():
    while True:
        mostrar_menu()
        op = input("Ingrese una opción: ")
        if op == '1':
            saludar()
        elif op == '2':
            despedirse()
        elif op == '3':
            print("Estas saliendo del programa...." \
            "\n Adiosito ")
            break
        else:
            print("Opción invalida. Intenta Ingresar un Número entre el 1 y el 3.")

# Inicializamos el programa
main()
