import funciones as fn
#from funciones import agregar_producto

productos={}
#menu ppal
while True:
    print("---MENU---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            op = int(input("Selecccione opción: "))
            break
        except ValueError:
            print("Error, debe ingresar un número entre 1 y 5, Intente Nuevamente")

    if op == 1 :
        fn.agregar_producto(productos)
        # con from se usa , si fn
        #agregar_producto(productos)

        
    elif op == 2:
        fn.mostrar_productos(productos)
        #print(productos)
        
    elif op == 3:
        fn.buscar_producto(productos)
        #print("3")
        
    elif op == 4:
        fn.producto_mas_caro(productos)
        #print("4")
    elif op == 5:
        print("Fin del programa...")
        break
    else:
        print("Opción inválida!")
    

