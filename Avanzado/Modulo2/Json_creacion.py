#importamos la libreria json
import json
# un objeto de tipo Diccionario:

obj = {
    "nombre": "Edgar Burbano",
    "edad": 32,
    "ciudad": "Bolivar"
}

#guardar en un archivo JSON:
with open( "D:/MAURICIO/PYTHON/FUNDAMENTOS_PYTHON/NETZUN/Avanzado/Modulo2/eburbano.json", "w") as outfile:
    # convertit a JSON:
    json.dump(obj, outfile)