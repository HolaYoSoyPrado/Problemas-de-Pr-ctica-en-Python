#
def es_palindromo(cadena):
    # Normalizar la cadena
    cadena_normalizada = ''.join(c.lower() for c in cadena if c.isalnum())
    
    # Comparar la cadena normalizada con su reverso
    return cadena_normalizada == cadena_normalizada[::-1]

# Ejemplo de uso
texto = "A man, a plan, a canal: Panama"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')
