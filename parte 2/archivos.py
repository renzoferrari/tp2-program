import json
import os

def cargar_desde_json():
    ruta = os.path.dirname(__file__) + "/alumnos.json"
    archivo = open(ruta, "r")
    contenido = archivo.read()
    alumnos = json.loads(contenido)
    archivo.close()
    return alumnos

def guardar_json(alumnos):
    ruta = os.path.dirname(__file__) + "/alumnos.json"
    archivo = open(ruta, "w")
    contenido = json.dumps(alumnos, indent=4)
    archivo.write(contenido)
    archivo.close()