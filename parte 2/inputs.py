def pedir_nombre(mensaje):
    while True:
        cadena = input(mensaje)
        if len(cadena) >= 3:
            es_valido = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if (valor_ascii < 65 or valor_ascii > 90) and (valor_ascii < 97 or valor_ascii > 122) and valor_ascii != 32:
                    es_valido = False
                    break
            if es_valido:
                return cadena
            else:
                print("Error: solo se permiten letras y espacios")
        else:
            print("Error: mínimo 3 caracteres")

def pedir_egreso(mensaje):
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            es_numero = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii < 48 or valor_ascii > 57:
                    es_numero = False
                    break
            if es_numero:
                numero = int(cadena)
                if numero >= 1991 and numero <= 2026:
                    return numero
                else:
                    print("Error: el año debe estar entre 1991 y 2026")
            else:
                print("Error: ingresaste caracteres inválidos")
        else:
            print("Error: no puede estar vacío")

def pedir_plan(mensaje):
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            es_numero = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii < 48 or valor_ascii > 57:
                    es_numero = False
                    break
            if es_numero:
                numero = int(cadena)
                if numero == 1991 or numero == 2003 or numero == 2024:
                    return numero
                else:
                    print("Error: el plan debe ser 1991, 2003 o 2024")
            else:
                print("Error: ingresaste caracteres inválidos")
        else:
            print("Error: no puede estar vacío")

def pedir_nota_promedio(mensaje):
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            es_valido = True
            cantidad_puntos = 0
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii == 46:  # el punto tiene ascii 46
                    cantidad_puntos = cantidad_puntos + 1
                    if cantidad_puntos > 1:  # no puede haber más de un punto
                        es_valido = False
                        break
                elif valor_ascii < 48 or valor_ascii > 57:
                    es_valido = False
                    break
            if es_valido:
                numero = float(cadena)
                if numero >= 6 and numero <= 10:
                    return numero
                else:
                    print("Error: la nota debe estar entre 6 y 10")
            else:
                print("Error: ingrese un número válido (ejemplo: 8.5)")
        else:
            print("Error: no puede estar vacío")
        
def pedir_opcion(mensaje, minimo, maximo):
    while True:
        cadena = input(mensaje)
        if len(cadena) > 0:
            es_numero = True
            for i in range(len(cadena)):
                valor_ascii = ord(cadena[i])
                if valor_ascii < 48 or valor_ascii > 57:
                    es_numero = False
                    break
            if es_numero:
                numero = int(cadena)
                if numero >= minimo and numero <= maximo:
                    return numero
                else:
                    print("Error: ingrese una opción entre " + str(minimo) + " y " + str(maximo))
            else:
                print("Error: ingresaste caracteres inválidos")
        else:
            print("Error: no puede estar vacío")