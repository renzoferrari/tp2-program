def cargar_desde_csv():
    matriz = []
    archivo = open("notas.csv", "r")
    linea = archivo.readline()  # saltamos el encabezado
    linea = archivo.readline()  # primera línea de datos
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

from datetime import date

def guardar_csv(matriz):
    fecha = date.today()
    nombre_archivo = str(fecha.day) + "-" + str(fecha.month) + "-" + str(fecha.year) + ".csv"
    archivo = open(nombre_archivo, "w")
    archivo.write("trimestre1,trimestre2,trimestre3\n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            archivo.write(str(matriz[i][j]))
            if j < len(matriz[i]) - 1:
                archivo.write(",")
        archivo.write("\n")
    archivo.close()
    return nombre_archivo