'''usuarios= {
    "daniel" : {
        "sexo" : "M",
        "pass" : "123mnh"
    },
    "juan" : {
        "sexo" : "M",
        "pass" : "123213sadsad"
    }
}

usuarios2 = {
    "juan" : ["M","21313sadad"],
    "pedro" : ["M","213asdsad"],
    "maria" : ["F","dadsadasd"]
}'''

# -- funciones
def ingresar_usuario():
    while True:
        nombre = input("Ingrese nombre de usuario: ")

        if nombre in usuarios:
             print("El usuario ya existe, intente con otro nombre")
             
        else:
             break
        
    while True:
        sexo = input("Ingrese sexo (M,F): ").upper()

        if sexo == "M"  or sexo == "F":
             break
        else:
             print("Debe ingresar M o F al sexo, intente nuevamente!")

    while True:
            contraseña = input("Ingrese contraseña: ")
            if validar_contraseña(contraseña):
                 #print("Contraseña válida!")
                 break
            else:
                 print("Contraseña inválida,debe tener 8 caracteres (letras y numeros) intente nuevamente")

    usuarios[nombre] = {
         "sexo" : sexo,
         "contraseña" : contraseña
    }

    print("Datos ingresados correctamente!!")

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
     
    if " " in contraseña :
        return False

    num = False
    letra = False
    for caracter in contraseña:
        if caracter.isdigit():
            num = True 
        if caracter.isalpha():
             letra = True
        
    return num and letra
             
def buscar_usuario():
    nombre = input("Ingrese usuario para buscar: ")

    if nombre in usuarios:
        print(f"Sexo: {usuarios[nombre]["sexo"]}")
        print(f"Contraseña: {usuarios[nombre]["contraseña"]}")

    else:
         print("Usuario no encontrado!")

def eliminar_usuario():
            
    nombre = input("Ingrese usuario para buscar: ")

    if nombre in usuarios:
         del usuarios[nombre]
         print("Usuario eliminado")
    else:
         print("No existe usuario!")


#---- Menu ppal ----
usuarios = {}
while True:
    print("--- MENU PRINCIPAL ---")
    print("1. Ingresar Usuario")
    print("2. Buscar Usuario")
    print("3. Eliminar Usuario")
    print("4. Salir")

    while True:
        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
                print("Ingrese un valor válido, intente nuevamente")
    
    if op == 1:
        ingresar_usuario()

    elif op == 2 :
        buscar_usuario()
    elif op == 3:
         eliminar_usuario()

    elif op == 4:
         print("Saliendo...")
         break
    else:
         print("Opción no es válida, debe estar entre 1 y 4")


        


