def son_anagramas(cadena1, cadena2):
    # Eliminar espacios y convertir a minúsculas
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()

    # Ordenar las letras de cada cadena
    letras_cadena1 = sorted(cadena1)
    letras_cadena2 = sorted(cadena2)

    # Comparar las listas ordenadas
    return letras_cadena1 == letras_cadena2

# Ejemplo de uso
resultado = son_anagramas("amor", "roma")
print(resultado)  # Debería imprimir True
