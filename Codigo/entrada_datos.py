#No tiene parámetros porque recibe datos del usuario

from librerias import normalizar_texto
from datetime import datetime, time

def tiempo_disponible():
    #Definir los días a la semana disponibles y cada uno qué horas está disponible
    """
Características a cumplir. 
Se debe recibir día y horas disponibles.
Un día puede tener varios tramos horarios.
Debe permitir cambios → listas, no tuplas.
No se sabe cuántos tramos → usar estructura flexible.

Devuelve un diccionario de día con lista de rangos horas (tuplas con strings)
"""
    diccionario_tiempos = {}
    dias= int(input("Escriba la cantidad de días con disponibilidad: "))
    contador = 1 
    
    while contador <= dias :
        clave_dia = normalizar_texto(input("Nombre del día " + str(contador) +": "))
        diccionario_tiempos[clave_dia] = []  
        
        bloques="si"
        while bloques== "si":
            while True:
                try:
                    inicio = datetime.strptime(input("Hora de inicio Formato 24 horas HH:MM (Ej.20:30): "), "%H:%M").time()
                    break
                except ValueError:
                    print("Formato incorrecto, inténtelo de nuevo (Ej. 08:30). ")

            while True:
                try:
                    fin = datetime.strptime(input("Hora de finalización Formato 24 horas HH:MM (Ej.20:30): "), "%H:%M").time()
                    break
                except ValueError:
                    print("Formato incorrecto, inténtelo de nuevo (Ej. 08:30)")

            diccionario_tiempos[clave_dia].append((inicio, fin))
        
            bloques =normalizar_texto(input("¿Desea agregar otro bloque? Si / No "))
            while bloques not in ["si", "no"]:
                bloques = normalizar_texto(input("Respuesta no válida. Por favor, escriba Si o No: "))

        contador += 1
    
    return diccionario_tiempos 
   

def actividades():
    #Aquí se ingresaran las actividades, si están predefinidas, recursos necesarios
    """
Una lista formada por diccionarios con nombre, duración (string),disponibilidad(formato de función tiempos), requiere_recurso (booleano), recurso(lista)
"""
    lista_actividades = []
    cantidad= int(input("Escriba la cantidad de actividades a ingresar: "))
    contador = 1 
    
    while contador <= cantidad :
        nombre_act = normalizar_texto(input("Nombre de la actividad a agregar: "))
        duracion = input("Ingrese la duración de la actividad: ")
        disponibilidad = tiempo_disponible()
        
        requerimiento = normalizar_texto(input("¿Esta actividad requiere recursos? Si/No: "))
        if requerimiento=="si":
            recursos = recursos_disponibles()
        elif requerimiento=="no":
            recursos = []
        
        actividades = {"Actividad": nombre_act, "Duración": duracion, "Disponibilidad": disponibilidad, "Requiere recurso" : (requerimiento == "si"),"Recursos": recursos}
        lista_actividades.append(actividades)

        print(lista_actividades)
        contador += 1

    return lista_actividades



def personas_disponibles():
    #Definir la cantidad de personas disponibles, registro de identificación con nombre, su disponibilidad
    """Lista de diccionarios con nombre, disponibilidad(formato de función tiempos)"""
    lista_personas = []

    decision = normalizar_texto(input("Desea agregar personal? Si/No: "))
    while decision not in ["si", "no"]:
        decision = normalizar_texto(input("Respuesta no válida. Escriba Si o No: "))
    if decision=="no":
        print ("Se continuará a la siguiente sección.")
        pass
    else:
        while decision=="si":
            nombre_personal= normalizar_texto(input("Nombre de la persona a ingresar: "))
            disponibilidad = tiempo_disponible()
            personal = {"Nombre": nombre_personal, "Disponibilidad": disponibilidad}

            lista_personas.append(personal)
            decision = normalizar_texto(input("¿Desea agregar a otra persona? Si/No: "))

            while decision not in ["si", "no"]:
                decision = normalizar_texto(input("Respuesta no válida. Escriba SiNo: "))
        
        print(lista_personas)
    return lista_personas



def recursos_disponibles():
    """Lista de diccionarios con nombre, disponibilidad(formato de función tiempos), cantidad(entero)"""
    lista_recursos = []# inicializando una lista


    decision = normalizar_texto(input("Desea agregar recursos? Si/No: "))
    while decision not in ["si", "no"]:
        decision = normalizar_texto(input("Respuesta no válida. Escriba Si o No: "))
    if decision=="no":
        print ("Se continuará a la siguiente sección.")
        pass
    else:

        while decision=="si":
            nombre_recurso= normalizar_texto(input("Nombre del recurso: "))
            cantidad= int(input("Agregar la cantidad disponible del recurso: "))
            disponibilidad = tiempo_disponible()
            recurso = {"nombre": nombre_recurso, "cantidad": cantidad, "disponibilidad": disponibilidad}

            lista_recursos.append(recurso)
            decision = normalizar_texto(input("¿Desea agregar otro recurso? Si/No: "))

        while decision not in ["si", "no"]:
            decision = normalizar_texto(input("Respuesta no válida. Escriba SiNo: "))
    
    return lista_recursos

