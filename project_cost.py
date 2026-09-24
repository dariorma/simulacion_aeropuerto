def project_cost(nombre, cantidad, precio):
    if len(nombre) != len(cantidad):
        raise ValueError("nombre y cantidad deben tener la misma longitud")

    total = 0
    for i in range(len(nombre)):
        if not isinstance(cantidad[i], int) or cantidad[i] < 0:
            raise ValueError(f"cantidad invalida para '{nombre[i]}'")

        if nombre[i] not in precio:
            raise ValueError(f"recurso desconocido: '{nombre[i]}'")

        total += precio[nombre[i]] * cantidad[i]

    return total


if __name__ == "__main__":
    precios = {"Pilotos": 300, "Azafatas": 150, "Carburante": 2, "Mantenimiento": 800}

    print(project_cost(
        ["Pilotos", "Azafatas", "Carburante", "Mantenimiento"],
        [2, 4, 500, 1],
        precios,
    ))
