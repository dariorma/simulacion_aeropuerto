from dependencias import dependencias, falta_predecesores, detectar_ciclo, verificar_bloqueo
from sumar_elementos_array_y_matrices import matriz_sum, elementwise_array_sum
from sort_array import sort_array
from project_cost import project_cost
from create_tasks import create_tasks

#sort_array
hora_salida=[14, 9, 22, 6, 18]
#duracion_vuelo=[180, 45, 300, 90]
#numero_pasajero=[220, 182, 96, 312]

salida_ordenada = sort_array(hora_salida)
print("sort_array:", salida_ordenada)

#matriz_sum filas vuelos, columnas pasajeros
#dos turnos manyana y tarde 
manyana = [[80,40], [60,30]]
tarde = [[30, 15], [90, 45]]
print("matriz_sum:", matriz_sum(manyana, tarde))


#elementwise_array_sum lista combustible reservado y lista combustibles extra
reservado=[500, 750, 600]
extra=[100, 135, 95 ]
print("elementwise_array_sum:", elementwise_array_sum(reservado, extra))

#igual para pasajeros turista y business
#turista=[120,105,132]
#business=[35,30,15]

plan_incompleto = ["Vuelos"]
print("falta_predecesores (incompleto):", falta_predecesores(plan_incompleto, dependencias))

plan_completo = list(dependencias.keys())
print("falta_predecesores (completo):", falta_predecesores(plan_completo, dependencias))

print("detectar_ciclo:", detectar_ciclo(dependencias))

print("verificar_bloqueo (incompleto):", verificar_bloqueo(plan_incompleto, dependencias))
print("verificar_bloqueo (completo):", verificar_bloqueo(plan_completo, dependencias))

#project_cost: coste de los recursos necesarios para operar los vuelos
precios = {"Pilotos": 300, "Azafatas": 150, "Carburante": 2, "Mantenimiento": 800}
nombres_coste = ["Pilotos", "Azafatas", "Carburante", "Mantenimiento"]
cantidades_coste = [2, 4, 500, 1]
print("project_cost:", project_cost(nombres_coste, cantidades_coste, precios))

#create_tasks: desglose de recursos en tareas individuales
horas = {"Pilotos": 8, "Azafatas": 6, "Mantenimiento": 4}
nombres_tareas = ["Pilotos", "Azafatas", "Mantenimiento"]
cantidades_tareas = [2, 3, 1]
print("create_tasks:", create_tasks(nombres_tareas, cantidades_tareas, horas))