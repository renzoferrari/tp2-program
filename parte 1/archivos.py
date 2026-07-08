from datetime import date

def cargar_desde_csv(nombre_archivo: str) -> list:
    """
    Lee un archivo CSV y retorna una matriz con los datos.
    Recibe el nombre del archivo como parametro.
    """
    matriz = []
    archivo = open(nombre_archivo, "r")
    archivo.readline()  
    linea = archivo.readline()
    while linea != "":
        cadena_actual = ""
        fila = []
        for i in range(len(linea)):
            if linea[i] == ",":
                fila.append(int(cadena_actual))
                cadena_actual = ""
            else:
                if linea[i] != "\n":
                    cadena_actual = cadena_actual + linea[i]
        fila.append(int(cadena_actual))
        matriz.append(fila)
        linea = archivo.readline()
    archivo.close()
    return matriz

def guardar_csv(matriz: list, cabecera: str) -> str:
    """
    Guarda una matriz en un archivo CSV con la fecha actual como nombre.
    Recibe la cabecera como parametro para ser reutilizable.
    """
    fecha = date.today()
    nombre_archivo = str(fecha.day) + "-" + str(fecha.month) + "-" + str(fecha.year) + ".csv"
    archivo = open(nombre_archivo, "w")
    archivo.write(cabecera + "\n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            archivo.write(str(matriz[i][j]))
            if j < len(matriz[i]) - 1:
                archivo.write(",")
        archivo.write("\n")
    archivo.close()
    return nombre_archivo