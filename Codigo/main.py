"""
    Flujo:
    1. Recepción de datos, preguntar al usuario sobre la información necesaria de cada función que se encuentra en el módulo entrada_datos.
       En este se puede plantear en el módulo main preguntar al usuario si tiene algo que agregar o no, ejemplo argumentos predefinidos, si es FALSO, salte al siguiente
    2. Pasar al módulo validaciones, con la información recolectada y almacenada en el módulo recepción de datos, se ejecutan las funciones en orden
    3. Pasan los resultados al módulo asignar
    4. Pasan los resultados visualizar, en donde por medio de la consola el usuario puede visualizar su horario ya diseñado
    5. Pasan los resultados al módulo exportar y allí el usuario decide en qué tipo de archivo desea exportar y descargar el horario
    6. Finaliza

    El main funcionará de manera lineal por la facilidad de construcción de código.
    El main coordina todos los módulos y controla el orden general de la ejecución
    """
from entrada_datos import *
from validaciones import *
from asignar import *
from visualizar import *
from exportar import *

def main():
   print ("Bienvenido al organizador automático\n")
   entradas_actividades = actividades()
   entradas_personal = personas_disponibles()
   entradas_recursos = recursos_disponibles()
   entradas_tiempos = tiempo_disponible()

   print ("Analizando la información recibida")
   validacion_recursos = validar_recursos(entradas_recursos, entradas_actividades)

   #validacion_recursos_vs_act= actividades_vs_recursos(entradas_actividades, entradas_tiempos)
   validacion_personas = validar_tiempos(entradas_personal, entradas_tiempos)

   print ("Asignando actividades")

   asignacion = asignar_horario(validacion_personas, validacion_recursos, entradas_actividades, entradas_personal, entradas_recursos) 
   """validacion_recursos_vs_act"""

   print("Generando horario")
   diccionario_horario = asignacion
   horario_string = genera_horario(diccionario_horario)
   print(horario_string)

   decision = normalizar_texto(input("¿En qué formato desea exportar la información a un documento 1.TXT o 2.PDF?"))
   if decision=="1":
      exportar_texto(diccionario_horario)
   elif decision=="2":
      exportar_pdf(diccionario_horario)
   else:
      print ("Horario generado con satisfacción sin archivos extra")


if __name__ == "__main__":
   main()

