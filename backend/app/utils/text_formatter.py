"""
Utilidades para formatear textos provenientes de la base de datos.
"""

# Palabras de conexión comunes que deben mantenerse en minúscula (excepto al inicio)
PALABRAS_CONEXION = {'de', 'del', 'y', 'la', 'el', 'en', 'por', 'para', 'con', 'sin', 'a', 'al'}


def formatear_texto(texto: str) -> str:
    """
    Formatea un texto según las reglas:
    - Si es una sola palabra y parece ser una sigla (todo mayúsculas o <= 3 caracteres), 
      dejarlo todo en mayúsculas
    - Si tiene múltiples palabras, aplicar Title Case:
      - Primera letra de cada palabra en mayúscula, resto en minúscula
      - Palabras de conexión comunes se mantienen en minúscula (excepto al inicio)
      - Siglas cortas (<= 3 caracteres) se mantienen en mayúsculas
    
    Args:
        texto: Texto a formatear
        
    Returns:
        Texto formateado
    """
    if not texto or not texto.strip():
        return texto
    
    texto = texto.strip()
    palabras = texto.split()
    
    # Si es una sola palabra
    if len(palabras) == 1:
        palabra = palabras[0]
        # Si es todo mayúsculas o tiene 3 o menos caracteres, probablemente es una sigla
        if palabra.isupper() or len(palabra) <= 3:
            return palabra.upper()
        else:
            # Title case para palabras normales
            return palabra.capitalize()
    
    # Si tiene múltiples palabras, aplicar Title Case inteligente
    palabras_formateadas = []
    for i, palabra in enumerate(palabras):
        palabra_lower = palabra.lower()
        
        # Si es una palabra de conexión y no es la primera palabra, mantenerla en minúscula
        if palabra_lower in PALABRAS_CONEXION and i > 0:
            palabras_formateadas.append(palabra_lower)
        # Si es una sigla corta (todo mayúsculas y <= 3 caracteres), mantenerla en mayúsculas
        elif palabra.isupper() and len(palabra) <= 3:
            palabras_formateadas.append(palabra.upper())
        else:
            # Title case para palabras normales
            palabras_formateadas.append(palabra.capitalize())
    
    return ' '.join(palabras_formateadas)

