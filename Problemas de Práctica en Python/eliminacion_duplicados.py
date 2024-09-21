def eliminar_duplicados(lista):
    # Nueva lista para almacenar elementos únicos
    lista_sin_duplicados = []
    
    # Iterar a través de la lista original
    for elemento in lista:
        # Verificar si el elemento ya está en la nueva lista
        if elemento not in lista_sin_duplicados:
            # Agregarlo si no está presente
            lista_sin_duplicados.append(elemento)
    
    # Devolver la nueva lista sin duplicados
    return lista_sin_duplicados


# Ejemplos de uso
lista_original = [1, 2, 3, 2, 4, 5, 3, 6]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(lista_sin_duplicados)  # Imprime: [1, 2, 3, 4, 5, 6]


