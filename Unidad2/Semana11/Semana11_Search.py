# Definir la matriz bidimensional de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorrer las filas
        for j in range(len(matriz[i])):  # Recorrer las columnas
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no se encontró en la matriz"

# Definir el valor a buscar
valor_a_buscar = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)
