# ppal
consolas = {} # {sigla:[nombre,fabricante,añoLanzamiento]}
ventas = {} # {sigla: [precio,stock]}

def menu():
    print("="*40)
    print("SISTEMA DE CONSOLAS DE VIDEOJUEGOS")
    print("1. Agregar Consola")
    print("2. Buscar Consola por sigla")
    print("3. Eliminar Consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("="*40)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            return opcion
        except ValueError:
            print("Debe ingresar un número!! ")

while True:
    menu()
    op = leer_opcion()
    if op == 1 :
        agregar_consola(consolas,ventas)
    elif op == 2:
        opcion_buscar(consolas,ventas)
    elif op == 3:
        eliminar_consola(consolas,ventas)
    elif op == 4:
        mostrar_todas(consolas,ventas)
    elif op == 5:
        print("Saliendo..")
        break
    else:
        print("las opciones son del 1 al 5, vuelva a ingresar")
    
    
