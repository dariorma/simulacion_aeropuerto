numeros = [1, 2, 3, 4, 5]
suma_total = 0

for n in numeros:
    suma_total += n

print(suma_total) 





def sumar_matrices(matriz_a, matriz_b):
    resultado = []
    
    for i in range(len(matriz_a)):
        fila_actual = []
        for j in range(len(matriz_a[0])):
            suma = matriz_a[i][j] + matriz_b[i][j]
            fila_actual.append(suma)
        resultado.append(fila_actual)
        
    return resultado

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

matriz_suma = sumar_matrices(A, B)
print(matriz_suma) 
