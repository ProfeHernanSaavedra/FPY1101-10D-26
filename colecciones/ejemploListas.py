nombres = ["juan","Pedro","maria",4]
#            0      1        2

print(nombres)

# J U A N
# 0 1 2 3

print("0: ",nombres[0])

for i in range(3):
    print(nombres[i])

for i in nombres:
    print(i)

nombres.append("Francisca") # agregar elemento al final

print(nombres)

nombres.append(2356) # agregar elemento al final
print(nombres)

nombres.insert(1,1234)
print(nombres)

nombres.remove("Francisca")
print(nombres)

nombres.reverse()
print(nombres)

#nombres.sort()
#print(nombres)

datos = [3,1,2]
datos.sort()
print(datos)