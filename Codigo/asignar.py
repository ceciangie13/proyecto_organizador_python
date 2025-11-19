from entrada_datos import *
from validaciones import *

def asignar_horario(validaciones_personal, recursos_validados, actividad, personal, recurso):
# tiempo_recursos
    """ Recibe:
    - tiempos_validados: resultado de validar_tiempos()
    - recursos_validados: resultado de validar_recursos()
    - tiempo_recursos: resultado de actividades_vs_recursos()
    - actividades: estructura original de actividades ingresadas por el usuario
    - personal: estructura original de personas_disponibles()
    - recursos: estructura original de recursos_disponibles()

    Todos los datos anteriores llegan en forma de diccionarios o listas de diccionarios.

    La función debe:
    - combinar todas las validaciones
    - seleccionar qué persona, qué recurso y en qué horario puede ejecutarse cada actividad
    - evitar solapamientos
    - respetar disponibilidad de tiempo, persona y recurso

    Devuelve:
    Un diccionario por día, donde cada día contiene una lista de actividades ya asignadas.
    Cada actividad asignada se representa con un diccionario que contiene:
        - "actividad": nombre de la actividad
        - "persona": nombre del personal asignado
        - "recurso": recurso asignado (si aplica)
        - "inicio": hora de inicio
        - "fin": hora de fin
    """
    horario_final = {}  # Inicializamos el diccionario por día


    for iterador in actividad:
        nombre_actividad = iterador["Actividad"]
        requiere_recurso= iterador["Requiere recurso"]
        duracion = iterador["Duración"]  
        disponibilidad_actividad = iterador["Disponibilidad"]

        for dia, intervalos in disponibilidad_actividad.items():
            if dia != horario_final:
                horario_final[dia] = []

            persona_asignada = None
            recurso_asignado = None

            for iterador1 in personal:
                nombre_persona = iterador1["Nombre"]
                if dia in validaciones_personal[nombre_persona]["Días disponibles"]:
                    persona_asignada = nombre_persona
                    break  

            if requiere_recurso and recursos_validados[nombre_actividad]:
                for iterador2 in actividad["Recursos"]:
                    nombre_recurso = iterador2["nombre"]
                    if recursos_validados[nombre_actividad][nombre_recurso]["Existe"]:
                        recurso_asignado = nombre_recurso
                        break  

            actividad_asignada = {"Actividad": nombre_actividad,"Persona Asignada": persona_asignada,"Recurso": recurso_asignado, "Inicio": intervalos[0][0], "Fin": intervalos[0][1] }

            horario_final[dia].append(actividad_asignada)

            return horario_final

    return