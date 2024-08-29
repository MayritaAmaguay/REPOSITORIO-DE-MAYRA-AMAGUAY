def buscar_valor_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j
    return None

# Definimos una matriz 3x3
matriz = [
    [5, 8, 12],
    [14, 3, 7],
    [9, 11, 6]
]

# Definimos el valor que queremos buscar
valor_buscado = 7

# Realizamos la búsqueda
posicion = buscar_valor_en_matriz(matriz, valor_buscado)

# Mostramos el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
