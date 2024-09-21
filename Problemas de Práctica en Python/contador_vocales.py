#contador de vocales
def contar_vocales(cadena):
    # 1. Definir las vocales (tanto en minúscula como en mayúscula)
    vocales = "aeiouAEIOU"
    
    # 2. Inicializar un contador en 0
    contador = 0
    
    # 3. Recorrer cada carácter en la cadena
    for caracter in cadena:
        # 4. Si el carácter es una vocal, incrementar el contador
        if caracter in vocales:
            contador += 1
    
    # 5. Devolver el total de vocales contadas
    return contador

# Ejemplo de uso
resultado = contar_vocales("Hola Mundo")
print(f"Número de vocales: {resultado}")

