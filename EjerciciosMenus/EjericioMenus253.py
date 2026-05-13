menu = True
deuda = 100000
saldo = 400000

while menu:
    
    print("--MENU--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de Compras")
    print("3. Salir")
    while True:
        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Error, el valor debe ser numérico entre 1 y 3, intente nuevamente")

    if op == 1 :
        print("Pago Tarjeta de Crédito")
        print("Deuda : $",deuda)
        var = True
        while var:
            try:
                pago = int(input("Ingrese monto de pago: "))
                var = False
            except ValueError:
                print("Error, El valor debe ser numerico!, por favor intente nuevamente")
        if pago >= 0 :
            if pago <= deuda:
                deuda = deuda - pago
                saldo = saldo + pago
                print("Pago exitoso! su nuevo deuda es: $",deuda)
            else:
                print("El pago excede la deuda")

    elif op == 2 :
        print("Comprando...")
        print("Su saldo para comprar es: $",saldo)
        cont = 0
        for i in range(saldo):
            cont = cont + 1
            print("Compra: ",cont )
            montoCompra = int(input("Ingrese monto de compra: $ " ))

            if montoCompra >=0 :
                    if saldo >= montoCompra :
                        saldo = saldo - montoCompra
                        deuda = deuda + montoCompra
                        print("Su saldo es: $",saldo)
                        if montoCompra == 0 or saldo <= 0:
                            break
                    else:
                        print("Saldo insuficiente")
                        break
            else:
                print("Por favor ingrese valor mayor que cero")
                cont = cont - 1

    elif op == 3: 
        print("Saliendo...")
        menu = False
    else:
        print("Opción no válida!")


