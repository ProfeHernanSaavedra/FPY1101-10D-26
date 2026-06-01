'''productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}'''
#definicion de funciones
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre.isdigit() :
        print("Debe ingresar letras!!")
        return

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    if nombre in productos:
        print("El producto ya existe!")
        return
    
   
    while True:
        try:
            stock = int(input("Ingrese stock: "))
            if stock > 0:
                break
            else:
                print("El stock debe ser mayor a cero")
        except ValueError:
            print("Debe ingresar un número para stock!! , vuelva a intentar")

    while True:
        try:
            precio = int(input("Ingrese precio $:"))
            if precio > 0 :
                break
            else:
                print("El precio debe ser mayor a cero!")
        except ValueError:
            print("Debe ingresar un número para el precio!! , vuelva a intentar")      
   
        
    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente!")

def validarNumero(num):
     while True:
        try:
            
            if num > 0 :
                break
            else:
                print(f"El {num} debe ser mayor a cero!")
        except ValueError:
            print(f"Debe ingresar un número para el {num}!! , vuelva a intentar")

        return True


def mostrar_productos(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    
    for nombre in productos:
        print(nombre,"--Stock:",productos[nombre][0],"--Precio:$",productos[nombre][1])


def buscar_producto(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return

    nombre = input("Nombre producto a buscar: ").strip()

    if nombre in productos:
        print("Producto encontrado!!")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio : ${productos[nombre][1]}")
    else:
        print("Producto no existe o agotado!")

def producto_mas_caro(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    mayor = 0
    mayorNombre = ""
    for nombre in productos :
        precio = productos[nombre][1]

        if precio > mayor :
            mayor = precio
            mayorNombre = nombre

    
    print(f"Producto más caro es {mayorNombre}")
    print(f"Su precio es: ${mayor}")

