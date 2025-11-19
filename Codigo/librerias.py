# utils.py
import unicodedata

def normalizar_texto(texto):
    # Convierte a minúsculas y quita tildes
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

