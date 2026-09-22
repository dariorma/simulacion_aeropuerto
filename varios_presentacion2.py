#Raiz entera

def raiz_cuadrada_entera(n):
    x = 0

    while (x + 1) * (x + 1) <= n:
        x = x + 1

    return x


n = int(input("Introduce un numero: "))

resultado = raiz_cuadrada_entera(n)

print("La raiz cuadrada entera es:", resultado)