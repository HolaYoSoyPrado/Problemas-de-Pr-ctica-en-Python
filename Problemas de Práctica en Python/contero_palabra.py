def conteo_palabras(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()
    
    # Dividir el texto en palabras usando espacios
    palabras = texto.split()
    
    # Crear un diccionario para almacenar el conteo
    conteo = {}
    
    # Contar cada palabra
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1  # Si ya está, incrementar el conteo
        else:
            conteo[palabra] = 1  # Si no está, inicializar en 1
    
    # Devolver el diccionario con el conteo de palabras
    return conteo

# Ejemplo de uso
texto = "Hola mundo hola"
resultado = conteo_palabras(texto)
print(resultado)
