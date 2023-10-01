PI = 3.1415

def area_circulo(radio):
    area = PI*pow(radio, 2)
    return area

print(PI)
radio = float(input("Radio: "))
resultado = area_circulo(radio)
print("el area del circulo con radio {} es {}".format(radio, resultado))