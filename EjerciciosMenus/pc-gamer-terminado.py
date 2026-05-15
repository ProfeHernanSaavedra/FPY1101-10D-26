presupuesto = 1200000
tiene_pc = False
rendimiento_base = 0

menu = True
while menu:
    print("---TIENDA DE PC GAMER---")
    print("1. Armar y comprar una PC")
    print("2. Test de rendimiento")
    print("3. Resetear / Vender")
    print("4. Salir")
    try:
        op_menu = int(input("--> "))
    except ValueError:
        print("Error: solo ingresar números")
        continue

    if op_menu == 1:
        if tiene_pc: 
            print("Ya tienes un PC.")
        else:
            print("\n~~~CONFIGURACIÓN~~~")
            try:
                op_cpu = int(input("""Elige CPU:
            1: Ryzen 3 3200G
            2: Ryzen 5 5600X
            3: Ryzen 7 5700G
            4: Ryzen 7 5800X3D
            5: Ryzen 9 7950X
            --> """))
                # Logica cpu
                if op_cpu == 1:
                    cost_cpu = 80000
                    pts_cpu = 20
                elif op_cpu == 2:
                    cost_cpu = 150000
                    pts_cpu = 45
                elif op_cpu == 3:
                    cost_cpu = 220000
                    pts_cpu = 65
                elif op_cpu == 4:
                    cost_cpu = 350000
                    pts_cpu = 90
                elif op_cpu == 5:
                    cost_cpu = 550000
                    pts_cpu = 130
                else:
                    print("Opcion invalida. Se asignara la opcion 1 por defecto.")
                    cost_cpu = 80000
                    pts_cpu = 20

                op_gpu = int(input("""Elige GPU:
            1: GTX 1650
            2: RTX 3060
            3: RTX 3070
            4: RTX 4070
            5: RTX 4090
            --> """))

                # Logica gpu
                if op_gpu == 1:
                    cost_gpu = 150000
                    pts_gpu = 30
                elif op_gpu == 2:
                    cost_gpu = 280000
                    pts_gpu = 70
                elif op_gpu == 3:
                    cost_gpu = 400000
                    pts_gpu = 100
                elif op_gpu == 4:
                    cost_gpu = 600000
                    pts_gpu = 130
                elif op_gpu == 5:
                    cost_gpu = 950000
                    pts_gpu = 200
                else:
                    print("Opcion invalida. Se asignara la opcion 1 por defecto.")
                    cost_gpu = 150000
                    pts_gpu = 30

                op_ram = int(input("""Elige RAM:
            1: 8GB
            2: 16GB
            3: 32GB
            --> """))

                # Logica ram
                if op_ram == 1:
                    cost_ram = 35000
                    mult_ram = 0.7
                elif op_ram == 2:
                    cost_ram = 65000
                    mult_ram = 1.0
                elif op_ram == 3:
                    cost_ram = 110000
                    mult_ram = 1.3
                else:
                    print("Opcion invalida. Se asignara la opcion 1 por defecto.")
                    cost_ram = 35000
                    mult_ram = 0.7

                op_psu = int(input("""Elige Fuente de Poder:
            1: 500W Generica
            2: 650W Certificación Bronce
            3: 850W Certificación Gold
            --> """))

                # Logica fuente de poder
                if op_psu == 1:
                    cost_psu = 30000
                elif op_psu == 2:
                    cost_psu = 65000
                elif op_psu == 3:
                    cost_psu = 120000
                else:
                    print("Opcion invalida. Se asignara la opcion 1 por defecto.")
                    cost_psu = 30000
            
                #calculo de costos
                cost_total = cost_cpu + cost_gpu + cost_ram + cost_psu
                presupuesto_valido = cost_total <= presupuesto

                #logica de explosion
                pc_seguro = True
                if (op_gpu == 3 or op_gpu == 4 or op_gpu == 5) and op_psu == 1:
                    pc_seguro = False 
                elif op_gpu == 5 and op_psu == 2:
                    pc_seguro = False 

                if not presupuesto_valido:
                    print(f"\nError: te pasaste del presupuesto. costo total: ${cost_total}")
                elif not pc_seguro:
                    print("\nError: tu PC exploto. Pusiste una tarjeta grafica muy potente con una fuente de poder muy debil")
                else:
                    print(f"\n¡Compra exitosa! Tu vuelto es ${presupuesto - cost_total}")
                    rendimiento_base = (pts_cpu + pts_gpu) * mult_ram
                    tiene_pc = True
            except ValueError:
                print("Error: opción no valida durante el armado")
    elif op_menu == 2:
        if not tiene_pc:
            print("No se puede testear")
        else:
            print("~~~TEST~~~")
            try:
                print()
                op_juego = int(input("""Elige el juego:
1: League of Legends
2: Left 4 Dead 2
3: Minecraft
4: Valorant
5: The Forest
6: Sekiro: Shadows Die Twice
7: Resident Evil 4 Remake
8: Cyberpunk 2077
9: ClairObscure: Expedition 33
--> """))
                if op_juego == 1:
                    fps = rendimiento_base * 2.8
                    juego = "League of Legends"
                elif op_juego == 2:
                    fps = rendimiento_base * 2.5
                    juego = "Left 4 Dead 2"
                elif op_juego == 3:
                    fps = rendimiento_base * 2.0
                    juego = "Minecraft"
                elif op_juego == 4:
                    fps = rendimiento_base * 1.8
                    juego = "Valorant"
                elif op_juego == 5:
                    fps = rendimiento_base * 1.4
                    juego = "The Forest"
                elif op_juego == 6:
                    fps = rendimiento_base * 1.0
                    juego = "Sekiro: Shadows Die Twice"
                elif op_juego == 7:
                    fps = rendimiento_base * 0.8
                    juego = "Resident Evil 4 Remake"
                elif op_juego == 8:
                    fps = rendimiento_base * 0.6
                    juego = "Cyberpunk 2077"
                elif op_juego == 9:
                    fps = rendimiento_base * 0.3
                    juego = "ClairObscure: Expedition 33"
                else:
                    print("Opcion ingresada invalida. Calculando para el League of Legends")
                    fps = rendimiento_base * 2.8
                    juego = "League of Legends"
                    
                print(f"Tu PC correra {juego} a {int(fps)} FPS estimados.")
            except ValueError:
                print("Debe ser un número")
    elif op_menu == 3:
        if tiene_pc:
            tiene_pc = False
            presupuesto = 1200000
            rendimiento_base = 0
            print("reset exitoso")
        else:
            print("No tiene ningun pc")

    elif op_menu == 4:
        print("Saliendo...")
        menu = False
    else:
        print("Opcion invalida")