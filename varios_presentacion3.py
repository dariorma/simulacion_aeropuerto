#Potencia

def potencia(x, y):
    resultado = 1

    for i in range(y):
        resultado = resultado * x

    return resultado


x = int(input("Introduce la base: "))
y = int(input("Introduce el exponente: "))

resultado = potencia(x, y)

print("El resultado es:", resultado)