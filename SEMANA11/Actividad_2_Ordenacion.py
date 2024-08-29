# Definir la matriz bidimensional
matriz = [
    [34, 21, 12],
    [7, 15, 3],
    [16, 8, 10]
]


# Función para ordenar una fila específica utilizando Bubble Sort
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)

    # Algoritmo de ordenación Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar si el elemento encontrado es mayor
                # que el siguiente elemento
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Reemplazar la fila en la matriz original con la fila ordenada
    matriz[fila_index] = fila


# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz después de ordenar la fila específica
print("\nMatriz después de ordenar la segunda fila:")
for fila in matriz:
    print(fila)

