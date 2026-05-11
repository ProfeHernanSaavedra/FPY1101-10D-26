menu = True
deuda = 100000

while menu:
    print("--MENU--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")

    op = int(input("Ingrese su opción: "))

    if op == 1 :
        print("Pago Tarjeta de Crédito")
        while True:
            try:
                pago = int(input("Ingrese monto de pago: "))
                break
            except:
                print("El valor debe ser numerico!")
        if pago >= 0 :
            if pago <= deuda:
                deuda = deuda - pago
                print("Pago exitoso! su nuevo deuda es: $",deuda)
            else:
                print("El pago excede la deuda")

    elif op == 2 :
        print("Comprando...")
    elif op == 3: 
        print("Saliendo...")
        menu = False
    else:
        print("Opción no válida!")


