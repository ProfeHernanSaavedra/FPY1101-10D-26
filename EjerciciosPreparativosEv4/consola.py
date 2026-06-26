# ============================================================
#  Sistema de Gestión de Consolas de Videojuegos
#  FPY1101 - Fundamentos de Programación
# ============================================================

# ── Estructuras de datos ─────────────────────────────────────
# consolas = { sigla: [nombre, fabricante, anio_lanzamiento] }
# ventas   = { sigla: [precio, stock] }


# ════════════════════════════════════════════════════════════
#  FUNCIONES DE VALIDACIÓN  (responsabilidad única: True/False)
# ════════════════════════════════════════════════════════════

def validar_sigla_formato(sigla):
    """Sigla: 2-5 caracteres, solo letras mayúsculas."""
    return sigla.isupper() and sigla.isalpha() and 2 <= len(sigla) <= 5


def validar_sigla_no_existe(sigla, consolas):
    """Retorna True si la sigla NO existe aún en el diccionario."""
    return sigla not in consolas


def validar_nombre(nombre):
    """Nombre: entre 3 y 40 caracteres, no vacío."""
    return 3 <= len(nombre.strip()) <= 40


def validar_fabricante(fabricante):
    """Fabricante: entre 2 y 30 caracteres, no vacío."""
    return 2 <= len(fabricante.strip()) <= 30


def validar_anio(anio_str):
    """Año: entero entre 1972 y 2025."""
    if not anio_str.isdigit():
        return False
    return 1972 <= int(anio_str) <= 2025


def validar_precio(precio_str):
    """Precio: número decimal mayor a 0."""
    try:
        return float(precio_str) > 0
    except ValueError:
        return False


def validar_stock(stock_str):
    """Stock: entero mayor o igual a 0."""
    if not stock_str.isdigit():
        return False
    return int(stock_str) >= 0


# ════════════════════════════════════════════════════════════
#  FUNCIÓN MENÚ
# ════════════════════════════════════════════════════════════

def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print("\n" + "=" * 40)
    print("   SISTEMA DE CONSOLAS DE VIDEOJUEGOS")
    print("=" * 40)
    print("  1. Agregar consola")
    print("  2. Buscar consola por sigla")
    print("  3. Eliminar consola")
    print("  4. Mostrar todas las consolas")
    print("  5. Salir")
    print("=" * 40)


def leer_opcion():
    """Lee y valida la opción del menú (1-5)."""
    opcion = input("Seleccione una opción: ").strip()
    while not opcion.isdigit() or int(opcion) not in range(1, 6):
        print("  ✗ Opción inválida. Ingrese un número entre 1 y 5.")
        opcion = input("Seleccione una opción: ").strip()
    return int(opcion)


# ════════════════════════════════════════════════════════════
#  FUNCIÓN AGREGAR
# ════════════════════════════════════════════════════════════

def agregar_consola(consolas, ventas):
    """Solicita datos, valida y agrega la consola en ambos diccionarios."""
    print("\n── AGREGAR CONSOLA ──")

    # Sigla
    sigla = input("Sigla (2-5 letras mayúsculas): ").strip()
    while not validar_sigla_formato(sigla):
        print("  ✗ Sigla inválida. Debe tener entre 2 y 5 letras mayúsculas.")
        sigla = input("Sigla: ").strip()
    if not validar_sigla_no_existe(sigla, consolas):
        print(f"  ✗ La sigla '{sigla}' ya existe. No se puede agregar.")
        return

    # Nombre
    nombre = input("Nombre de la consola (3-40 caracteres): ").strip()
    while not validar_nombre(nombre):
        print("  ✗ Nombre inválido. Debe tener entre 3 y 40 caracteres.")
        nombre = input("Nombre: ").strip()

    # Fabricante
    fabricante = input("Fabricante (2-30 caracteres): ").strip()
    while not validar_fabricante(fabricante):
        print("  ✗ Fabricante inválido. Debe tener entre 2 y 30 caracteres.")
        fabricante = input("Fabricante: ").strip()

    # Año
    anio_str = input("Año de lanzamiento (1972-2025): ").strip()
    while not validar_anio(anio_str):
        print("  ✗ Año inválido. Debe ser un entero entre 1972 y 2025.")
        anio_str = input("Año: ").strip()

    # Precio
    precio_str = input("Precio (mayor a 0): ").strip()
    while not validar_precio(precio_str):
        print("  ✗ Precio inválido. Debe ser un número mayor a 0.")
        precio_str = input("Precio: ").strip()

    # Stock
    stock_str = input("Stock disponible (0 o más): ").strip()
    while not validar_stock(stock_str):
        print("  ✗ Stock inválido. Debe ser un número entero mayor o igual a 0.")
        stock_str = input("Stock: ").strip()

    # Agregar en ambos diccionarios bajo la misma clave
    consolas[sigla] = [nombre.strip(), fabricante.strip(), int(anio_str)]
    ventas[sigla]   = [float(precio_str), int(stock_str)]

    print(f"\n  ✓ Consola '{sigla}' agregada exitosamente.")


