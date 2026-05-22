import funciones as fn
#from funciones import sumar


# llamando a funciones
fn.sumarFijo()
fn.sumarFijo()
fn.sumar(3,4)
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
fn.sumar(n1,n2)
resta = fn.restar(n1,n2)
print(resta)

radio = float(input("Ingrese radio circulo: "))
areaCirculo = fn.AreaCirculo(radio)
print("El area es: " , areaCirculo)
perimetro = fn.perimetroCirculo(radio)
print("El perimetro es: " , perimetro)
