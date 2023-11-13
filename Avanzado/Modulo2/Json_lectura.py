#importamos la libreria json
import json

#leer el archivo JSON
with open( "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/eburbano.json", "r") as json_file:
    data = json.load(json_file)
    #diccionario = data[]
    #print(data)
    #print(diccionario)
    #print('nombre:', diccionario['nombre'])
    #print('edad:', diccionario['edad'])
    #print('ciudad:', diccionario['ciudad'])
    
print(json.dumps(data, indent=2))