from math import pi

def sumarFijo():
    num1 = 2
    num2 = 3
    sumar = num1 + num2 
    print(sumar)

def sumar(num1,num2)-> int:
    '''Esta funcion sirve para sumar dos números enteros cualquiera'''
    sumar = num1 + num2 
    print(sumar)

def restar(num1,num2):
    restar = num1 - num2
    return restar

def AreaCirculo(radio):
    '''Esta función calcula el radio de un circulo'''
    
    areaCirculo = pi * (radio**2)
    return areaCirculo
    
def perimetroCirculo(radio):
    per = 2*pi*radio
    return per