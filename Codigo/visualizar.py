"""
    Recibe:
    Un diccionario por día de la funcion asignar_horario(), donde cada día contiene una lista de actividades ya asignadas.
    Cada actividad asignada se representa con un diccionario que contiene:
        - "actividad": nombre de la actividad
        - "persona": nombre del personal asignado
        - "recurso": recurso asignado (si aplica)
        - "inicio": hora de inicio
        - "fin": hora de fin

    La función debe:
    - Convertir el diccionario en algo visual de fácil entendimiento para el usuario

    Devuelve:
    Un string que contiene el horario completo, listo para:
       - mostrar en consola,
       - exportar en PDF,
       - o guardarse en un archivo de texto

    """
from asignar import *

def genera_horario(diccionario_horario):
    
    horario = ""

    # Recorrer cada día
    for dia, actividades in diccionario_horario.items():
        horario += f"{dia}:\n"  
        if not actividades:  
            horario += "  No hay actividades asignadas.\n"
            continue

        # Recorrer cada actividad del día
        for iterador in actividades:
            nombre = iterador.get("Actividad", "Actividad sin nombre")
            persona = iterador.get("Persona Asignada", "Sin persona asignada")
            recurso = iterador.get("Recurso", "Sin recurso")  # Puede estar vacío
            inicio = iterador.get("Inicio", "??:??")
            fin = iterador.get("Fin", "??:??")

            # Formato de línea tipo tabla
            horario += f"  [{inicio} - {fin}] Actividad: {nombre}, Persona: {persona}"
            if recurso != "Sin recurso":
                horario += f", Recurso: {recurso}"
            horario += "\n"  # Salto de línea

        horario += "\n"  # Separación entre días

    return horario