# ════════════════════════════════════════════════════════════
#  FUNCIÓN BUSCAR
# ════════════════════════════════════════════════════════════

def buscar_consola(consolas, sigla):
    """
    Busca la sigla en el diccionario consolas.
    Retorna True si existe, False si no.
    """
    return sigla in consolas


# ════════════════════════════════════════════════════════════
#  FUNCIÓN MOSTRAR UNA CONSOLA
# ════════════════════════════════════════════════════════════

def mostrar_detalle(sigla, consolas, ventas):
    """Imprime los datos completos de una consola cruzando ambos diccionarios."""
    nombre, fabricante, anio = consolas[sigla]
    precio, stock            = ventas[sigla]
    print("\n  === Consola Encontrada ===")
    print(f"  Sigla       : {sigla}")
    print(f"  Nombre      : {nombre}")
    print(f"  Fabricante  : {fabricante}")
    print(f"  Año lanz.   : {anio}")
    print(f"  Precio      : ${precio:,.2f}")
    print(f"  Stock       : {stock} unidades")


def opcion_buscar(consolas, ventas):
    """Gestiona la búsqueda interactiva desde el menú."""
    print("\n── BUSCAR CONSOLA ──")
    sigla = input("Ingrese la sigla a buscar: ").strip().upper()
    if buscar_consola(consolas, sigla):
        mostrar_detalle(sigla, consolas, ventas)
    else:
        print(f"  ✗ No se encontró ninguna consola con la sigla '{sigla}'.")


# ════════════════════════════════════════════════════════════
#  FUNCIÓN ELIMINAR
# ════════════════════════════════════════════════════════════

def eliminar_consola(consolas, ventas):
    """Elimina una consola de ambos diccionarios usando la función de búsqueda."""
    print("\n── ELIMINAR CONSOLA ──")
    sigla = input("Ingrese la sigla a eliminar: ").strip().upper()

    if not buscar_consola(consolas, sigla):          # reutiliza buscar, sin duplicar lógica
        print(f"  ✗ No se encontró la sigla '{sigla}'.")
        return

    mostrar_detalle(sigla, consolas, ventas)
    confirmar = input("\n  ¿Confirma la eliminación? (s/n): ").strip().lower()
    if confirmar == "s":
        del consolas[sigla]
        del ventas[sigla]
        print(f"  ✓ Consola '{sigla}' eliminada exitosamente.")
    else:
        print("  Eliminación cancelada.")


# ════════════════════════════════════════════════════════════
#  FUNCIÓN MOSTRAR TODAS
# ════════════════════════════════════════════════════════════

def mostrar_todas(consolas, ventas):
    """Recorre ambos diccionarios de forma cruzada por clave e imprime cada consola."""
    print("\n" + "=" * 62)
    print("              LISTADO COMPLETO DE CONSOLAS")
    print("=" * 62)

    if len(consolas) == 0:
        print("  No hay consolas registradas en el sistema.")
    else:
        for sigla, datos in consolas.items():          # técnica correcta: .items()
            nombre, fabricante, anio = datos
            precio, stock            = ventas[sigla]   # cruce por clave compartida
            print(f"  {sigla:<6} | {nombre:<22} | {fabricante:<12} | "
                  f"{anio} | ${precio:>10,.2f} | Stock: {stock}")

    print("=" * 62)
    print(f"  Total de consolas: {len(consolas)}")


# ════════════════════════════════════════════════════════════
#  PROGRAMA PRINCIPAL
# ════════════════════════════════════════════════════════════

def main():
    consolas = {}   # { sigla: [nombre, fabricante, anio_lanzamiento] }
    ventas   = {}   # { sigla: [precio, stock] }

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_consola(consolas, ventas)
        elif opcion == 2:
            opcion_buscar(consolas, ventas)
        elif opcion == 3:
            eliminar_consola(consolas, ventas)
        elif opcion == 4:
            mostrar_todas(consolas, ventas)
        elif opcion == 5:
            print("\n  Hasta pronto. Cerrando el sistema...\n")
            continuar = False


main()