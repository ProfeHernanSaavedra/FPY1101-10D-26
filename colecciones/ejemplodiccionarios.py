datos = {
    "rut" : "123-4",
    "nombre" : "Alejandro",
    "telefono" : [123456,5647,125],
    "direccion" : "Viña"
}

print(f"El nombre es: {datos["nombre"]}")
print("El segundo telefono es: ",datos["telefono"][1])

print(datos)

# insertar datos o claves
datos["email"] = "ale@gmail.com"
print(datos["email"])
datos["telefono"].append(22222)
print(datos["telefono"])

#actualizar
datos["telefono"][0] = 666
print(datos["telefono"])
datos["direccion"] = "Valpo"
print(datos)

#borrar
del datos["direccion"]
print(datos)
print(datos["telefono"])
datos["telefono"].pop(2)
print(datos["telefono"])

#LISTAS - POP y REMOVE
lista = [1,2,"Juan",3,"Juan"]
lista.pop(1)
print(lista)
lista.remove(3)
print(lista)
lista.insert(3,"Maria")
lista.remove("Juan")
print(lista)



