dependencias = {
    "Vuelos": ["Pasajeros", "Tripulacion", "Avion"],
    "Pasajeros": ["Equipaje"],
    "Equipaje": ["Seguridad"],
    "Seguridad": [],
    "Tripulacion": ["Pilotos", "Azafatas"],
    "Pilotos": [],
    "Azafatas": [],
    "Avion": ["Mantenimiento", "Carburante"],
    "Mantenimiento": [],
    "Carburante": []
}

def falta_predecesores(plan, grafo):
    plan_set = set(plan)

    for elemento in plan: # recorro los elementos del plan
        requisitos = grafo.get(elemento, [])
        for requisito in requisitos: # recorro uno por uno las dependencias 
            if requisito not in plan_set:
                return (elemento, requisito) 
    return None  

BLANCO, GRIS, NEGRO= 0, 1, 2

def detectar_ciclo(grafo):
    estado = {nodo: BLANCO for nodo in grafo}
    camino = []

    def visitar(nodo): 
        estado[nodo] = GRIS
        camino.append(nodo)

        for requisito in grafo.get(nodo, []):
            if estado.get(requisito, BLANCO) == GRIS:
                inicio = camino.index(requisito)
                return camino[inicio:] + [requisito]
            if estado.get(requisito, BLANCO) == BLANCO:
                ciclo = visitar(requisito)
                if ciclo:
                    return ciclo

        camino.pop()
        estado[nodo] = NEGRO
        return None

    for nodo in grafo:
        if estado[nodo] == BLANCO:
            ciclo = visitar(nodo)
            if ciclo:
                return ciclo

    return None


def verificar_bloqueo(plan, grafo):
    ciclo = detectar_ciclo(grafo)
    if ciclo:
        return True, "Proyecto bloqueado: ciclo de dependencias detectado (" + " -> ".join(ciclo) + ")"

    resultado = falta_predecesores(plan, grafo)
    if resultado:
        elemento, requisito = resultado
        return True, f"Proyecto bloqueado: '{elemento}' requiere '{requisito}', que no ha sido planificado"

    return False, None