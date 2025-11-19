from librerias  import normalizar_texto
from datetime import datetime
from entrada_datos import tiempo_disponible
from entrada_datos import recursos_disponibles
from entrada_datos import *
from validaciones import *
from asignar import *
from visualizar import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas




actividades_test = actividades()
#personal_test = personas_disponibles()
recursos_test = recursos_disponibles()
#tiempos_test = tiempo_disponible()

# Probar validaciones
from validaciones import *

#val_act_rec = actividades_vs_recursos(actividades_test,recursos_test )
#print(val_act_rec)