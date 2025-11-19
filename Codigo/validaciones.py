from entrada_datos import *

def validar_tiempos(diccionario_personal, diccionario_tiempos):
    """
Compara entre tiempo_disponible() y personas_disponibles(disponibilidad), la intersección de los días disponibles
Devuelve un diccionario el nombre de la persona y los días en que trabajará
"""
    validaciones_personal= {} #inicializar el diccionario

    #Recorrer actividades
    for iterador in diccionario_personal:
        nombre_persona = iterador["Nombre"]
        disponibilidad = iterador["Disponibilidad"]
        
        dias_disponibles={}
        
        #Recorrer cada día disponible de los tiempos
        for dia, intervalos in diccionario_tiempos.items():
            if dia in disponibilidad:
                dias_disponibles[dia]=disponibilidad[dia]
                      
            
        validaciones_personal[nombre_persona]= {"Días disponibles": dias_disponibles}      
            

    return validaciones_personal
    



def validar_recursos(lista_recursos, lista_actividades):
    """
Valida para cada actividad:
    - Si los recursos existen
    - Si las cantidades son suficientes

    Devuelve una lista de diagnósticos, uno por actividad. Actividad, requiere recurso /True, nombre recurso, cantidad suficiente True """ 

    validaciones_recursos= {} #inicializar el diccionario

    #Recorrer actividades
    for iterador in lista_actividades:
        nombre_actividad = iterador["Actividad"]
        recurso_requerido = iterador["Recursos"]
        
        validaciones_recursos[nombre_actividad] = {} #Creando una sección dentro del diccionario


        #Recorrer cada recurso de las actividades
        for iterador1 in recurso_requerido:
            nombre_recurso = iterador1["nombre"]
            cantidad_requerida = iterador1["cantidad"]
            disponibilidad_requerida = iterador1["disponibilidad"]

            existencia=False
            recurso_encontrado=None
            cantidad= False
            disponible= None
            
            #Validaciones de recursos en orden
            #EXISTENCIA DEL RECURSO
            #Entro a recorrer los recursos_disponibles
            for iterador2 in lista_recursos:
                if iterador2["nombre"]==nombre_recurso: #donde iterador2 toma el valor de cada diccionario dentro de la lista_recursos
                    existencia = True
                    recurso_encontrado=iterador2
                    break

           
            #Cantidad mínima del recurso
            #Entro a validar con el nuevo diccionario guardado
            if recurso_encontrado != None:
                if recurso_encontrado["cantidad"]>= cantidad_requerida: 
                    cantidad = True
            else:
                cantidad=False  


    validaciones_recursos[nombre_actividad][nombre_recurso] = { "Existe": existencia, "Cantidad": cantidad, "disponibilidad": disponible}      
            

    return validaciones_recursos



"""""
def actividades_vs_recursos(diccionario_actividades, diccionario_tiempos):
    
Compara entre actividades() y tiempo_disponible(), los días 
Devuelve un diccionario de las actividades y recursos con el horario del día en común "
    tiempos_recursos= {} #inicializar el diccionario

    #Recorrer actividades
    for iterador in diccionario_actividades:
        nombre_actividad = iterador["Actividad"]
        caracteristicas_recurso = iterador["Recursos"]
        
        tiempos_recursos[nombre_actividad] = {} #Creando una sección dentro del diccionario


        #Recorrer cada recurso de las actividades
        for iterador1 in caracteristicas_recurso:
            nombre_recurso = iterador1["nombre"]
            disponibilidad_requerida = iterador1["disponibilidad"]

            dias={}
                
            #Recorrer cada día disponible de los tiempos
            for dia, intervalos in diccionario_tiempos.items():
                if dia in disponibilidad_requerida:
                    dias[dia]=disponibilidad_requerida[dia]
                      
            
                tiempos_recursos[nombre_actividad][nombre_recurso]= {"Días en común": dias}      
            

    return tiempos_recursos
"""""
    

