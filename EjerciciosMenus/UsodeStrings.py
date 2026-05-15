palabra = "CRISTINA"

#[C R I S T I N A]
# 0 1 2 3 4 5 6 7

#hay funciones que trabajan con String

if palabra.startswith("C"):
    print("Bien! ")

if palabra.endswith("A"):
    print("Valida")

#substring
print(palabra[0:4])
print(palabra[7:8])

#"@"
correo = "hola@gmail.com"
if "@" in correo:
    print("Correo válido")

for caracter in correo:
    if caracter == "@" :
        print("Correo ultra valido con for") 

# tamaño -> len
print(len(palabra))



