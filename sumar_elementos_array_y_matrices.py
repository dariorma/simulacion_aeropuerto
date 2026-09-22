numeros = [1, 2, 3, 4, 5]
suma_total = 0

for n in numeros:
    suma_total += n

print(suma_total)  # Imprime 15





def sumar_matrices(matriz_a, matriz_b):
    # Crear una matriz vacía para el resultado
    resultado = []
    
    # Recorrer las filas
    for i in range(len(matriz_a)):
        fila_actual = []
        # Recorrer las columnas
        for j in range(len(matriz_a[0])):
            # Sumar elementos en la misma posición
            suma = matriz_a[i][j] + matriz_b[i][j]
            fila_actual.append(suma)
        resultado.append(fila_actual)
        
    return resultado

# Definir dos matrices de 2x2
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Obtener la suma
matriz_suma = sumar_matrices(A, B)
print(matriz_suma)  # Salida: [[6, 8], [10, 12]]
