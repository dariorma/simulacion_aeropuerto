def matriz_sum(a, b):
    resultado = []

    if len(a) != len(b):
        raise ValueError("Las matrices no tiene el mismo tamaño")

    if len({len(fila) for fila in a})>1:
        raise ValueError("Las filas son desiguales")

    if len({len(fila) for fila in b})>1:
        raise ValueError("Las filas son desiguales")

    if len(a[0]) != len(b[0]):
        raise ValueError("el tamaño de las filas es distinto")
    
    for i in range(len(a)):
        fila_actual = []
        for j in range(len(a[0])):
            suma = a[i][j] + b[i][j]
            fila_actual.append(suma)
        resultado.append(fila_actual)
    return resultado

def elementwise_array_sum(a,b):
    res=[]
    if len(a) != len(b):
        raise ValueError("Tamanyo distinto")
    for i in range(len(a)):
        suma = a[i]+b[i]
        res.append(suma)
    return res