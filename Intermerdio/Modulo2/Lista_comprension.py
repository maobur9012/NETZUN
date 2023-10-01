numeros = [1, 2, 3, 4, 5, 6, 7, 8]
r1 = []

for item in numeros:
    valor = item*2
    r1.append(valor)

print("Listas utilizando for normal")
print(r1)

#Comprension de lista
print("Lista por comprension")
r2 = [e*2 for e in numeros if e > 4]
print(r2)




