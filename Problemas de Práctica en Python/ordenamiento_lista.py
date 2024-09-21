def ordenamiento_burbuja(lista):
    # Determinamos la longitud de la lista
    n = len(lista)
    
    # Bucle externo para recorrer la lista varias veces
    for i in range(n):
        # Bucle interno para comparar elementos adyacentes
        for j in range(0, n-i-1):  # Últimos elementos ya están en su lugar
            # Comparar si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                # Intercambiar si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada:", ordenamiento_burbuja(numeros))
