try:
    # ZeroDivisionError: division by zero
    resultado = 10 * (1/0)
except:
    print("Error de sintaxis, ZeroDivisionError: division by zero")
    
# NameError
try:
    print(4 + spam*3)
except:
    print("Error de NameError:")
    
# TypeError
try:
    resultado = '2' + 2
except:
    print("Error de TypeError:")

print("hemos gestionado las excepciones")