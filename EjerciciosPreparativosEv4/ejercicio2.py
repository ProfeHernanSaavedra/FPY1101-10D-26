import funciones as fn
# codigo ppal
alumnos = {}

while True:
    print("---MENU---")
    print("1. Agregar Alumno")
    print("2. Mostrar Alumnos")
    print("3. Ver Promedios")
    print("4. Mejor Alumno")
    print("5. Cantidad de aprobados")
    print("6. Salir")
    while True:
        try:
            op = int(input("Seleccion opción: "))
            break
        except ValueError:
            print("Debe ingresar un valor entre 1 y 6, intentelo nuevamente!")

    if op == 1 :
        fn.agregar_alumno(alumnos)
    elif op == 2 :
        fn.mostrar_alumnos(alumnos)
    elif op == 3:
        fn.ver_promedios(alumnos)
    elif op == 4:
        fn.mejor_alumno(alumnos)
    elif op == 5:
        fn.cantidad_aprobados(alumnos)
    elif op == 6:
        print("Saliendo....")
        break
    else:
        print("Opción no válida")
        

