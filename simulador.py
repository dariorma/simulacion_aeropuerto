import time

from dependencias import dependencias, detectar_ciclo

# Horas-persona necesarias para completar cada elemento del grafo de vuelos.
HORAS_NECESARIAS = {
    "Seguridad": 10,
    "Pilotos": 8,
    "Azafatas": 8,
    "Mantenimiento": 25,
    "Carburante": 12,
    "Equipaje": 15,
    "Tripulacion": 5,
    "Avion": 5,
    "Pasajeros": 20,
    "Vuelos": 10,
}


def nodos_disponibles(completados, grafo):
    disponibles = []
    for nodo in grafo:
        if nodo in completados:
            continue
        requisitos = grafo[nodo]
        if all(requisito in completados for requisito in requisitos):
            disponibles.append(nodo)
    return disponibles


def repartir_equitativo(disponibles, horas_restantes, operarios):
    if not disponibles:
        return {}

    reparto = {}
    operarios_por_nodo = operarios // len(disponibles)
    resto = operarios % len(disponibles)

    for i, nodo in enumerate(disponibles):
        asignados = operarios_por_nodo + (1 if i < resto else 0)
        reparto[nodo] = min(asignados, horas_restantes[nodo])

    return reparto


def repartir_prioridad(disponibles, horas_restantes, operarios):
    reparto = {}
    orden = sorted(disponibles, key=lambda nodo: horas_restantes[nodo])
    restantes = operarios

    for nodo in orden:
        if restantes <= 0:
            break
        asignados = min(restantes, horas_restantes[nodo])
        reparto[nodo] = asignados
        restantes -= asignados

    return reparto


def repartir_secuencial(disponibles, horas_restantes, operarios, orden_grafo):
    for nodo in orden_grafo:
        if nodo in disponibles:
            return {nodo: min(operarios, horas_restantes[nodo])}
    return {}


MODALIDADES = {
    "equitativo": repartir_equitativo,
    "prioridad": repartir_prioridad,
}


def un_paso(grafo, horas_restantes, completados, operarios, modalidad, orden_grafo):
    """Ejecuta un unico tick: reparte operarios y actualiza el estado.

    No devuelve un estado nuevo: modifica horas_restantes y completados
    directamente (son un dict y un set, se pasan por referencia).
    """
    disponibles = nodos_disponibles(completados, grafo)

    if modalidad == "secuencial":
        reparto = repartir_secuencial(disponibles, horas_restantes, operarios, orden_grafo)
    else:
        reparto = MODALIDADES[modalidad](disponibles, horas_restantes, operarios)

    completados_este_tick = []
    for nodo, horas_aplicadas in reparto.items():
        horas_restantes[nodo] -= horas_aplicadas
        if horas_restantes[nodo] <= 0:
            horas_restantes[nodo] = 0
            completados.add(nodo)
            completados_este_tick.append(nodo)

    return disponibles, reparto, completados_este_tick


def simular(grafo, horas_necesarias, operarios_por_tick, modalidad, max_ticks=100):
    if operarios_por_tick <= 0:
        raise ValueError("operarios_por_tick debe ser positivo")

    if modalidad not in MODALIDADES and modalidad != "secuencial":
        raise ValueError(f"modalidad desconocida: '{modalidad}'")

    for nodo in grafo:
        if nodo not in horas_necesarias:
            raise ValueError(f"falta horas_necesarias para '{nodo}'")
        if horas_necesarias[nodo] <= 0:
            raise ValueError(f"horas_necesarias invalidas para '{nodo}'")

    ciclo = detectar_ciclo(grafo)
    if ciclo:
        raise ValueError("El grafo tiene un ciclo, no se puede simular: " + " -> ".join(ciclo))

    horas_restantes = dict(horas_necesarias)
    completados = set()
    historial = []
    orden_grafo = list(grafo.keys())

    tick = 0
    while len(completados) < len(grafo) and tick < max_ticks:
        tick += 1
        disponibles, reparto, completados_este_tick = un_paso(
            grafo, horas_restantes, completados, operarios_por_tick, modalidad, orden_grafo
        )

        historial.append({
            "tick": tick,
            "disponibles": disponibles,
            "trabajado": reparto,
            "completados_este_tick": completados_este_tick,
        })

    return historial, completados


def simular_paso_a_paso(grafo, horas_necesarias, operarios_por_tick, modalidad, pausa=1, max_ticks=100):
    """Igual que simular(), pero imprime cada tick de forma legible y espera 'pausa' segundos entre uno y otro."""
    horas_restantes = dict(horas_necesarias)
    completados = set()
    orden_grafo = list(grafo.keys())
    total_tareas = len(grafo)

    print("\n" + "=" * 60)
    print(f" SIMULACION PASO A PASO  |  modalidad: {modalidad}")
    print("=" * 60)

    tick = 0
    while len(completados) < total_tareas and tick < max_ticks:
        tick += 1
        disponibles, reparto, completados_este_tick = un_paso(
            grafo, horas_restantes, completados, operarios_por_tick, modalidad, orden_grafo
        )

        print(f"\n--- Tick {tick} ---")
        print("Disponibles ahora    :", ", ".join(disponibles) if disponibles else "(ninguna)")

        if reparto:
            texto_reparto = ", ".join(f"{nodo} +{horas}h" for nodo, horas in reparto.items())
        else:
            texto_reparto = "(sin operarios asignados)"
        print("Operarios repartidos :", texto_reparto)

        if completados_este_tick:
            print("Completadas hoy      :", ", ".join(completados_este_tick))

        print(f"Progreso total       : {len(completados)}/{total_tareas} tareas completadas")

        pendientes = {nodo: horas for nodo, horas in horas_restantes.items() if horas > 0}
        if pendientes:
            print("Horas que faltan por tarea:")
            for nodo, horas in pendientes.items():
                print(f"   - {nodo:<15} {horas}h")

        time.sleep(pausa)

    print("\n" + "=" * 60)
    print(f" FIN: {len(completados)}/{total_tareas} tareas completadas en {tick} ticks")
    print("=" * 60 + "\n")
    return completados


if __name__ == "__main__":
    for modalidad in ("equitativo", "prioridad", "secuencial"):
        historial, completados = simular(dependencias, HORAS_NECESARIAS, operarios_por_tick=6, modalidad=modalidad)
        print(f"--- {modalidad} ---")
        print(f"ticks empleados: {len(historial)}")
        print(f"completados: {len(completados)} de {len(dependencias)}")
        for entrada in historial:
            print(entrada)
        print()
