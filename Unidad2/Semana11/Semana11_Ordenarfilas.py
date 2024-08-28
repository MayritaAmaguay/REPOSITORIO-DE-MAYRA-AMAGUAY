# Definir la matriz bidimensional de 3x3
matriz = [
    [9, 5, 3],
    [8, 2, 7],
    [6, 4, 1]
]

# Función para ordenar una fila específica utilizando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar los elementos
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
