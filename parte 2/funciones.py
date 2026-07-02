import random
from inputs import *

def generar_legajo(alumnos):
    legajo = random.randint(100000, 999999)
    existe = False
    for i in range(len(alumnos)):
        if alumnos[i]["legajo"] == legajo:
            existe = True
            break
    if existe:
        legajo = generar_legajo(alumnos)
    return legajo

def cargar_manual(alumnos):
    nombre = pedir_nombre("Ingrese nombre: ")
    apellido = pedir_nombre("Ingrese apellido: ")
    egreso = pedir_egreso("Ingrese año de egreso: ")
    plan = pedir_plan("Ingrese plan (1991, 2003, 2024): ")
    nota_promedio = pedir_nota_promedio("Ingrese nota promedio: ")
    legajo = generar_legajo(alumnos)
    
    alumno = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "egreso": egreso,
        "plan": plan,
        "nota_promedio": nota_promedio
    }
    
    print("=== DATOS DEL ALUMNO ===")
    print("Legajo: " + str(alumno["legajo"]))
    print("Nombre: " + alumno["nombre"])
    print("Apellido: " + alumno["apellido"])
    print("Egreso: " + str(alumno["egreso"]))
    print("Plan: " + str(alumno["plan"]))
    print("Nota promedio: " + str(alumno["nota_promedio"]))
    
    confirmacion = pedir_opcion("¿Confirma la carga? (1=Si, 2=No): ", 1, 2)
    if confirmacion == 1:
        alumnos.append(alumno)
        print("Alumno agregado correctamente!")
    else:
        print("Carga cancelada")

def obtener_egresados_por_plan(alumnos, plan):
    resultado = []
    for i in range(len(alumnos)):
        if alumnos[i]["plan"] == plan:
            resultado.append(alumnos[i])
    return resultado

def obtener_egresados_anteriores_2000(alumnos):
    resultado = []
    for i in range(len(alumnos)):
        if alumnos[i]["egreso"] < 2000:
            resultado.append(alumnos[i])
    return resultado

def calcular_promedio_general(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]["nota_promedio"]
    promedio = suma / len(lista)
    return int(promedio * 100) / 100

def transformar_a_minuscula(cadena):
    resultado = ""
    for i in range(len(cadena)):
        valor_ascii = ord(cadena[i])
        if valor_ascii >= 65 and valor_ascii <= 90:  
            resultado = resultado + chr(valor_ascii + 32)  
        else:
            resultado = resultado + cadena[i]
    return resultado

def contiene(cadena, subcadena):
    cadena = transformar_a_minuscula(cadena)      
    subcadena = transformar_a_minuscula(subcadena)
    longitud_sub = len(subcadena)
    for i in range(len(cadena) - longitud_sub + 1):
        encontrado = True
        for j in range(longitud_sub):
            if cadena[i + j] != subcadena[j]:
                encontrado = False
                break
        if encontrado:
            return True
    return False

def buscar_por_nombre_o_apellido(alumnos, texto):
    resultado = []
    for i in range(len(alumnos)):
        if contiene(alumnos[i]["nombre"], texto) or contiene(alumnos[i]["apellido"], texto):
            resultado.append(alumnos[i])
    return resultado

def obtener_salon_de_la_fama(alumnos):
    resultado = []
    for i in range(len(alumnos)):
        if alumnos[i]["nota_promedio"] >= 9:
            resultado.append(alumnos[i])
    return resultado

def ordenar_por_nota(lista):
    n = len(lista)
    for i in range(n - 1):
        hubo_swap = False
        for j in range(n - i - 1):
            if lista[j]["nota_promedio"] < lista[j+1]["nota_promedio"]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                hubo_swap = True
        if hubo_swap == False:
            break
    return lista