menu = True
while menu:
    print("--MENU--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")

    op = int(input("Ingrese su opción: "))

    if op == 1 :
        print("Pago Tarjeta de Crédito")
    elif op == 2 :
        print("Comprando...")
    elif op == 3: 
        print("Saliendo...")
        menu = False
    else:
        print("Opción no válida!")


