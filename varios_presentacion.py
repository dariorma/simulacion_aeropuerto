#Módulo

def modulo(a, b):
    division = a // b
    multiplicacion = division * b
    resto = a - multiplicacion

    return resto


a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))

resultado = modulo(a, b)

print("El resto es:", resultado)


