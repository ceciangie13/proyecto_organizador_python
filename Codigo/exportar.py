from visualizar import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def exportar_texto(diccionario_horario, nombre_archivo="horario.txt"):
    """
    Guarda el horario como archivo de texto.
    """
    horario_string = genera_horario(diccionario_horario)
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(horario_string)
    print(f"Horario guardado en {nombre_archivo}")


def exportar_pdf(diccionario_horario, nombre_archivo="horario.pdf"):
    """
    Guarda el horario como PDF simple.
    """
    horario_string = genera_horario(diccionario_horario)
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    y = height - 40  

    for linea in horario_string.split("\n"):
        c.drawString(30, y, linea)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    print(f"Horario exportado a {nombre_archivo}")

def formato_imagen(horario_string):
    """
    Recibe un string generado por genera_horario(), con el formato final del horario.
    Funciones:
        - Convertir ese horario en una imagen (PNG o JPG).
        - Organizar el texto en bloques visuales (similar a una tabla simple).
        - Preparar la imagen para guardarla o mostrarla.
    Devuelve un documento tipo JPG con la representación del horario
    """  
    return

