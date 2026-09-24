def create_tasks(names, quantities, hours):
    if len(names) != len(quantities):
        raise ValueError("names y quantities deben tener la misma longitud")

    tasks = []
    for i in range(len(names)):
        if not isinstance(quantities[i], int) or quantities[i] < 0:
            raise ValueError(f"cantidad invalida para '{names[i]}'")

        if names[i] not in hours:
            raise ValueError(f"recurso desconocido: '{names[i]}'")

        if hours[names[i]] <= 0:
            raise ValueError(f"horas invalidas para '{names[i]}'")

        tasks.extend([names[i]] * quantities[i])

    return tasks


if __name__ == "__main__":
    horas = {"Pilotos": 8, "Azafatas": 6, "Mantenimiento": 4}

    print(create_tasks(
        ["Pilotos", "Azafatas", "Mantenimiento"],
        [2, 3, 1],
        horas,
    ))
