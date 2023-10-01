#Matriz: lista de lista

c = [[2, 3, 4],
     [40, 50, 60],
     [100, 200, 300]
     ]

# equivalente usando for
total = 0
for row in c:
    for x in row:
        total += x
print(total)

#Suma total
total_comprension = [x for row in c for x in row]
print(total_comprension)

print(sum(total_comprension))

