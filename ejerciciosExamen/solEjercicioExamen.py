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

#  funciones de validaciones que retornan True o False

def validar_sigla_formato(sigla):
    return sigla.upper() and sigla.isalpha() and len(sigla) >= 2 and len(sigla) <= 5
    # return True

def validar_sigla_no_existe(sigla,consolas):
    if sigla not in consolas:
        return True
    else:
        return False

def validar_nombre(nombre):

    return 3 <= len(nombre.strip()) <= 40

def validar_año(añoStr):
    if not añoStr.isdigit():
        return False
    
    return 1972 <= int(añoStr) <= 2025

def validar_precio(precioStr):
    try:
        return float(precioStr) > 0
    except ValueError:
        return False

def validar_stock(stockStr):
    if not stockStr.isdigit():
        return False
    
    return int(stockStr) >= 0



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
    
    
