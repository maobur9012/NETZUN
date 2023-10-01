dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Utilizando for")
for item in dias:
    print(item)
print("-----------------")

print("Utilizando un range")
for i in range(len(dias)):
    print(dias[i])    
print("-----------------")

print("Utilizando enumerate")
for i, item in enumerate(dias):
    print(i, item)

