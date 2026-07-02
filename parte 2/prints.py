def mostrar_egresados(lista):
    if len(lista) == 0:
        print("No hay alumnos de ese plan")
    else:
        for i in range(len(lista)):
            print("Legajo: " + str(lista[i]["legajo"]) + " | Nombre: " + lista[i]["nombre"] + " " + lista[i]["apellido"])

def mostrar_egresados_anteriores_2000(lista, promedio):
    if len(lista) == 0:
        print("No hay egresados anteriores al año 2000")
    else:
        print("=== EGRESADOS ANTERIORES AL 2000 ===")
        for i in range(len(lista)):
            print("Legajo: " + str(lista[i]["legajo"]) + " | Nombre: " + lista[i]["nombre"] + " " + lista[i]["apellido"] + " | Egreso: " + str(lista[i]["egreso"]))
        print("Promedio general: " + str(promedio))

def mostrar_busqueda(lista):
    if len(lista) == 0:
        print("No se encontraron alumnos")
    else:
        print("=== RESULTADOS DE BUSQUEDA ===")
        print("Se encontraron " + str(len(lista)) + " alumnos")
        for i in range(len(lista)):
            print("Legajo: " + str(lista[i]["legajo"]) + " | Nombre: " + lista[i]["nombre"] + " " + lista[i]["apellido"])


def mostrar_salon_de_la_fama(lista):
    if len(lista) == 0:
        print("No hay alumnos con promedio mayor o igual a 9")
    else:
        print("=== SALON DE LA FAMA ===")
        for i in range(len(lista)):
            print("Nombre: " + lista[i]["nombre"] + " " + lista[i]["apellido"] + " | Promedio: " + str(lista[i]["nota_promedio"]))